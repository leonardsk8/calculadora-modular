# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import math


def calcularDivisionModular(a, b, m):
    a = a % m
    inv = moduloInverso(b, m)
    if (inv == -1):
        print("La división no esta definida,")
    else:
        print("El resultado de la división es: ", (inv * a) % m)


def moduloInverso(b, m):
    g = math.gcd(b, m)
    if (g != 1):
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)


if __name__ == '__main__':
    print('CRIPTOLOGIA')
    Zn = int(input('INGRESE EL Zn: '))
    a = int(input('INGRESE EL A: '))
    b = int(input('INGRESE EL B: '))
    suma = (a + b) % Zn
    resta = (a - b) % Zn
    Multiplicacion = (a * b) % Zn
    division = (a / b) % Zn
    print('Suma: ', suma)
    print("Resta: ", resta)
    print("Multiplicación: ", Multiplicacion)
    calcularDivisionModular(a, b, Zn)
