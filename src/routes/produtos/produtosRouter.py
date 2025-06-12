from http import HTTPStatus
from fastapi import APIRouter
from src.controllers.produto.produtoController import produtoController
from typing import List
from src.models.produto.produtoModel import Produto, ProdutoCreateUpdate

produtoRouter = APIRouter(
    prefix='/produtos',
    tags=['Produto']
)

@produtoRouter.get('/{artesaoId}', response_model=List[Produto], tags=['Produto'], description='Listar todos os produtos', operation_id='listar_todos_produtos', status_code=HTTPStatus.OK)
async def listar_produtos(artesaoId: int): return await produtoController.listar(artesaoId)

@produtoRouter.post('/{artesaoId}', response_model=ProdutoCreateUpdate, tags=['Produto'], description='Adicionar um produto', operation_id='adicionar_produto_artesao', status_code=HTTPStatus.CREATED)
async def adicionar_produto_artesao(artesaoId: int, data: ProdutoCreateUpdate): return await produtoController.adicionarPorArtesao(artesaoId, data)