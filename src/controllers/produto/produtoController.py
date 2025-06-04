from pydantic import BaseModel
from src.config.prisma.prismaClient import client as prisma
from src.models.produto.produtoModel import ProdutoCreateUpdate, Produto

class produtoController:

    async def adicionar(self, data: ProdutoCreateUpdate) -> Produto:
        try:
            produto = await prisma.produto.create(data=data)
            return produto
        except Exception as e:
            raise e
    
    async def atualizar(self, id: int, data: ProdutoCreateUpdate) -> Produto:
        try:
            produto = await prisma.produto.update(where={"id": id}, data=data)
            return produto
        except Exception as e:
            raise e
        
    async def deletar(self, id: int) -> Produto:
        try:
            produto = await prisma.produto.delete(where={"id": id})
            return produto
        except Exception as e:
            raise e
        
    async def listar(self) -> list[Produto]:
        try:
            produtos = await prisma.produto.find_many()
            return produtos
        except Exception as e:
            raise e
        
    async def buscar(self, id: int) -> Produto:
        try:
            produto = await prisma.produto.find_unique(where={"id": id})
            return produto
        except Exception as e:
            raise e
        
    async def buscarPorArtesao(self, id: int) -> list[Produto]:
        try:
            produtos = await prisma.produto.find_many(where={"artesao_id": id})
            return produtos
        except Exception as e:
            raise e