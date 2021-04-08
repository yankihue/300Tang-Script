from PIL import Image, ImageFont, ImageDraw 
import json
import random

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
else:
  print("Couldn't get poem. Please try running the application again")





base = Image.open("base.jpeg")

image_editable = ImageDraw.Draw(base)

ttf=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 64)

image_editable.text((0,0), title_text, (237, 230, 211),font=ttf)

base.save('output.jpeg')