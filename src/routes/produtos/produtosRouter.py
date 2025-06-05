from http import HTTPStatus
from fastapi import APIRouter
from src.controllers.produto.produtoController import produtoController
from typing import List
from src.models.produto.produtoModel import Produto, ProdutoCreateUpdate

produtoRouter = APIRouter(
    prefix='/produtos',
    tags=['Produto']
)

@produtoRouter.get('', response_model=List[Produto], tags=['Produto'], description='Listar todos os produtos', operation_id='listar_todos_produtos', status_code=HTTPStatus.OK)
async def listar_produtos(): return await produtoController.listar()

@produtoRouter.put('/{id}', response_model=ProdutoCreateUpdate, tags=['Produto'], description='Atualizar um produto pelo id', operation_id='atualizar_produto', status_code=HTTPStatus.OK)
async def atualizar_produto(id: int, data: ProdutoCreateUpdate): return await produtoController.atualizar(id, data)

@produtoRouter.delete('/{id}', response_model=Produto, tags=['Produto'], description='Deletar um produto pelo id', operation_id='deletar_produto', status_code=HTTPStatus.OK)
async def deletar_produto(id: int): return await produtoController.deletar(id)

@produtoRouter.get('/{artesaoId}', response_model=List[Produto], tags=['Produto'], description='Listar todos os produtos', operation_id='listar_produtos_artesao', status_code=HTTPStatus.OK)
async def listar_produtos_artesao(artesaoId: int): return await produtoController.listarPorArtesao(artesaoId)

@produtoRouter.post('/{artesaoId}', response_model=ProdutoCreateUpdate, tags=['Produto'], description='Adicionar um produto', operation_id='adicionar_produto_artesao', status_code=HTTPStatus.CREATED)
async def adicionar_produto_artesao(artesaoId: int, data: ProdutoCreateUpdate): return await produtoController.adicionarPorArtesao(artesaoId, data)