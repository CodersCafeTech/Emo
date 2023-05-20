import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration for LCD:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 

disp = LCD_2inch.LCD_2inch()
disp.Init()

frame_count = {'blink':39, 'happy':60, 'sad':47,'dizzy':67,'excited':24,'neutral':61,'happy2':20,'angry':20,'happy3':26,'bootup3':124,'blink2':20,'sleep':112}

def show(emotion):
    try:
        for i in range(frame_count[emotion]):
            image = Image.open('/home/pi/Desktop/EmoBot/emotions/'+emotion+'/frame'+str(i)+'.png')	
            disp.ShowImage(image)
        #disp.module_exit()
        #logging.info("quit:")
    except IOError as e:
        logging.info(e)    
    except KeyboardInterrupt:
        disp.module_exit()
        logging.info("quit:")
        exit()
for i in range(5):
	show('sleep')
