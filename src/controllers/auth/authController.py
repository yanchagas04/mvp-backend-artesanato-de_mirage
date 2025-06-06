from src.config.config import prisma
from src.models.artesao.artesaoModel import Artesao, ArtesaoLogin
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate
from fastapi import HTTPException
from fastapi import status
from src.utils.utils import gerar_hash, verificar_senha

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
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao cadastrar usuário")