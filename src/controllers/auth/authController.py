from src.config.config import prisma
from src.models.artesao.artesaoModel import Artesao, ArtesaoLogin
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate
from fastapi import HTTPException
from fastapi import status
from src.utils.utils import gerar_hash, verificar_senha

class authController:

    @staticmethod
    async def login(data: ArtesaoLogin) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.find_unique(where={"email": data.email})
            await prisma.disconnect()
            if not artesao:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
            if not verificar_senha(data.senha, artesao.senha):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
            return artesao
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao logar usuário")
        
    @staticmethod
    async def register(data: ArtesaoCreateUpdate) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.create(data={
                "nome": data.nome,
                "email": data.email,
                "senha": gerar_hash(data.senha)
            })
            await prisma.disconnect()
            return artesao
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao cadastrar usuário")
        
    @staticmethod
    async def update(id: int, data: ArtesaoCreateUpdate) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.update(where={"id": id}, data={
                "nome": data.nome,
                "email": data.email,
                "senha": gerar_hash(data.senha)
            })
            await prisma.disconnect()
            return artesao
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar usuário")
        
    @staticmethod
    async def delete(id: int) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.delete(where={"id": id})
            await prisma.disconnect()
            return artesao
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar usuário")