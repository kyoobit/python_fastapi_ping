from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_DOMAIN: str = "localhost"
    API_IPADDRESS: str = "0.0.0.0"
    API_PORT: int = 8000
    LOG_LEVEL: str = "WARNING"
    RELOAD: bool = False

    class ConfigDict:
        env_file = ".env"
        # env_prefix = "MYAPP_"  # Use a prefix to avoid namespace collisions


settings = Settings()
