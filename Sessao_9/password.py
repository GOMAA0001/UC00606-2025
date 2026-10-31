"""
    Neste ficheiro python vamos converte uma Palavra-Passe para SHA-256 e verificar se a os hash sao iguais

    Para isso vamos importar sha256 na livraria hashlib
"""
from hashlib import sha256

"""
    A funçao hash_password

    Parametros:
        pwd (str): Palavra-Passe introduzida pelo utilizador.

    Retorno:
        Retorna o hash da Palavra-Passe.
"""
def hash_password (pwd: str) -> str:
    return sha256(pwd.encode()).hexdigest()

"""
    A funçao check_password
    
    Parametros:
        pwd (str): Palavra-Passe
        pwd_hash (str): O hash da Palavra-Passe introduzida anteritormente pelo utilizador.

    Retorno:
        Retorna True se os hashs forem iguais, e False se nao forem.
"""
def check_password(pwd:str, pwd_hash:str) -> bool:
    return sha256(pwd.encode()).hexdigest() == pwd_hash