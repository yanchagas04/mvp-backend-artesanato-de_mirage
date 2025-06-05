from fastapi import APIRouter
from src.controllers.artesao.artesaoController import artesaoController
from typing import List
from src.models.artesao.artesaoModel import Artesao

artesaoRouter = APIRouter(
    prefix='/artesao',
    tags=['Artesao']
)

@artesaoRouter.get('', response_model=List[Artesao], tags=['Artesao'], description='Listar todos os artesaos', status_code=200)
async def listar(): return await artesaoController.listar()

@artesaoRouter.get('/{id}', response_model=Artesao, tags=['Artesao'], description='Buscar um artesao pelo id', status_code=200)
async def buscar(id: int): return await artesaoController.buscar(id)

@artesaoRouter.post('', response_model=Artesao, tags=['Artesao'], description='Adicionar um artesao', status_code=201)
async def adicionar(data: Artesao): return await artesaoController.adicionar(data)

@artesaoRouter.put('/{id}', response_model=Artesao, tags=['Artesao'], description='Atualizar um artesao pelo id', status_code=200)
async def atualizar(id: int, data: Artesao): return await artesaoController.atualizar(id, data)

@artesaoRouter.delete('/{id}', response_model=Artesao, tags=['Artesao'], description='Deletar um artesao pelo id', status_code=200)
async def deletar(id: int): return await artesaoController.deletar(id)
