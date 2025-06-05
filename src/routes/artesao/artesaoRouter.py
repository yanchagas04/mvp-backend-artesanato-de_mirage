from fastapi import APIRouter
from src.controllers.artesao.artesaoController import artesaoController
from typing import List
from src.models.artesao.artesaoModel import Artesao, ArtesaoCreateUpdate
from http import HTTPStatus

artesaoRouter = APIRouter(
    prefix='/artesao',
    tags=['Artesao']
)

@artesaoRouter.get('', response_model=List[Artesao], tags=['Artesao'], description='Listar todos os artesaos', operation_id='listar_todos_artesaos', status_code=HTTPStatus.OK)
async def listar_artesaos(): return await artesaoController.listar()

@artesaoRouter.get('/{id}', response_model=Artesao, tags=['Artesao'], description='Buscar um artesao pelo id', operation_id='buscar_artesao', status_code=HTTPStatus.OK)
async def buscar_artesao(id: int): return await artesaoController.buscar(id)
