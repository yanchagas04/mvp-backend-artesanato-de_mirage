from fastapi import APIRouter
from src.controllers.auth.authController import authController
from src.models.artesao.artesaoModel import ArtesaoLogin, ArtesaoCreateUpdate

authRouter = APIRouter(
    prefix='/auth',
    tags=['Auth'],
    responses={
        404: {"description": "Não encontrado"},
        405: {"description": "Metodo nao permitido"},
        500: {"description": "Erro interno"}
    }
)

@authRouter.post('/register', response_model=ArtesaoCreateUpdate, tags=['Auth'], description='Register', operation_id='register', status_code=201)
async def register(data: ArtesaoCreateUpdate): return await authController.register(data)

@authRouter.post('/login', response_model=ArtesaoCreateUpdate, tags=['Auth'], description='Login', operation_id='login', status_code=200)
async def login(data: ArtesaoLogin): return await authController.login(data)