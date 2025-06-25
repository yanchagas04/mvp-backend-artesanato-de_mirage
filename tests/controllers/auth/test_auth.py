from src.controllers.auth.authController import authController
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate
from src.models.artesao.artesaoModel import ArtesaoLogin
from src.models.artesao.artesaoModel import Artesao
from src.config.config import prisma
import pytest

@pytest.mark.asyncio
async def test_register():
    data = ArtesaoCreateUpdate(
        nome="Artesao 1",
        email="testandoregistro@teste.com",
        senha="123456"
    )
    artesao : Artesao = await authController.register(data)
    await prisma.connect()
    await prisma.artesao.delete(where={"id": artesao.id})
    await prisma.disconnect()
    assert artesao.nome == "Artesao 1" and artesao.email == "testandoregistro@teste.com"

@pytest.mark.asyncio
async def test_login():
    data = ArtesaoCreateUpdate(
        nome="Artesao 1",
        email="testandologin@teste2.com",
        senha="123456"
    )
    a = await authController.register(data)
    data2 = ArtesaoLogin(
        email="testandologin@teste2.com",
        senha="123456"
    )
    artesao : Artesao = await authController.login(data2)
    print(artesao)
    await prisma.connect()
    await prisma.artesao.delete(where={"id": artesao['id']})
    await prisma.disconnect()
    assert artesao['email'] == "testandologin@teste2.com"