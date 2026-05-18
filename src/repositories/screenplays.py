from src.models import ScreenplayORM
from src.repositories.base import BaseRepository
from src.schemas.screenplays import ScreenplayDTO


class ScreenplaysRepository(BaseRepository):
    model = ScreenplayORM
    schema = ScreenplayDTO
