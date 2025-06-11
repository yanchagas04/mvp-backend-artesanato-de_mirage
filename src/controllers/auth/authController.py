from src.config.config import prisma
from src.models.artesao.artesaoModel import Artesao, ArtesaoLogin
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate
from fastapi import HTTPException
from fastapi import status
from src.utils.utils import gerar_hash, verificar_senha
from prisma.errors import UniqueViolationError

class authController:
        
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
            await prisma.disconnect()
            print(e)
            if (e.__str__() == "Unique constraint failed on the fields: (`email`)"):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ja cadastrado")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao cadastrar usuário")
        
    @staticmethod
    async def login(data: ArtesaoLogin) -> Artesao:
        try:
            await prisma.connect()
            artesao = await prisma.artesao.find_first(where={
                "email": data.email
            })
            await prisma.disconnect()
            if not artesao:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
            if not verificar_senha(data.senha, artesao.senha):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta")
            return {
                "id": artesao.id,
                "nome": artesao.nome,
                "email": artesao.email,
                "dataCadastro": artesao.dataCadastro,
                "senha": artesao.senha
            }
        except Exception as e:
            await prisma.disconnect()
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao logar usuário")