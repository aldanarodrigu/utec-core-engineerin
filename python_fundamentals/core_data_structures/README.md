# Python - Estructuras de datos básicas

**Nivel:** Novice | **Directorio:** `python_fundamentals/core_data_structures`

## Descripción

Funciones que trabajan con listas, matrices, tuplas, conjuntos y
diccionarios.

## Requisitos

- Ubuntu 20.04 LTS, Python 3.8.x
- Primera línea de cada archivo: `#!/usr/bin/env python3`
- Archivos ejecutables, con nueva línea final y estilo PEP8 (pycodestyle 2.7.x)

## Archivos

| Archivo | Función | Descripción |
|---------|---------|-------------|
| `print_list_integer.py` | `print_list_integer(my_list=[])` | Imprime los enteros de una lista, uno por línea (con `:d`) |
| `element_at.py` | `element_at(my_list, idx)` | Devuelve el elemento en `idx`, o `None` si es negativo o está fuera de rango |
| `replace_in_list.py` | `replace_in_list(my_list, idx, element)` | Reemplaza el elemento en `idx`; si el índice no es válido, devuelve la lista original |
| `print_matrix_integer.py` | `print_matrix_integer(matrix=[[]])` | Imprime una matriz, una fila por línea y valores separados por un espacio |
| `add_tuple.py` | `add_tuple(tuple_a=(), tuple_b=())` | Suma dos tuplas y devuelve una tupla de dos enteros (faltantes = 0) |
| `common_elements.py` | `common_elements(set_1, set_2)` | Devuelve el conjunto de elementos comunes |
| `update_dictionary.py` | `update_dictionary(a_dictionary, key, value)` | Reemplaza o agrega un par clave/valor y devuelve el diccionario |
| `best_score.py` | `best_score(a_dictionary)` | Devuelve la clave con el valor más grande, o `None` si es `None` o está vacío |

## Uso

```bash
chmod +x *.py
```

```python
>>> element_at = __import__('element_at').element_at
>>> element_at(["a", "b", "c"], 1)
'b'
```
