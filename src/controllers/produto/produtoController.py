from fastapi import HTTPException, status
from src.config.config import prisma
from src.models.produto.produtoModel import ProdutoCreateUpdate, Produto
from typing import List

class produtoController:

    @staticmethod
    async def adicionarPorArtesao(artesaoId: int,data: ProdutoCreateUpdate) -> Produto:
        try:
            await prisma.connect()
            produto = await prisma.produto.create(
                data={
                    "nome": data.nome,
                    "descricao": data.descricao,
                    "preco": data.preco,
                    "artesaoId": artesaoId
                }
            )
            await prisma.disconnect()
            return produto
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao cadastrar usuário")
    
    @staticmethod
    async def atualizar(id: int, data: ProdutoCreateUpdate) -> Produto:
        try:
            await prisma.connect()
            produto = await prisma.produto.update(where={"id": id}, data={
                "nome": data.nome,
                "descricao": data.descricao,
                "preco": data.preco
            })
            await prisma.disconnect()
            return produto
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar usuário")
        
    @staticmethod
    async def deletar(id: int) -> Produto:
        try:
            await prisma.connect()
            produto = await prisma.produto.delete(where={"id": id})
            await prisma.disconnect()
            return produto
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar usuário")
        
    @staticmethod
    async def listar() -> List[Produto]:
        try:
            await prisma.connect()
            produtos = await prisma.produto.find_many()
            await prisma.disconnect()
            return produtos
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao listar usuários")
    
    @staticmethod
    async def listarPorArtesao(id: int) -> List[Produto]:
        try:
            await prisma.connect()
            produtos = await prisma.produto.find_many(where={"artesaoId": id})
            await prisma.disconnect()
            return produtos
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao listar usuários")