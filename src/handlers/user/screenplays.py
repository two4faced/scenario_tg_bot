import datetime

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from src.database.database import async_session_maker
from src.lexicon.lexicon_ru import LEXICON_RU
from src.repositories.screenplays import ScreenplaysRepository
from src.schemas.screenplays import AddScreenplayDTO
from src.states.states import FSMScreenplayStates

router = Router()


@router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def cancel_screenplay_command(msg: Message, state: FSMContext):
    await msg.answer(LEXICON_RU["cancel"])
    await state.clear()


@router.message(Command(commands="new_screenplay"), StateFilter(default_state))
async def new_screenplay_command(msg: Message, state: FSMContext):
    await msg.answer(LEXICON_RU["new_screenplay"])
    await state.set_state(FSMScreenplayStates.title)


@router.message(
    StateFilter(FSMScreenplayStates.title), lambda x: x.text and len(x.text) <= 75
)
async def get_title(msg: Message, state: FSMContext):
    await state.update_data(title=msg.text)
    await msg.answer(LEXICON_RU["screenplay_title"])
    await state.set_state(FSMScreenplayStates.logline)


@router.message(StateFilter(FSMScreenplayStates.title))
async def warning_not_title(msg: Message):
    await msg.answer(LEXICON_RU["not_screenplay_title"])


@router.message(
    StateFilter(FSMScreenplayStates.logline), lambda x: x.text and len(x.text) <= 40
)
async def get_logline(msg: Message, state: FSMContext):
    await state.update_data(logline=msg.text)
    data = await state.get_data()

    async with async_session_maker() as session:
        new_screenplay = AddScreenplayDTO(
            title=data["title"],
            logline=data["logline"],
            author_id=msg.from_user.id,
            redacted_at=datetime.datetime.utcnow(),
        )
        await ScreenplaysRepository(session).create(new_screenplay)
        await session.commit()

    await msg.answer(LEXICON_RU["screenplay_logline"])
    await state.clear()


@router.message(StateFilter(FSMScreenplayStates.logline))
async def warning_not_logline(msg: Message):
    await msg.answer(LEXICON_RU["not_screenplay_logline"])
