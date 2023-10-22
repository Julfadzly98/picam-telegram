#pip install picamera python-telegram-bot

from urllib import request
import time
import picamera
import requests
import os
from time import sleep

from telegram import Bot

# Replace with your Telegram Bot API token and chat ID
TELEGRAM_API_TOKEN = '5642615236:AAG6x-p2z1Q-nj9anic2N3GTM_gDR3D7Pno'
TELEGRAM_CHAT_ID = '187740907'

#'5642615236:AAG6x-p2z1Q-nj9anic2N3GTM_gDR3D7Pno'
#'187740907'

bot = Bot(token=TELEGRAM_API_TOKEN)

def capture_and_send_image():
    success = False
    
    try:
        with picamera.PiCamera() as camera:
            image_path = '/path/to/your/image.jpg'
            camera.capture(image_path)
            
            with open(image_path, 'rb') as image_file:
                bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_file)
                
            os.remove(image_path)
            
            success = True
            
    except Exception as e:
        print("Error:", e)
    
    return success

while True:
    success = capture_and_send_image()
    if success:
        result = "Yes"
    else:
        result = "No"
    print(f"Image sent successfully? {result}")
    time.sleep(10)

