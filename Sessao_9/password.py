"""
Main Rule: No global variabels
"""
from hashlib import sha256

def get_password() -> str:
    print("Escreva uma Palavra-Passe. \n" \
    "Palavra-Passe com no minimo de 8 caracteres")
    return input(":>> ")
    

def checks(_text) -> bool:
    return {
        len(_text) >= 8 and 
        any(ch.isdigit() for ch in _text) and
        any(ch.islower() for ch in _text) and
        any(ch.isupper() for ch in _text) and
        any(not ch.isalnum() for ch in _text)
    }

def convert_to_SHA256 (_text) -> str:
    return sha256(_text.encode()).hexdigest()