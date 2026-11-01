"""Neste ficheiro convertemos uma Palavra-Passe para SHA-256
e verificamos se os hashes são iguais.

Para isso importamos sha256 da biblioteca hashlib.
"""
from hashlib import sha256


def hash_password(pwd: str) -> str:
    """Devolve o hash SHA-256 de uma Palavra-Passe.

    Parâmetros:
        pwd (str): Palavra-Passe introduzida pelo utilizador.

    Retorno:
        str: hash SHA-256 da Palavra-Passe, em hexadecimal.
    """
    return sha256(pwd.encode()).hexdigest()


def check_password(pwd: str, pwd_hash: str) -> bool:
    """Verifica se uma Palavra-Passe corresponde a um hash.

    Parâmetros:
        pwd (str): Palavra-Passe a verificar.
        pwd_hash (str): hash SHA-256 contra o qual se compara.

    Retorno:
        bool: True se os hashes forem iguais, False caso contrário.
    """
    return hash_password(pwd) == pwd_hash