mes = input("Ingrese un mes: ")

meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "seeptiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,}

if mes.lower() in meses:
    numero_mes = meses[mes.lower()]
    print(f"El número del mes {mes} es {numero_mes}.")