"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    import pandas as pd

    #Lectura archivos tbl0 y tbl2
    df_tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t",)
    df_tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t",)

    df_computado = pd.merge(df_tbl0, df_tbl2, on='c0')

    suma = df_computado.groupby("c1")["c5b"].sum()

    return suma
print(pregunta_13())