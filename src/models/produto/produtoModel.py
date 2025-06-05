from pydantic import BaseModel
from datetime import datetime

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    dataCadastro: datetime
    artesaoId: int

class ProdutoCreateUpdate(BaseModel):
    nome: str
    descricao: str
    preco: float