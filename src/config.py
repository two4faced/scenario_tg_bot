from dataclasses import dataclass

from environs import Env


@dataclass
class DBConfig:
    name: str
    host: str
    port: int
    user: str
    password: str

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


@dataclass
class LogConfig:
    level: str
    format: str


@dataclass
class TgBotConfig:
    token: str


@dataclass
class Config:
    bot: TgBotConfig
    database: DBConfig
    log: LogConfig


env: Env = Env()
env.read_env()

settings = Config(
    bot=TgBotConfig(token=env("BOT_TOKEN")),
    database=DBConfig(
        name=env("DB_NAME"),
        host=env("DB_HOST"),
        port=env("DB_PORT"),
        user=env("DB_USER"),
        password=env("DB_PASS"),
    ),
    log=LogConfig(level=env("LOG_LEVEL"), format=env("LOG_FORMAT")),
)
