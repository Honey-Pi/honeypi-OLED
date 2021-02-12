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

def oled_Logo():
    ## HoneyPi Logo an OLED senden
    oled.onoff(1) 
    oled.display()
    oled.cls()
    draw.rectangle((0, 0, 128, 64), outline=1, fill=1)
    draw.bitmap((0, 0), Image.open('HoneyPi_logo.png'), fill=0)
    oled.display()
    time.sleep(1)
    
    ## Versionsnummern auslesen und an OLED senden
    try:
        #oled.cls() # Nach dem Logo wird es drüber geschieben 
        version_file = "/var/www/html/version.txt"
        fp = open(version_file)
        for i, line in enumerate(fp):
            if i >= 1 :
                print(line.split()[-1])
                draw.text((0, 13*i-10), str(line.split()[-1]), fill=1)
                oled.display()
        #print("Anzahl Datensaetze: ", i)
        fp.close()
    except Exception as ex:
        print("Exception in function check_undervoltage:" + str(ex))
        #pass
  