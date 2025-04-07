import os
import subprocess
import telebot

# چک کردن اینکه آیا telebot نصب شده است یا خیر
try:
    import telebot
except ImportError:
    print("کتابخانه telebot نصب نیست. در حال نصب...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])

# توکن ربات خود را وارد کنید
TOKEN = 'توکن_ربات_خودتان'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات من خوش آمدید.")

# شروع ربات
bot.polling()
