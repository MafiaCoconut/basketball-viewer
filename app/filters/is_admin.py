from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
import os

load_dotenv()


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return str(message.chat.id) in str(os.getenv("ADMINS_ID")).split(',')


class IsAdminCallback(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return str(call.message.chat.id) in str(os.getenv("ADMINS_ID")).split(',')

