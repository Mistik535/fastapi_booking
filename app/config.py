# from pydantic_settings import BaseSettings


# from pydantic import validator


# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_USER: str
#     DB_PASS: str
#     DB_NAME: str

    # @validator("DATABASE_URL", pre=True, always=True)
    # def assemble_database_url(cls, v, values):
    #     return f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@{values['DB_HOST']}:{values['DB_PORT']}/{v}"
    #
    # class Config:
    #     env_file = ".env"
#
#
# settings = Settings()
