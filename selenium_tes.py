# https://github.com/openatx/atx-agent/releases

import pyautogui as pag
from time import sleep
import os

os.system('adb push atx-agent /data/local/tmp')
os.system('adb shell chmod 755 /data/local/tmp/atx-agent')
os.system('adb shell /data/local/tmp/atx-agent server -d')
