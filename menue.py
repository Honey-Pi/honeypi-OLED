import smbus
import time
import logging
from oled_data import oled_data_prepare

from logo_onOLED import oled_Logo
from ip_onOLED import oled_network_data
from voltage_onOLED import oled_undervoltage_data
from switchOff_OLED import oled_off
from utilities import reboot

logger = logging.getLogger('HoneyPi.Menue')

from lib_oled96 import ssd1306
from smbus import SMBus
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
bus = smbus.SMBus(1) # Rev 2 Pi
oled = ssd1306(i2cbus)
draw = oled.canvas
from PIL import Image
oled.display()
oled.cls()
entprellVar = 0.3
durchlaufzeit = 0

from PIL import ImageFont, ImageDraw, Image
font = ImageFont.load_default()
#font = ImageFont.truetype('Retron2000.ttf', 9)
#font = ImageFont.truetype('BMSPA___.TTF', 9) 
#font = ImageFont.truetype('8-BIT WONDER.TTF', 6) 


DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
OLATA = 0x14 # Register fuer Ausgabe (GPB)
OLATB = 0x15 # Register fuer Ausgabe (GPB)
GPIOA = 0x12 # Register fuer Eingabe (GPA)
GPIOB = 0x13 # Register fuer Eingabe (GPA) 

# Binaer: 0 bedeutet Output, 1 bedeutet Input
# Definiere GPA Pin 7 als Input (10000000 = 0x80)
# Definiere alle GPA Pins als Output (00000000 = 0x00)
bus.write_byte_data(DEVICE,IODIRA,0x00)

# Setze alle Output bits auf 0
bus.write_byte_data(DEVICE,OLATA,0)
#Kein Output: bus.write_byte_data(DEVICE,OLATB,0)

# Definiere alle GPB als Input (11111111 = 0xFF)
bus.write_byte_data(DEVICE,IODIRB,0xFF)

# view menu
oled_Logo()
time.sleep(3)
        
def menu0_level_0():
    try:
        lcdLine0="Main menu"
        lcdLine1="Measuring"
        lcdLine2="Show CSV"
        lcdLine3="Single beehive"
        lcdLine4="System"
        lcdLine5="Menu 0"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 0-0 " + repr(e))
    # Error occured
    return {} 

def menu0_level_1():
    try:
        lcdLine0="NICHT VORHANDEN"
        lcdLine1="Menu 0-1"
        lcdLine2="Menu 0-2"
        lcdLine3="Menu 0-3"
        lcdLine4="Menu 0-4"
        lcdLine5="Menu 0-5"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        print (">>> menu0_level_1")
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 0-1 " + repr(e))
    # Error occured
    return {} 

def menu1_level_1():
#  "Measuring"
    try:
        lcdLine0="Measuring"
        lcdLine1="Menu 1-1"
        lcdLine2="Menu 1-2"
        lcdLine3="Menu 1-3"
        lcdLine4="Menu 1-4"
        lcdLine5="Menu 1-5"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        print (">>> menu_1")
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 1-1 " + repr(e))
    # Error occured
    return {} 
    
def menu2_level_1():
# "Show CSV"
    try:
        lcdLine0="Show CSV"
        lcdLine1="Show last row from csv"
        lcdLine2="Menu 2-2"
        lcdLine3="Menu 2-3"
        lcdLine4="Menu 2-4"
        lcdLine5="Menu 2-5"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        print (">>> menu_2")
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 2-1 " + repr(e))
    # Error occured
    return {} 

def menu3_level_1():
# "Single beehive"
    try:
        lcdLine0="Single beehive"
        lcdLine1="Menu 3-1"
        lcdLine2="Menu 3-2"
        lcdLine3="Menu 3-3"
        lcdLine4="Menu 3-4"
        lcdLine5="Menu 3-5"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        print (">>> menu_3")        
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 3-1 " + repr(e))
    # Error occured
    return {} 
    
def menu4_level_1():
# "System"
    try:
        lcdLine0="System"
        lcdLine1="Network"
        lcdLine2="Voltage & CPU temp"
        lcdLine3="Version"
        lcdLine4="Reboot Raspberry Pi"
        lcdLine5="Switch off"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        print (">>> menu_4")        
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 4-1 " + repr(e))
    # Error occured
    return {} 
    
def menu5_level_1():
    try:
        lcdLine0="Menu 0"
        lcdLine1="Menu 5-1"
        lcdLine2="Menu 5-2"
        lcdLine3="Menu 5-3"
        lcdLine4="Menu 5-4"
        lcdLine5="Menu 5-5"
        oled.cls()
        draw.text((3, 12), ">", font=font, fill=1)
        draw.text((3, 2), lcdLine0, font=font, fill=1)
        draw.text((10, 12), lcdLine1, font=font, fill=1)
        draw.text((10, 22), lcdLine2, font=font, fill=1)
        draw.text((10, 32), lcdLine3, font=font, fill=1)
        draw.text((10, 42), lcdLine4, font=font, fill=1)
        draw.text((10, 52), lcdLine5, font=font, fill=1)
        oled.display()
        print (">>> menu_5")        
    except Exception as e:
        logger.exception("Unhandled Exception in Menu level 5-1 " + repr(e))
    # Error occured
    return {} 
    
    
