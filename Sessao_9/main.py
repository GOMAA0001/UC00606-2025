"""Programa principal: coordena as funções dos outros ficheiros."""

from hide_IP import mask_ip
from check_email import is_corporate_email
from password import hash_password


def main():
    """Pede password, email e IP ao utilizador e mostra os resultados.

    Mostra o hash SHA-256 da password, se o email é corporativo
    e o IP mascarado. Todas as variáveis são locais.
    """
    # Dados introduzidos pelo utilizador (variáveis locais)
    pwd = input("Password: ")
    email = input("Email: ")
    ip = input("IP: ")

    # Resultados
    print("Hash da password:", hash_password(pwd))
    print("Email corporativo:", is_corporate_email(email))
    print("IP mascarado:", mask_ip(ip))


main()