from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from src.lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def start_command(msg: Message):
    await msg.answer(LEXICON_RU["start"])


@router.message(Command(commands="help"))
async def help_command(msg: Message):
    await msg.answer(LEXICON_RU["help"])


@router.message(Command(commands="new_screenplay"))
async def new_screenplay_command(msg: Message):
    await msg.answer(LEXICON_RU["new_screenplay"])
