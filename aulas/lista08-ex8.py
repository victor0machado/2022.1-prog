

MESES = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

class InvalidDateError(Exception):
    pass

def valida_dia(info):
    if not info.isnumeric():
        raise InvalidDateError("O dia precisa ser numérico!")

    if not 0 < int(info) < 31:
        raise InvalidDateError("O mês tem no máximo 31 dias!")

def valida_mes(info):
    if not info in MESES:
        raise InvalidDateError("Mês informado não é válido!")

def converte_formato_data(data_abreviada):
    if data_abreviada.count("/") != 2:
        raise InvalidDateError("Precisa de duas barras separando as informações!")
    elem = data_abreviada.split("/")
    valida_dia(elem[0])
    valida_mes(elem[1])
    return elem[0] + " de " + MESES[elem[1]] + " de " + elem[2]
