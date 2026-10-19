#!/usr/bin/env python3


def uppercase(str):
    resultado = ""
    for caracter in str:
        if 97 <= ord(caracter) <= 122:
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
    print(resultado)
