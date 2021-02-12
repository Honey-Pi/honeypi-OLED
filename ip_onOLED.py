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

def oled_network_data():
    ## IP auslesen
    def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # muss nicht unbedingt erreichbar sein
            s.connect(('10.255.255.255', 0))
            IP = s.getsockname()[0]
            #DefNRoute?= s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
        
    lcdLine3="IP is:" + str(get_ip())
    
    ## Gateway auslesen
    lcdLine4="Gateway:" + str(get_default_gateway_linux())
    
    ## Internetverbindung zu http://www.msftncsi.com/ncsi.txt prüfen
    def check_internet_connection():
        try:
            #response = str(urllib.request.urlopen('http://www.msftncsi.com/ncsi.txt', timeout=1).read())
            response = str(urllib.request.urlopen('http://www.msftncsi.com/ncsi.txt', timeout=1).read().decode('utf-8'))
            if response == "Microsoft NCSI":
                #print (response)
                #print (type(response))
                #if response == "b'Microsoft NCSI'":
                #if "Microsoft NCSI" in str(response):
                print("Success: Connection established after " + str(i) + " seconds.")
                return True
            #else:
            #    return False
        except:
            print("Except: Connection ")
        return False
    
    lcdLine5="I-Connected: " + str(check_internet_connection())
   
    
    ## an OLED senden
    oled.cls()
    draw.text((0, 2), "", fill=1)
    draw.text((0, 12), "", fill=1)
    draw.text((0, 24), lcdLine3, fill=1)
    draw.text((0, 34), lcdLine4, fill=1)
    draw.text((0, 44), lcdLine5, fill=1)
    draw.text((0, 54), "", fill=1)
    oled.display()
    time.sleep(4)
    