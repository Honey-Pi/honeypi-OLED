#!/usr/bin/env python
# This file is part of HoneyPi [honey-pi.de] which is released under Creative Commons License Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0).
# See file LICENSE or go to http://creativecommons.org/licenses/by-nc-sa/3.0/ for full license details.

import time
from datetime import datetime

###### Später prüfen: ######
import csv  # Kann raus?
import os, sys # Kann raus?
import io # Kann raus?
from utilities import scriptsFolder, check_file, error_log, clean_fields # Prüfen: Kann raus?
###########################
from lib_oled96 import ssd1306
from smbus import SMBus
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
draw = oled.canvas
from PIL import Image
oled.display()
####### Testdatensatz #######
ChannelId="x"
lcdValue1="123.45"
lcdValue2="1,1"
lcdValue3="1000"
lcdValue4="150,66"
lcdValue5="19,55"
lcdValue6="50"
lcdValue7="999"
lcdValue8="11,5"
lcdDate="14.12"
lcdTime="09:33"


def view_singlechannel(ChannelId, lcdTime, lcdDate, lcdValue1, lcdValue2, lcdValue3, lcdValue4, lcdValue5, lcdValue6, lcdValue7, lcdValue8):
    try:
        oled.onoff(1) 
        oled.cls()
        draw.rectangle((0, 0, 128, 64), outline=1, fill=1)
        draw.bitmap((0, 0), Image.open('HoneyPi_logo.png'), fill=0)
        oled.display()
        time.sleep(2)
        for (Id) in ChannelId:
            lcdLine1="Cn:" + ChannelId + " | " + lcdValue1.rjust(6) + "|" + lcdValue2.rjust(6)
            lcdLine2="     | " + lcdValue3.rjust(6) + "|" + lcdValue4.rjust(6)
            lcdLine3=lcdTime.rjust(5) + "| " + lcdValue5.rjust(6) + "|" + lcdValue6.rjust(6)
            lcdLine4=lcdDate.rjust(5) + "| " + lcdValue7.rjust(6) + "|" + lcdValue8.rjust(6)
            oled.cls()
            #mylcd.lcd_clear()
            draw.text((0, 2), lcdLine1, fill=1)
            draw.text((0, 12), lcdLine2, fill=1)
            draw.text((0, 22), lcdLine3, fill=1)
            draw.text((0, 32), lcdLine4, fill=1)
            oled.display()
            time.sleep(5)
            oled.onoff(0)   # kill the oled.  RAM contents still there.
            #error_log("Info: A dataset was successfully sent to the LCD")
        return Id
        
    except IOError as ex1:
        error_log(ex1, "View-LCD IOError")
    except Exception as ex:
        error_log(ex, "View-LCD Exception")
    return False
