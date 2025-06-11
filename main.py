from fastapi import FastAPI
from src.routes.produtos.produtosRouter import produtoRouter
from src.routes.auth.authRouter import authRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(produtoRouter)
app.include_router(authRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}
