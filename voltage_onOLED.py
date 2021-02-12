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

def oled_undervoltage_data():
    ## HoneyPi Logo an OLED senden
    oled.onoff(1) 
    oled.display()
    oled.cls()

    ## Unterspannubngsnachricht auslesen
    try:
        undervoltage = str(os.popen("sudo vcgencmd get_throttled").readlines())
        error_log("undervoltagecheck")
        print(undervoltage)
    
        if "0x0" in undervoltage:
            error_log("Info: No undervoltage alarm")
            print("Unterspannung 0x0 " + undervoltage)
            lcdLine1= "Undervoltage:" 
            lcdLine2= "          No alarm"
    
        elif "0x50000" in undervoltage:
            error_log("Warning: Undervoltage alarm had happened since system start ", undervoltage)
            print("Undervoltage " + undervoltage)
            lcdLine1= "Undervoltage check: Alarm"
            lcdLine2=  "    Alarm!"
    
        elif "0x50005" in undervoltage:
            error_log("Warning: Undervoltage alarm is currently raised ", undervoltage)
            print("Undervoltage 0x50005 " + undervoltage)
            lcdLine1= "Undervoltage check: Alarm " 
            lcdLine2=  "    Alarm!"
        lcdLine3=""
        lcdLine4=""
        lcdLine5=""
        lcdLine6=""
    except Exception as e:
        print("Exception in function check_undervoltage:" + str(e))
        #pass
    
    ## CPU-Temperatur ermitteln
    fd = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(fd.readline().rstrip())/1000.0
    fd.close()
    lcdLine6 = "CPU T: %.2f" % temp
     
    ## an OLED senden
    oled.cls()
    draw.text((0, 2), lcdLine1, fill=1)
    draw.text((0, 12), lcdLine2, fill=1)
    draw.text((0, 24), lcdLine3, fill=1)
    draw.text((0, 34), lcdLine4, fill=1)
    draw.text((0, 44), lcdLine5, fill=1)
    draw.text((0, 54), lcdLine6, fill=1)
    oled.display()
    #time.sleep(4)
    