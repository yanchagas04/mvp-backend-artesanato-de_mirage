from fastapi import APIRouter
from src.controllers.auth.authController import authController
from src.models.artesao.artesaoModel import ArtesaoLogin, ArtesaoCreateUpdate

authRouter = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@authRouter.post('/login', response_model=ArtesaoLogin, tags=['Auth'], description='Login', operation_id='login', status_code=200)
async def login(data: ArtesaoLogin): return await authController.login(data)

@authRouter.post('/register', response_model=ArtesaoCreateUpdate, tags=['Auth'], description='Register', operation_id='register', status_code=201)
async def register(data: ArtesaoCreateUpdate): return await authController.register(data)

@authRouter.put('/{id}', response_model=ArtesaoCreateUpdate, tags=['Auth'], description='Update', operation_id='update', status_code=200)
async def update(id: int, data: ArtesaoCreateUpdate): return await authController.update(id, data)

@authRouter.delete('/{id}', response_model=ArtesaoCreateUpdate, tags=['Auth'], description='Delete', operation_id='delete', status_code=200)
async def delete(id: int): return await authController.delete(id)