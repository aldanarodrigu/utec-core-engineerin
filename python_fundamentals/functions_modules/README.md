# Python - Funciones y modularidad

**Nivel:** Novice | **Autor del proyecto:** Javier Valenzani | **Peso:** 1

## Descripción

Introducción a las funciones y la modularidad en Python: definir funciones,
distinguir `print` de `return`, entender cómo Python ejecuta un archivo y
reutilizar código entre archivos con `import` y `if __name__ == "__main__"`.

## Requisitos

- Ubuntu 20.04 LTS, Python 3.8.x
- Primera línea de cada archivo: `#!/usr/bin/env python3`
- Archivos ejecutables, con nueva línea final y estilo PEP8 (pycodestyle 2.7.x)
- Sin bibliotecas externas ni `sys.argv`

## Archivos

| # | Tarea | Archivo |
|---|-------|---------|
| 0 | `islower(c)`: indica si `c` es minúscula (usando `ord()`) | `islower.py` |
| 1 | `uppercase(str)`: imprime la cadena en mayúsculas | `uppercase.py` |
| 2 | `print_last_digit(number)`: imprime y devuelve el último dígito | `print_last_digit.py` |
| 3 | `pow(a, b)`: calcula `a` elevado a `b` con un bucle | `pow.py` |
| 4 | Ejecución de scripts y comportamiento de importación | `simple_add.py`, `test_import.py` |
| 5 | Importa `add` desde `add_0.py` e imprime `1 + 2 = 3` | `add.py` |
| 6 | Importa las funciones de `calculator_1.py` e imprime las 4 operaciones | `calculation.py` |
| 7 | Importa la variable `a` desde `variable_load_5.py` | `variable_load.py` |

## Uso

```bash
chmod +x *.py
./add.py
```

## Repositorio

`utec-core-engineering` / `python_fundamentals/functions_modules`
