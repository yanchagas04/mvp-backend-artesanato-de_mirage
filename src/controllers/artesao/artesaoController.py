from fastapi import HTTPException, status
from src.config.config import prisma
from typing import List
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate, Artesao

class artesaoController():
    
    @staticmethod
    async def listar() -> List[Artesao]:
        try:
            await prisma.connect()
            artesoes = await prisma.artesao.find_many()
            await prisma.disconnect()
            return artesoes
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao listar usuários")
    
    @staticmethod
    async def buscar(id: int) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.find_unique(where={"id": id})
            await prisma.disconnect()
            return artesao
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao buscar usuário")