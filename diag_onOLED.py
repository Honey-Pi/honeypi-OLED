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

def oled_diag_data():
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
    time.sleep(4)
    
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
    
    except Exception as e:
        print("Exception in function check_undervoltage:" + str(e))
        #pass
    
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
    time.sleep(4)
    