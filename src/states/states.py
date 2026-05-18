from aiogram.fsm.state import StatesGroup, State


class FSMScreenplayStates(StatesGroup):
    title = State()
    logline = State()
