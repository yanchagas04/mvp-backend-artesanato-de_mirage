from fastapi import FastAPI
from src.routes.artesao.artesaoRouter import artesaoRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(artesaoRouter)
app.middleware(
    CORSMiddleware(
        app=app,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
)

app.include_router(artesaoRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}
