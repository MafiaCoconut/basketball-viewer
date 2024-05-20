from aiogram import Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
