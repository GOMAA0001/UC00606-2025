"""
Main Rule: No global variabels
Neste ficheiro python vamos ler, verificar, converte para SHA-256
"""
from hashlib import sha256
import time

def convert_to_SHA256 (_text) -> str:
    return sha256(_text.encode()).hexdigest()

def checks(_text) -> bool:
    return len(_text) >= 8 and any(ch.isdigit() for ch in _text) and any(ch.islower() for ch in _text) and any(ch.isupper() for ch in _text) and any(not ch.isalnum() for ch in _text)

def get_password() -> str:
    print("Escreva uma Palavra-Passe. \n" \
    "Com no minimo de 8 caracteres \n" \
    "Com letras maiusculas e minusculas \n" \
    "E com pelo menos um caracter especial \n")
    while(True):
        temp_input = input(">> ")
        if(checks(temp_input)):
            return convert_to_SHA256(temp_input)
        else:
            time.sleep(2)
            print("A Palavra-Passe tem conter as regras indicadas em cima \n")

print(get_password())