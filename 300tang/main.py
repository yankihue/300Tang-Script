from PIL import Image, ImageFont, ImageDraw 
import json
import random
from time import time, sleep
import os


while True:
    #random poem id
    n = random.randint(1,320)
    print(n)

    with open('poems.json') as f:
        data = json.load(f)


    def find_poem (n):
        for keyval in data:
            if n == keyval['id']:
                return keyval['contents']

    if (find_poem(n) != None):
        title_text=find_poem(n)


    def find_title(n):
        for keyval in data:
            if n ==keyval['id']:
                return keyval['title']    
    if (find_title(n) != None):
        title=find_title(n)            

    base = Image.open("base.jpeg")

    image_editable = ImageDraw.Draw(base)

    ttf=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 36)

    w,h = image_editable.textsize(title_text, font=ttf)

    image_editable.text(((1920-w)/2,(1200-h)/2), title_text, (49, 27, 8,64),font=ttf)
    
    w2,h2=image_editable.textsize(title, font=ttf)

    image_editable.text(((1920-w2)/2,((1200-h)/2)-h), title, (49, 27, 8,64),font=ttf)


    base.save('output.jpeg')
    os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri ~/Desktop/300Tang/300tang/output.jpeg')
    sleep(60 - time() % 60)
