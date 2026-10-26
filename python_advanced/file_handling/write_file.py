#!/usr/bin/env python3
"""Módulo que contiene una función para escribir en un archivo UTF-8."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo de texto UTF-8.

    Crea el archivo si no existe y sobrescribe su contenido si ya existe.

    Args:
        filename (str): ruta del archivo donde escribir.
        text (str): cadena a escribir en el archivo.

    Returns:
        int: número de caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
