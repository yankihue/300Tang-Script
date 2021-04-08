from PIL import Image, ImageFont, ImageDraw 
import json
import random
from time import time, sleep

while True:
    #random poem id
    n = random.randint(0,319)
    print(n)

    with open('poems.json') as f:
        data = json.load(f)


    def find_poem (n):
        for keyval in data:
            if n == keyval['id']:
                return keyval['contents']

    if (find_poem(n) != None):
        title_text=find_poem(n)

    base = Image.open("base.jpeg")

    image_editable = ImageDraw.Draw(base)

    ttf=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 48)

    w,h = image_editable.textsize(title_text, font=ttf)

    image_editable.text(((1920-w)/2,(1200-h)/2), title_text, (0, 0, 0,128),font=ttf)

    base.save('output.jpeg')

    sleep(60 - time() % 60)
