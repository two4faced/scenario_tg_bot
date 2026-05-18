import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from handlers.base import router as base_router
from handlers.user.screenplays import router as screenplay_router
from src.keyboards.set_menu import set_main_menu


async def main():
    logging.basicConfig(level=settings.log.level, format=settings.log.format)

    storage = MemoryStorage()

    bot = Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=storage)

    await set_main_menu(bot)

    dp.include_router(base_router)
    dp.include_router(screenplay_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
