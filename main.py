import os
import asyncio
import picamera
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Replace with your Telegram Bot API token
TELEGRAM_API_TOKEN = '5642615236:AAG6x-p2z1Q-nj9anic2N3GTM_gDR3D7Pno'
# Replace with your chat ID
TELEGRAM_CHAT_ID = '187740907'

# Initialize the Telegram Bot
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Create a function to capture and send the image
async def capture_and_send_image():
    try:
        # Initialize the Pi Camera
        with picamera.PiCamera() as camera:
            # Capture an image
            image_path = '/home/pi/Desktop/image.jpg'
            camera.capture(image_path)
            
            # Send the image to Telegram
            with open(image_path, 'rb') as image_file:
                await bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=image_file)
                
            # Remove the captured image
            os.remove(image_path)
            
            print("Image sent successfully.")
            
    except Exception as e:
        print("Error:", e)

# Handler for /start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Welcome! I'm capturing and sending images every 10 seconds.")

# Main loop
async def main():
    while True:
        await capture_and_send_image()
        await asyncio.sleep(10)  # Capture and send an image every 10 seconds

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
