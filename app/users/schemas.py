from pydantic import BaseModel


class SUserRegister(BaseModel):
    email: str
    password: str


