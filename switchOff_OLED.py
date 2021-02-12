#!/usr/bin/env python3
# This file is part of HoneyPi [honey-pi.de] which is released under Creative Commons License Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0).
# See file LICENSE or go to http://creativecommons.org/licenses/by-nc-sa/3.0/ for full license details.
from utilities import error_log, get_default_gateway_linux, wait_for_internet_connection
import os
import time
import socket
import urllib.request

from lib_oled96 import ssd1306
from smbus import SMBus
i2cbus = SMBus(1)  # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
draw = oled.canvas
from PIL import Image

def oled_off():
    ## OLED aus
    oled.cls()
    draw.text((0, 2), "", fill=1)
    draw.text((0, 12), "", fill=1)
    draw.text((0, 24), "", fill=1)
    draw.text((0, 34), "  good by....", fill=1)
    draw.text((0, 44), "", fill=1)
    draw.text((0, 54), "", fill=1)
    oled.display()
    time.sleep(3)
    oled.onoff(0) 
    