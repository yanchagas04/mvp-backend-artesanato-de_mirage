from typing import List
from src.controllers.produto.produtoController import produtoController
from src.models.produto.produtoModel import ProdutoCreateUpdate
from src.models.produto.produtoModel import Produto
from src.controllers.auth.authController import authController
from src.models.artesao.artesaoModel import Artesao, ArtesaoCreateUpdate, ArtesaoLogin
from src.config.config import prisma
import pytest


