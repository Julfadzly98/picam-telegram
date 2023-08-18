## pip install picamera python-telegram-bot


sudo nano /etc/systemd/system/picamera_bot.service


[Unit]
Description=PiCamera Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your/script.py
WorkingDirectory=/path/to/your/script/directory
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target


sudo systemctl enable picamera_bot.service
sudo systemctl start picamera_bot.service

sudo reboot


#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/bbt
sudo python bbt.py
cd /
