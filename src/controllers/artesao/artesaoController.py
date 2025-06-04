from pydantic import BaseModel
from src.config.prisma.prismaClient import client as prisma

from src.models.artesao.artesaoModel import ArtesaoCreateUpdate, Artesao

class artesaoController( BaseModel ):

    async def adicionar(self, data: ArtesaoCreateUpdate) -> Artesao:
        try:
            artesao = await prisma.artesao.create(data=data)
            return artesao
        except Exception as e:
            raise e
        
    async def listar(self) -> list[Artesao]:
        try:
            artesoes = await prisma.artesao.find_many()
            return artesoes
        except Exception as e:
            raise e
        
    async def buscar(self, id: int) -> Artesao:
        try:
            artesao = await prisma.artesao.find_unique(where={"id": id})
            return artesao
        except Exception as e:
            raise e
        
    async def atualizar(self, id: int, data: ArtesaoCreateUpdate) -> Artesao:
        try:
            artesao = await prisma.artesao.update(where={"id": id}, data=data)
            return artesao
        except Exception as e:
            raise e
        
    async def deletar(self, id: int) -> Artesao:
        try:
            artesao = await prisma.artesao.delete(where={"id": id})
            return artesao
        except Exception as e:
            raise e