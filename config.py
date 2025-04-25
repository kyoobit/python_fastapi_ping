import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_DOMAIN: str = "localhost"
    API_IPADDRESS: str = "127.0.0.1"
    API_PORT: int = 8000
    LOG_LEVEL: str = "WARNING"
    RELOAD: bool = False

    @property
    def log_level(self):
        return logging.getLevelName(self.LOG_LEVEL.upper())

    # class ConfigDict: <--- not picking up LOG_LEVEL, why?
    # https://docs.pydantic.dev/2.11/api/config/#pydantic.config.ConfigDict
    # https://docs.pydantic.dev/2.11/migration/#changes-to-config
    class Config:
        env_file = ".env"
        # env_prefix = "MYAPP_"  # Use a prefix to avoid namespace collisions


settings = Settings()
