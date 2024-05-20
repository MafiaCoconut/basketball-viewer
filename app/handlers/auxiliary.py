from datetime import datetime

# from utils.logs import set_func, set_func_and_person
from aiogram.types import CallbackQuery

from app.handlers import config
from app.utils.bot import bot


# from utils.bot import bot


def is_correct_time(data):
    if len(data) == 5 and data[2] in [':', '.', '/', '\\', ',', ';']:
        hour, minute = data[:2], data[3:5]

        if hour.isdigit() and 0 <= int(hour) <= 23 and minute.isdigit() and 0 <= int(minute) <= 59:
            return True
        return False
    return False


def refactor_datetime(time: str):
    colon_index = time.find(':')
    underlining_index = time.find('_')
    whitespace_index = time.find(' ')

    hour = time[colon_index-2:colon_index]
    minute = time[colon_index+1: colon_index+3]
    if underlining_index != -1:
        type_of_mailing = time[underlining_index+1:whitespace_index]
        return f"{hour}:{minute} - {type_of_mailing}"
    else:
        return f"{hour}:{minute}"


async def get_stub(call: CallbackQuery, l10n):
    await call.answer(l10n.format_value('in-development'))
    await call.answer()


# async def send_message_to_admin(message, _reply_markup=None):
#     await bot.send_message(config.get_admin_id(), message, reply_markup=_reply_markup)


def is_weekday():
    weekday = int(datetime.now().isoweekday())
    if 1 <= weekday <= 5:
        return True
    return False
