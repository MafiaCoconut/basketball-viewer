from datetime import datetime

from aiogram.types import InputFile, FSInputFile
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.utils.bot import bot
from app.utils.logs import set_func
# from config.log_def import set_func
from app.handlers.parser import Parser
import threading
import logging as log
# from main import bot
import asyncio

tag = "mailing"
scheduler = AsyncIOScheduler()
parser_sqlite = Parser()
# interval = 600  # 10 минут


async def start_scheduler_job():
    function_name = 'start_scheduler_job'
    set_func(function_name, tag)

    # data = parser_sqlite.test_func()
    data = parser_sqlite.start_parser()
    log.info(data)

    if data == "Есть свободные записи":
        photo = FSInputFile(path="data/termins.png")

        # Я
        await bot.send_photo(603789543, photo=photo, caption=data)

        # Андрей
        await bot.send_photo(821755718, photo=photo, caption=data)

    elif data == "Сайт заподозрил DDOS":
        photo = FSInputFile(path="data/ddos_screenshot.png")
        await bot.send_photo(6016855180, photo=photo, caption=data)

    elif data == "Нет свободных записей":
        photo = FSInputFile(path="data/termins.png")
        await bot.send_photo(6016855180, photo=photo, caption=data)


async def set_jobs():
    # threading.Timer(interval, start_scheduler_job).start()
    # asyncio.create_task(async_timer(interval, start_scheduler_job))
    for hour in [i for i in range(24)]:
        for minute in [15, 30, 45, 0]:

            scheduler.add_job(start_scheduler_job, 'cron', hour=hour, minute=minute)
    scheduler.start()

    for job in scheduler.get_jobs():
        print(job)


async def async_timer(interval, callback):
    while True:
        await asyncio.sleep(interval)
        await asyncio.create_task(callback())


async def run_scheduler():
    await start_scheduler_job()

