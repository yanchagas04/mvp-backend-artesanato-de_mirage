from fastapi import APIRouter
from src.controllers.auth.authController import authController
from src.models.artesao.artesaoModel import ArtesaoLogin, ArtesaoCreateUpdate

authRouter = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@authRouter.post('/register', response_model=ArtesaoCreateUpdate, tags=['Auth'], description='Register', operation_id='register', status_code=201)
async def register(data: ArtesaoCreateUpdate): return await authController.register(data)