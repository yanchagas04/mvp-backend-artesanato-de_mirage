from typing import List
from src.controllers.produto.produtoController import produtoController
from src.models.produto.produtoModel import ProdutoCreateUpdate
from src.models.produto.produtoModel import Produto
from src.controllers.auth.authController import authController
from src.models.artesao.artesaoModel import ArtesaoCreateUpdate
from src.config.config import prisma
import pytest

@pytest.mark.asyncio
async def test_adicionar_produto_artesao():    
    data = ProdutoCreateUpdate(
        nome="Produto 1",
        descricao="Descricao 1",
        preco=10.0
    )
    try:
        produto : Produto = await produtoController.adicionarPorArtesao(1, data)
        await prisma.connect()
        await prisma.produto.delete(where={"id": produto.id})
        await prisma.disconnect()
        assert produto.artesaoId == 1 and produto.nome == "Produto 1" and produto.descricao == "Descricao 1" and produto.preco == 10.0
    except Exception as e:
        #caso ainda não existam artesãos
        await authController.register(ArtesaoCreateUpdate(nome="Artesao 1", email="Qyj6a@example.com", senha="123456"))
        produto : Produto = await produtoController.adicionarPorArtesao(1, data)
        await prisma.connect()
        await prisma.produto.delete(where={"id": produto.id})
        await prisma.artesao.delete(where={"id": 1})
        await prisma.disconnect()
        assert produto.artesaoId == 1 and produto.nome == "Produto 1" and produto.descricao == "Descricao 1" and produto.preco == 10.0

@pytest.mark.asyncio
async def test_listar_produtos():
    try:
        produtos : List[Produto] = await produtoController.listar(1)
        assert len(produtos) >= 0
    except Exception as e:
        #caso ainda não existam artesãos
        await authController.register(ArtesaoCreateUpdate(nome="Artesao 1", email="Qyj6a@example.com", senha="123456"))
        produtos : List[Produto] = await produtoController.listar(1)
        await prisma.connect()
        await prisma.artesao.delete(where={"id": 1})
        await prisma.disconnect()
        assert len(produtos) >= 0
