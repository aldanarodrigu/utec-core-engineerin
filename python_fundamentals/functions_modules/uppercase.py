#!/usr/bin/env python3


def uppercase(str):
    texto = "{}".format(str)
    resultado = ""
    for caracter in texto:
        if 97 <= ord(caracter) <= 122:
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
    print("{}".format(resultado))
