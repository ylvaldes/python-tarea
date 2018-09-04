#!/usr/bin/env python3

from colorama import init, Fore, Back, Style
import string
__author__ = 'Yasmani Ledesma Valdés'

MAX_NUMERO = 999999999999

UNIDADES = ('cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve')
DECENAS = ('diez','once','doce','trece','catorce','quince','dieciseis','diecisiete','dieciocho','diecinueve')
MULT_DIEZ = ('cero','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa')
CIENTOS = ('_','ciento','doscientos','trescientos','cuatroscientos','quinientos','seiscientos','setecientos','ochocientos','novecientos')

def numero_a_letras(numero):
    numero_entero = int(numero)
    if numero_entero > MAX_NUMERO:
        raise OverflowError('Número demasiado alto')
    if numero_entero < 0:
        return 'menos {}'.format(numero_a_letras(abs(numero)))
    letras_decimal = ''
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
    if (numero_entero <= 99):
        resultado = leer_decenas(numero_entero)
    elif (numero_entero <= 999):
        resultado = leer_centenas(numero_entero)
    elif (numero_entero <= 999999):
        resultado = leer_miles(numero_entero)
    elif (numero_entero <= 999999999):
        resultado = leer_millones(numero_entero)
    else:
        resultado = leer_millardos(numero_entero)
    resultado = resultado.replace('uno mil', 'un mil')
    resultado = resultado.strip()
    resultado = resultado.replace(' _ ', ' ')
    resultado = resultado.replace('  ', ' ')
    if parte_decimal > 0:
        resultado = '{} {}'.format(resultado, letras_decimal)
    return resultado

def leer_decenas(numero):
    if numero < 10:
        return UNIDADES[numero]
    decena, unidad = divmod(numero, 10)
    if numero <= 19:
        resultado = DECENAS[unidad]
    elif numero <= 29:
        resultado = 'veinti{}'.format(UNIDADES[unidad])
    else:
        resultado = MULT_DIEZ[decena]
        if unidad > 0:
            resultado = '{} y {}'.format(resultado, UNIDADES[unidad])
    return resultado

def leer_centenas(numero):
    centena, decena = divmod(numero, 100)
    if numero == 0:
        resultado = 'cien'
    else:
        resultado = CIENTOS[centena]
        if decena > 0:
            resultado = '{} {}'.format(resultado, leer_decenas(decena))
    return resultado

def leer_miles(numero):
    millar, centena = divmod(numero, 1000)
    resultado = ''
    if (millar == 1):
        resultado = ''
    if (millar >= 2) and (millar <= 9):
        resultado = UNIDADES[millar]
    elif (millar >= 10) and (millar <= 99):
        resultado = leer_decenas(millar)
    elif (millar >= 100) and (millar <= 999):
        resultado = leer_centenas(millar)
    resultado = '{} mil'.format(resultado)
    if centena > 0:
        resultado = '{} {}'.format(resultado, leer_centenas(centena))
    return resultado

def leer_millones(numero):
    millon, millar = divmod(numero, 1000000)
    resultado = ''
    if (millon == 1):
        resultado = ' un millon '
    if (millon >= 2) and (millon <= 9):
        resultado = UNIDADES[millon]
    elif (millon >= 10) and (millon <= 99):
        resultado = leer_decenas(millon)
    elif (millon >= 100) and (millon <= 999):
        resultado = leer_centenas(millon)
    if millon > 1:
        resultado = '{} millones'.format(resultado)
    if (millar > 0) and (millar <= 999):
        resultado = '{} {}'.format(resultado, leer_centenas(millar))
    elif (millar >= 1000) and (millar <= 999999):
        resultado = '{} {}'.format(resultado, leer_miles(millar))
    return resultado

def leer_millardos(numero):
    millardo, millon = divmod(numero, 1000000)
    return '{} millones {}'.format(leer_miles(millardo), leer_millones(millon))

def main():
    init()
    inicio="Programa para convertir números a letras"
    print(Fore.RED+inicio.center(50,"*"))
    print(Style.RESET_ALL+"Escriba un número:")
    num=int(input())
    print('{} \t---> \t {}'.format(num,numero_a_letras(num).capitalize()))
    numeros=[0,-15,15,109.9,589,1587,13695,154789,5874695,95874563,999999999,128,1229]
    for x in numeros:
        print('{} \t---> \t {}'.format(x,numero_a_letras(x).capitalize()))
   

if __name__=='__main__':main()