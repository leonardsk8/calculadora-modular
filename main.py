# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import math


def calcularDivisionModular(a, b, Zn):
    a = a % Zn
    inv = moduloInverso(b, Zn)
    if (inv == -1):
        print("La división no esta definida,")
    else:
        print("El resultado de la división es: ", (inv * a) % Zn)


def moduloInverso(b, Zn):
    g = math.gcd(b, Zn)
    if (g != 1):
        return -1
    else:
        # Si b y m son primos relativos,
        # El modulo inverso es b^(m-2) modulo Zn
        return pow(b, Zn - 2, Zn) # Lo mismo que b^(m-2) % Zn


if __name__ == '__main__':
    print('CRIPTOLOGIA')
    Zn = int(input('INGRESE EL Zn: '
                   ''))
    a = int(input('INGRESE EL A: '
                  ''))
    b = int(input('INGRESE EL B: '
                  ''))
    suma = (a + b) % Zn
    resta = (a - b) % Zn
    Multiplicacion = (a * b) % Zn
    print('')
    print('Suma: ', suma)
    print("Resta: ", resta)
    print("Multiplicación: ", Multiplicacion)
    calcularDivisionModular(a, b, Zn)
