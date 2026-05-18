from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from src.database.database import async_session_maker
from src.lexicon.lexicon_ru import LEXICON_RU
from src.repositories.users import UsersRepository
from src.schemas.users import UserDTO

router = Router()


@router.message(CommandStart())
async def start_command(msg: Message):
    await msg.answer(LEXICON_RU["start"])

    async with async_session_maker() as session:
        if not await UsersRepository(session).get_one_or_none(id=msg.from_user.id):
            new_user = UserDTO(id=msg.from_user.id)
            await UsersRepository(session).create(new_user)
            await session.commit()


@router.message(Command(commands="help"))
async def help_command(msg: Message):
    await msg.answer(LEXICON_RU["help"])
