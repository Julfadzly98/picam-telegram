import requests
import time
from picamera import PiCamera

# Set up the camera
camera = PiCamera()

# Define the Telegram bot token and chat ID
bot_token = '5731951595:AAHRe31htcyq1e4ma9xfftN12cA1ggnlNDo'
chat_id = '187740907'

# Define the URL for the Telegram API
telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

# Capture an image
camera.capture('/home/pi/image.jpg')  # Save the image to a file

# Prepare the message data
files = {'photo': open('/home/pi/image.jpg', 'rb')}
params = {'chat_id': chat_id}

# Send the message with the image
response = requests.post(telegram_api_url, params=params, files=files)

# Check the response from the API
if response.status_code == 200:
    print("Image sent successfully")
else:
    print(f"Failed to send image. Status code: {response.status_code}")

# Clean up
camera.close()
