from src.models import UsersORM
from src.repositories.base import BaseRepository
from src.schemas.users import UserDTO


class UsersRepository(BaseRepository):
    model = UsersORM
    schema = UserDTO
