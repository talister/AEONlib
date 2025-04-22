from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="AEON_", env_file=".env")

    lco_token: str = ""
    lco_api_root: str = "https://observe.lco.global/api/"


settings = Settings()
