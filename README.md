# 300Tang-Script
This is a python script that I use on my desktop. It randomly picks one of the famous [320 Tang poems](https://en.wikipedia.org/wiki/Tang_poetry) and displays it on top of a painting. 
I used [this resource](https://github.com/xuchunyang/300) to get all 320 poems in JSON format. A new wallpaper will be generated overriding the old one every minute (by default).

![Screenshot](/screenshot.png)

# Usage
For Ubuntu:


Clone the repo. IMPORTANT: You have to clone it to your desktop.
```bash
cd ~/Desktop
git clone https://github.com/yankihue/300Tang-Script 300Tang
```

If you want to put it anywhere else, you should change main.py and point it at that directory([change this line](https://github.com/yankihue/300Tang-Script/blob/db4c9e56edd7b80cd49506fc5a0cc99b2559b1cb/300tang/main.py#L49)). By default the script points at desktop, inside the folder 300Tang.

You need the [WQY Microhei](https://github.com/anthonyfok/fonts-wqy-microhei) font for this to work. To install:

```bash
sudo apt-get install ttf-wqy-microhei 
```

Get [poetry](https://python-poetry.org/) if you don't have it:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
```

Afterwards, if you want to test the script first, run
```bash
poetry install
```
at the base directory of the project. Then run

```bash
python3 main.py
```
If you like it and want it to automatically run on the background starting from boot, add a .desktop file to /home/your_name/.config/autostart/
```
[Desktop Entry]
Encoding=UTF-8
Name=300Tang
Comment=Random wallpaper generator
Icon=gnome-info
Exec=python3 path/to/script/main.py
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=10
```
Modify the path and save the .desktop file.

# TODO
* Add more base images
* Add English and Pinyin
