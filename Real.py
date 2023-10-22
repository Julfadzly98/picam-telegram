import requests
import time
from picamera import PiCamera
from urllib import request
from time import sleep

# Set up the camera
camera = PiCamera()

# Define the Telegram bot token and chat ID
bot_token = '5731951595:AAHRe31htcyq1e4ma9xfftN12cA1ggnlNDo'
chat_id = '187740907'

#6613591889:AAHs4CLWbRMXmr5c3Xs0oO7WOqv-biXxyIc
#6398307452

# Define the URL for the Telegram API
telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

# Initialize a variable to keep track of success
image_sent_successfully = False

# Infinite loop to send images every 10 seconds
while True:
    try:
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
            image_sent_successfully = True
        else:
            print(f"Failed to send image. Status code: {response.status_code}")
            image_sent_successfully = False
    except Exception as e:
        print(f"Error: {e}")
        image_sent_successfully = False

    # Check if image was sent successfully
    if image_sent_successfully:
        # Do something when image was sent successfully, e.g., assign as Yes
        result = "Yes"
        #https://docs.google.com/forms/d/e/1FAIpQLSf1fiB4uWz5OsGLJVIpPi36h7paUG2kRBad-Pdm_CCZdAL0ZQ/formResponse?usp=pp_url&entry.1472446157={}
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf1fiB4uWz5OsGLJVIpPi36h7paUG2kRBad-Pdm_CCZdAL0ZQ/formResponse?usp=pp_url&entry.1472446157={}&submit=submit".format(result)
        request.urlopen(form_url)
        print("done")
    else:
        # Do something when image was not sent successfully, e.g., assign as No
        result = "No"

    # Reset the variable for the next iteration
    image_sent_successfully = False

    # Wait for 10 seconds before capturing the next image
    time.sleep(10)

# Clean up (this code will never be reached in this loop)
camera.close()
