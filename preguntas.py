"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

"importo csv, para leer los datos que me entregan"
import csv


def leer_data_csv():
    with open("data.csv", "r") as file:
        data = list(csv.reader(file, delimiter="\t"))
        # for row in data:
        #     print(row)
    return data


# data=leer_data_csv()
# print(data)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = leer_data_csv()
    suma = 0

    for row in data:
        suma += int(row[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = leer_data_csv()
    letra_cantidad = {}

    for i in data:
        letra = i[0]
        if letra in letra_cantidad:
            letra_cantidad[letra] += 1
        else:
            letra_cantidad[letra] = 1
    resultado = sorted(letra_cantidad.items(), key=lambda x: x[0])
    return resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = leer_data_csv()
    suma3 = {}
    for i in data:
        if i[0] in suma3.keys():
            suma3[i[0]] += int(i[1])
        else:
            suma3[i[0]] = int(i[1])
    sortedsum3 = sorted(suma3.items())
    return sortedsum3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = leer_data_csv()
    mes = {}
    for i in data:
        meses = i[2].split("-")[1]
        if meses in mes:
            mes[meses] += 1
        else:
            mes[meses] = 1
    cantmes = sorted(mes.items())
    return cantmes


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = leer_data_csv()
    lista = {}
    for i in data:
        word = i[0]
        value = int(i[1])
        if word in lista:
            lista[word].append(value)
        else:
            lista[word] = [value]
    resultado = []
    for words, values in lista.items():
        max_value = max(values)
        min_value = min(values)
        resultado.append((words, max_value, min_value))
        result_sort = sorted(list(resultado))
    return result_sort


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = leer_data_csv()
    valor_w = {}
    for i in data:
        dicod = i[4]
        dic = {}
        for z in dicod.split(","):
            clave, valor = z.split(":")
            dic[clave] = int(valor)
        for clave, valor in dic.items():
            if clave in valor_w:
                valor_w[clave] = (
                    min(valor_w[clave][0], valor),
                    max(valor_w[clave][1], valor),
                )
            else:
                valor_w[clave] = (valor, valor)
    resultado = [(clave, valores[0], valores[1]) for clave, valores in valor_w.items()]
    resultord = sorted(list(resultado))
    return resultord


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = leer_data_csv()
    wv = {}
    for i in data:
        vcs = int(i[1])
        l = i[0]
        if vcs in wv:
            wv[vcs].append(l)
        else:
            wv[vcs] = [l]
    resultd = sorted(wv.items())
    return resultd


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = leer_data_csv()
    wordv = {}
    for row in data:
        vcd = int(row[1])
        let = row[0]
        if vcd in wordv:
            wordv[vcd].append(let)
        else:
            wordv[vcd] = [let]
    results = sorted(
        [(valor, sorted(set(let))) for valor, let in wordv.items()], key=lambda x: x[0]
    )
    return results


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = leer_data_csv()
    wv = {}
    for row in data:
        for i in row[4].split(","):
            clave = i.split(":")[0]
            if clave in wv.keys():
                wv[clave] += 1
            else:
                wv[clave] = 1
    registros = dict(sorted(wv.items()))
    return registros


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = leer_data_csv()
    listatu = []
    for i in data:
        let1 = i[0]
        colum4 = len(i[3].split(","))
        colum5 = len(i[4].split(","))
        tupl = (let1, colum4, colum5)
        listatu.append(tupl)
    return listatu


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = leer_data_csv()
    suma = {}
    for row in data:
        letc4 = row[3].split(",")
        for i in letc4:
            if i in suma.keys():
                suma[i] += int(row[1])
            else:
                suma[i] = int(row[1])
    sumaletord = dict(sorted(suma.items()))
    return sumaletord


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    data = leer_data_csv()
    letra = {}
    for row in data:
        value = row[4].split(",")
        dicv = dict((rw.split(":")[0], int(rw.split(":")[1])) for rw in value)
        if row[0] in letra.keys():
            letra[row[0]] += sum(dicv.values())
        else:
            letra[row[0]] = sum(dicv.values())
    resultadordenado = dict(sorted(letra.items()))
    return resultadordenado
