from pydantic import BaseModel
from datetime import datetime

class Artesao(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    dataCadastro: datetime

class ArtesaoCreateUpdate(BaseModel):
    nome: str
    email: str
    senha: str

class ArtesaoLogin(BaseModel):
    email: str
    senha: str