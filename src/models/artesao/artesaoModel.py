from pydantic import BaseModel
from datetime import datetime

class Artesao(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    data_cadastro: datetime

    class Config:
        orm_mode = True

class ArtesaoCreateUpdate(BaseModel):
    nome: str
    email: str
    senha: str

class ArtesaoLogin(BaseModel):
    email: str
    senha: str