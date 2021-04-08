from PIL import Image, ImageFont, ImageDraw 


base = Image.open("base.jpeg")

title_text = "孤鸿海上来，池潢不敢顾。\n侧见双翠鸟，巢在三珠树。\n矫矫珍木巅，得无金丸惧。\n美服患人指，高明逼神恶。\n今我游冥冥，弋者何所慕。"


image_editable = ImageDraw.Draw(base)

ttf=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 64)

image_editable.text((0,0), title_text, (237, 230, 211),font=ttf)

base.save('output.jpeg')