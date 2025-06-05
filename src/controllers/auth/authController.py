from src.config.config import prisma
from src.models.artesao.artesaoModel import Artesao, ArtesaoLogin
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate
from fastapi import HTTPException
from fastapi import status

class authController:

    @staticmethod
    async def login(data: ArtesaoLogin) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.find_unique(where={"email": data.email})
            await prisma.disconnect()
            if not artesao:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
            if data.senha != artesao.senha:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
            return artesao
        except Exception as e:
            raise e
        
    @staticmethod
    async def register(data: ArtesaoCreateUpdate) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.create(data={
                "nome": data.nome,
                "email": data.email,
                "senha": data.senha
            })
            await prisma.disconnect()
            return artesao
        except Exception as e:
            if e.code == "P2002":
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado")
            raise e
        
    @staticmethod
    async def update(id: int, data: ArtesaoCreateUpdate) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.update(where={"id": id}, data={
                "nome": data.nome,
                "email": data.email,
                "senha": data.senha
            })
            await prisma.disconnect()
            return artesao
        except Exception as e:
            if e.code == "P2002":
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado")
            raise e
        
    @staticmethod
    async def delete(id: int) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.delete(where={"id": id})
            await prisma.disconnect()
            return artesao
        except Exception as e:
            raise e