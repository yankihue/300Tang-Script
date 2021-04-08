# 300Tang-Script
This is a python script that I use on my desktop. It randomly picks one of the famous [320 Tang poems](https://en.wikipedia.org/wiki/Tang_poetry) and displays it on top of a painting. 
I used [this resource](https://github.com/xuchunyang/300) to get all 320 poems in JSON format. A new wallpaper will be generated overriding the old one every minute (by default).

![Screenshot](/screenshot.png)

# Usage
For Ubuntu:

You need the [WQY Microhei](https://github.com/anthonyfok/fonts-wqy-microhei) font for this to work. To install:

```bash
sudo apt-get install ttf-wqy-microhei 
```
Afterwards, if you want to test the script first, run
```bash
poetry install
```
at the base directory of the project. Then run

```bash
poetry shell
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
