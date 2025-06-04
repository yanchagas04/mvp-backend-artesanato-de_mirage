from pydantic import BaseModel
from datetime import datetime

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    artesao_id: int
    data_cadastro: datetime

    class Config:
        orm_mode = True