menuposition=1
menupositionmin=1
menupositionmax=5 
menupositionold=0

menulevel=0
menulevelmin=0
menulevelmax=3
menulevelold=0

menu0_level_0()    
menu=0
while True:
    try:
        if durchlaufzeit == 0:
            durchlaufzeit = time.time()
            # Status von GPIOA Register auslesen
            rowA = bus.read_byte_data(DEVICE,GPIOA)
            rowB = bus.read_byte_data(DEVICE,GPIOB)
            
            if rowA & 0b00010000 == 0b00010000:
                if menulevel <= menulevelmax:
                    print ("Cursor right  -->") 
                    menulevel=menulevel+1
                    if  menuposition== 0 and menulevel == 1:
                        print ("0-1")
                        menu=0
                    elif menuposition== 1 and menulevel == 1:
                        menu1_level_1()
                        menu=1      
                    elif menuposition== 2 and menulevel == 1:
                        menu2_level_1()
                        menu=2
                    elif menuposition== 3 and menulevel == 1:
                        menu3_level_1()
                        menu=3

                    elif menuposition== 4 and menulevel == 1:
                        menu4_level_1()
                        menu=4

                    elif menuposition== 5 and menulevel == 1:
                        menu5_level_1()
                        menu=5
                    if menulevel < 2:
                        menuposition = 1
            
                    # Level 2 // Programmstart 
                    
                    if menu == 1 and menulevel == 2:
                        # Menu Measuring
                        if menuposition == 0:
                            print ("Starte Programm im 1/2/0")
                          
                        elif menuposition == 1:
                            print ("Starte Programm im 1/2/1")
                            #oled_network_data()

                        elif menuposition == 2:
                            print ("Starte Programm im 1/2/2")
                            #oled_undervoltage_data()

                        elif menuposition == 3:
                            print ("Starte Programm im 1/2/3")
                            #oled_network_data()

                        elif menuposition == 4:
                            print ("Starte Programm im 1/2/4")
                            #oled_undervoltage_data()
                        
                        elif menuposition == 5:
                            print ("Starte Programm im 1/2/5")
                            #oled_undervoltage_data()
                       

                            
                    if menu == 2 and menulevel == 2:                 
                        # Menu Show CSV
                        if menuposition == 0:
                            print ("Starte Programm im 2/2/0")
                            
                        elif menuposition == 1:
                            print ("Starte Programm im 2/2/1")
                            oled_data_prepare()

                        elif menuposition == 2:
                            print ("Starte Programm im 2/2/2")
                            #oled_undervoltage_data()

                        elif menuposition == 3:
                            print ("Starte Programm im 2/2/3")
                            #oled_network_data()

                        elif menuposition == 4:
                            print ("Starte Programm im 2/2/4")
                            #oled_undervoltage_data()
                        
                        elif menuposition == 5:
                            print ("Starte Programm im 2/2/5")
                            #oled_undervoltage_data()

                    if menu == 3 and menulevel == 2:                 
                        # Menu Single beehive
                        if menuposition == 0:
                            print ("Starte Programm im 3/2/0")
                          
                        elif menuposition == 1:
                            print ("Starte Programm im 3/2/1")
                            #oled_network_data()

                        elif menuposition == 2:
                            print ("Starte Programm im 3/2/2")
                            #oled_undervoltage_data()

                        elif menuposition == 3:
                            print ("Starte Programm im 3/2/3")
                            #oled_network_data()

                        elif menuposition == 4:
                            print ("Starte Programm im 3/2/4")
                            #oled_undervoltage_data()
                        
                        elif menuposition == 5:
                            print ("Starte Programm im 3/2/5")
                            #oled_undervoltage_data()                            

                    if menu == 4 and menulevel == 2:                 
                        # Menu System
                        if menuposition == 0:
                            print ("Starte Programm im 4/2/0")
                          
                        elif menuposition == 1:
                            print ("Starte Programm im 4/2/1")
                            oled_network_data()

                        elif menuposition == 2:
                            print ("Starte Programm im 4/2/2")
                            oled_undervoltage_data()

                        elif menuposition == 3:
                            print ("Starte Programm im 4/2/3")
                            oled_Logo()

                        elif menuposition == 4:
                            print ("Starte Programm im 4/2/4")
                            #oled_undervoltage_data()
                            oled.cls()
                            oled_off()
                            reboot()
                            
                        elif menuposition == 5:
                            print ("Starte Programm im 4/2/5")
                            #oled_off                                
                            oled_off()
                            
                    if menu == 5 and menulevel == 2:                 
                        # Menu LEER
                        if menuposition == 0:
                            print ("Starte Programm im 5/2/0")
                          
                        elif menuposition == 1:
                            print ("Starte Programm im 5/2/1")
                            #oled_network_data()

                        elif menuposition == 2:
                            print ("Starte Programm im 5/2/2")
                            #oled_undervoltage_data()

                        elif menuposition == 3:
                            print ("Starte Programm im 5/2/3")
                            #oled_network_data()

                        elif menuposition == 4:
                            print ("Starte Programm im 5/2/4")
                            #oled_undervoltage_data()
                        
                        elif menuposition == 5:
                            print ("Starte Programm im 5/2/5")
                            #oled_undervoltage_data()                          
                            
                    if menulevel > 2:  
                        menulevel=1

                     
            elif rowA & 0b10000000 == 0b10000000:
                oled.onoff(1)
                if menuposition < menupositionmax: 
                    print ("Cursor down")
                    menuposition = menuposition +1
                
            elif rowA & 0b01000000 == 0b01000000:
                oled.onoff(1)
                if menuposition > menupositionmin: 
                    print ("Cursor up")
                    menuposition = menuposition -1    
            
            elif rowA & 0b00100000 == 0b00100000:
                oled.onoff(1)
                if menulevel > 0:
                    print ("<-- Cursor left")
                    menulevel = 0
                    menu=0    
                    menuposition = 1
                    print(menulevel)
                if  menuposition== 1 and menulevel == 0:
                    menu0_level_0()
        
        
            
            print(str(menu) + "/" + str(menuposition)) 
            #else:
            #    print ("No action")
        
        
            
            if menupositionold != menuposition:
                #menu1_level_1()
                menupositionold = menuposition
                
                if menuposition == 0:
                    #draw.text((3, 2), ">", font=font, fill=1)
                    #draw.text((3, 12), ">", font=font, fill=0)
                    #draw.text((3, 22), ">", font=font, fill=0)
                    #draw.text((3, 32), ">", font=font, fill=0)
                    #draw.text((3, 42), ">", font=font, fill=0)
                    #draw.text((3, 52), ">", font=font, fill=0)
                    oled.display()  
                elif menuposition == 1:
                    #draw.text((3, 2), ">", font=font, fill=0)
                    draw.text((3, 12), ">", font=font, fill=1)
                    draw.text((3, 22), ">", font=font, fill=0)
                    draw.text((3, 32), ">", font=font, fill=0)
                    draw.text((3, 42), ">", font=font, fill=0)
                    draw.text((3, 52), ">", font=font, fill=0)            
                    oled.display()              
                elif menuposition == 2:
                    #draw.text((3, 2), ">", font=font, fill=0)
                    draw.text((3, 12), ">", font=font, fill=0)
                    draw.text((3, 22), ">", font=font, fill=1)
                    draw.text((3, 32), ">", font=font, fill=0)
                    draw.text((3, 42), ">", font=font, fill=0)
                    draw.text((3, 52), ">", font=font, fill=0)
                    oled.display()  
                elif menuposition == 3:
                    #draw.text((3, 2), ">", font=font, fill=0)
                    draw.text((3, 12), ">", font=font, fill=0)
                    draw.text((3, 22), ">", font=font, fill=0)
                    draw.text((3, 32), ">", font=font, fill=1)
                    draw.text((3, 42), ">", font=font, fill=0)
                    draw.text((3, 52), ">", font=font, fill=0)
                    oled.display()  
                elif menuposition == 4:
                    #draw.text((3, 2), ">", font=font, fill=0)
                    draw.text((3, 12), ">", font=font, fill=0)
                    draw.text((3, 22), ">", font=font, fill=0)
                    draw.text((3, 32), ">", font=font, fill=0)
                    draw.text((3, 42), ">", font=font, fill=1)
                    draw.text((3, 52), ">", font=font, fill=0)
                    oled.display()  
                elif menuposition == 5:
                    #draw.text((3, 2), ">", font=font, fill=0)
                    draw.text((3, 12), ">", font=font, fill=0)
                    draw.text((3, 22), ">", font=font, fill=0)
                    draw.text((3, 32), ">", font=font, fill=0)
                    draw.text((3, 42), ">", font=font, fill=0)
                    draw.text((3, 52), ">", font=font, fill=1)
                    oled.display()  
                    #print ("Menu up/down") 
                #oled.display()
                
                #print ("menuposition: "+ str(menuposition))         
                #print ("menulevel: "+ str(menulevel))
    
        verstricheneZeit  = (time.time() - durchlaufzeit)
        if verstricheneZeit >= entprellVar:
            durchlaufzeit=0        
    except Exception as ex:
        print("Exception in function Menu:" + str(ex))
        #pass