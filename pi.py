import time
import picamera
import requests
import os

from telegram import Bot

# Replace with your Telegram Bot API token
TELEGRAM_API_TOKEN = 'YOUR_TELEGRAM_API_TOKEN'
# Replace with your chat ID
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

# Initialize the Telegram Bot
bot = Bot(token=TELEGRAM_API_TOKEN)

# Create a function to capture and send the image
def capture_and_send_image():
    try:
        # Initialize the Pi Camera
        with picamera.PiCamera() as camera:
            # Capture an image
            image_path = '/path/to/your/image.jpg'
            camera.capture(image_path)
            
            # Send the image to Telegram
            with open(image_path, 'rb') as image_file:
                bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_file)
                
            # Remove the captured image
            os.remove(image_path)
            
            print("Image sent successfully.")
            
    except Exception as e:
        print("Error:", e)

# Main loop
while True:
    capture_and_send_image()
    time.sleep(10)  # Capture and send an image every 10 seconds
