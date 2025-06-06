from passlib.hash import pbkdf2_sha256

# Gerar hash
def gerar_hash(senha) -> str:
    return pbkdf2_sha256.hash(senha)

# Verificar senha
def verificar_senha(senha, hash) -> bool:
    return pbkdf2_sha256.verify(senha, hash)
