"""Funcion que calcule el potencial gravitatorio, por Diana Resendiz"""


def potencialgravitatorio(G: float, M: float, r: float) -> float:
    resultado = -G*(M / r)

    return resultado


"""Funcion que convierta grados Celsius a Farenheit"""


def FarenheitCelsius(C: float) -> float:
    F = (C * 1.8) + 32

    return F
