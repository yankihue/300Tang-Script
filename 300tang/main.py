#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw 
from time import time, sleep
import json, random, os

__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

while True:
    n = random.randint(1,320) # generate random poem id
    print(n)

    # with open('poems.json') as f:
       # data = json.load(f)
    with open(os.path.join(__location__, 'poems.json'),'r') as f:
        data = json.load(f)

    def find_poem (n): # extract poem from json
        for keyval in data:
            if n == keyval['id']:
                return keyval['contents']

    if (find_poem(n) != None):
        title_text=find_poem(n)


    def find_title(n): # extract poem title from json
        for keyval in data:
            if n ==keyval['id']:
                return keyval['title']    
    if (find_title(n) != None):
        title=find_title(n)            

    base = Image.open(os.path.join(__location__, 'base.jpeg')) # open base image

    image_editable = ImageDraw.Draw(base) # make it editable

    ttf=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 36) # load font

    w,h = image_editable.textsize(title_text, font=ttf) # get the size of the poem with font

    image_editable.text(((1920-w)/2,(1200-h)/2), title_text, (49, 27, 8,64),font=ttf) # center the poem itself
    
    w2,h2=image_editable.textsize(title, font=ttf) # get the size of the title with font

    image_editable.text(((1920-w2)/2,((1200-h)/2)-h), title, (49, 27, 8,64),font=ttf) # center the title horizontally, keep it above the poem vertically

    base.save('output.jpeg') # save output
    os.system('gsettings set org.gnome.desktop.background picture-uri ~/Desktop/300Tang/300tang/output.jpeg') # change GNOME wallpaper
    sleep(60 - time() % 60) # wait 1 minute
