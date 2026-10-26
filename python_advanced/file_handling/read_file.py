#!/usr/bin/env python3
"""Módulo que contiene una función para leer un archivo de texto UTF-8."""


def read_file(filename=""):
    """Lee un archivo de texto UTF-8 e imprime su contenido en stdout.

    Args:
        filename (str): ruta del archivo a leer.
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido, end="")
