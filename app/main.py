import asyncio
import logging
#
from app.handlers import mailing
from utils import commands, registration_dispatcher
from utils.bot import bot
from utils.logs import logs_settings, system_logger


async def main() -> None:
    system_logger.info("Starting the bot...")
    print(0)
    registration_dispatcher.register_all_in_dispatcher()
    system_logger.info("Dispatcher registered.")

    await commands.set_commands(bot)
    system_logger.info("Commands set.")
    print(1)
    await mailing.set_jobs()
    system_logger.info("Mailing jobs set.")

    await registration_dispatcher.dp.start_polling(bot)
    system_logger.info("Polling started.")
    print(2)
if __name__ == "__main__":
    logs_settings()
    logging.info("Main script started.")
    asyncio.run(main())