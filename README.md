# 300Tang-Script
This is a python script that I use on my desktop. It randomly picks one of the famous [320 Tang poems](https://en.wikipedia.org/wiki/Tang_poetry) and displays it on top of a painting. 
I used [this resource](https://github.com/xuchunyang/300) to get all 320 poems in JSON format. A new wallpaper will be generated overriding the old one every minute (by default).

![Screenshot](/screenshot.png)

# Usage
For GNOME:

Clone the repo. 
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
at the base directory of the project. 

Then run

```bash
poetry shell
cd 300tang
python3 main.py
```
I use [drop down terminal](https://extensions.gnome.org/extension/442/drop-down-terminal/) to manually start it after boot like this, and just leave that terminal to run it. That way, you don't have to create a .desktop file, have a terminal tab open always, etc. If you would like everything to be handled automatically from boot, keep reading:

# Automating it

If you would like the script to automatically run on the background starting from boot, add a .desktop file like below to /home/your_name/.config/autostart/

```
[Desktop Entry]
Encoding=UTF-8
Name=300Tang
Comment=Random wallpaper generator.
Icon=gnome-info
Exec=gnome-terminal -x bash -c "cd ~/Desktop/300Tang/300tang && python3 main.py exec bash"
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=10

```
 if you placed the project in another directory, modify the Exec=cd .../300Tang/300tang path. If its in your desktop, you can use this one without modifying. Just copy it to /home/your_name/.config/autostart/300Tang.desktop



# TODO
* Make .service file and use systemctl to run script without terminal
* Add more base images
* Add English and Pinyin
