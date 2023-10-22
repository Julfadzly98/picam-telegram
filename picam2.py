import asyncio
import time
import picamera
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from urllib import request
from time import sleep

# Replace with your Telegram Bot API token
TELEGRAM_API_TOKEN = '5731951595:AAHRe31htcyq1e4ma9xfftN12cA1ggnlNDo'

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
    print("Bot started")

async def on_shutdown(dp):
    print("Bot stopped")
    await bot.close()

async def send_photo():
    try:
        with picamera.PiCamera() as camera:
            image_path = '/home/pi/Desktop/picam/image.jpg'
            camera.capture(image_path)
            
            with open(image_path, 'rb') as image_file:
                await bot.send_photo(chat_id='187740907', photo=image_file, caption='Your image')
                
            os.remove(image_path)
            return True
    except Exception as e:
        print("Error:", e)
        return False

if __name__ == '__main__':
    dp.loop.create_task(on_startup(dp))
    dp.loop.create_task(on_shutdown(dp))

    while True:
        success = asyncio.run(send_photo())
        if success:
            result = "Yes"

            #https://docs.google.com/forms/d/e/1FAIpQLSf1fiB4uWz5OsGLJVIpPi36h7paUG2kRBad-Pdm_CCZdAL0ZQ/viewform?usp=pp_url&entry.1472446157={}&submit=Submit
            form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf1fiB4uWz5OsGLJVIpPi36h7paUG2kRBad-Pdm_CCZdAL0ZQ/formResponse?usp=pp_url&entry.1472446157={}&submit=Submit".format(result)
	          request.urlopen(form_url)
	          print("done")
        else:
            result = "No"
        print(f"Image sent successfully? {result}")
        time.sleep(10)
