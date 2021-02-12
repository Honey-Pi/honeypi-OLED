#!/usr/bin/env python3
# This file is part of HoneyPi [honey-pi.de] which is released under Creative Commons License Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0).
# See file LICENSE or go to http://creativecommons.org/licenses/by-nc-sa/3.0/ for full license details.
# Changelog 05.12.2020:
#
# Struktur:
#   Daten sammeln / auslesen
#   Aufbereitung der Daten --> Länge begrenzen, ggf.Ganzzahl:
#   Daten übergeben an view_*.py

import time 
import diag_onOLED
import csv
from utilities import scriptsFolder, check_file, error_log, clean_fields # Prüfen: Kann raus?
from view_OLED096_10 import view_singlechannel
import os, sys
import io

############# TEST LCD #############
# *.pyc verhindern
sys.dont_write_bytecode = True

print(time.strftime("%d.%m %H:%M"))
debug = "false"


lcdValue1="1"
reader=""
from read_settings import get_settings, get_sensors
settings = get_settings()
ts_channels = settings["ts_channels"] # ThingSpeak data (ts_channel_id, ts_write_key)
#csv_file = scriptsFolder + "/offline-"  + + "1243952.csv"

def oled_data_prepare():
    for (channelIndex, channel) in enumerate(ts_channels, 1):
        try:
            error_log("Info: Start script: sent to the LCD")
            csv_file = scriptsFolder + '/offline-' + str(channel['ts_channel_id']) + '.csv'
            #filename = scriptsFolder + "/offline-"
            fp = open(csv_file)
            for i, line in enumerate(fp):
                pass
            print("Anzahl Datensaetze: ", i)
            print(line)
            
            reader = line.split(",")
            fp.close()
            #time.sleep(0.5)
            lcdTime = str(reader[0])[11:16]
            lcdDate = str(reader[0])[5:10]
            lcdValue1 = str(reader[1])
            lcdValue2 = str(reader[2])
            lcdValue3 = str(reader[3])
            lcdValue4 = str(reader[4])
            lcdValue5 = str(reader[5])
            lcdValue6 = str(reader[6])
            lcdValue7 = str(reader[7])
            lcdValue8 = str(reader[8])
            t = view_singlechannel(str(channelIndex), lcdTime, lcdDate, lcdValue1, lcdValue2, lcdValue3, lcdValue4, lcdValue5, lcdValue6, lcdValue7, lcdValue8)
            if t and debug:
                error_log("Info: Dataset was successfully sent to the OLED" , i)
        except Exception as ext:
            error_log(ext, "Exception in oled_data.py")
