#!/usr/bin/env python3
"""Módulo que contiene una función para añadir texto a un archivo UTF-8."""


def append_write(filename="", text=""):
    """Añade una cadena al final de un archivo de texto UTF-8.

    Si el archivo no existe, lo crea.

    Args:
        filename (str): ruta del archivo al que añadir texto.
        text (str): cadena a añadir al final del archivo.

    Returns:
        int: número de caracteres añadidos.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
