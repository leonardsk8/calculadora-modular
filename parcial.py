import math

if __name__ == '__main__':
    print('PARCIAL CRIPTOLOGIA MÉTODO 1')
    Zn = 431
    A = 29
    for x in range(0, Zn, 1):
        resultado = A * x
        modulo = resultado % Zn
        if modulo == 1:
            print(A, " * ", x, " = ", resultado, " mod ", Zn, " = ", modulo)
            print("El inverso es ", x)
            break
        print(A, " * ", x, " = ", resultado, " mod ", Zn, " = ", modulo)


def moduloInverso(A, Zn):
    maximoComunDivisor = math.gcd(A, Zn)  # Greatest common divisor - Máximo común divisor
    print("El máximo común divisor es: ", maximoComunDivisor)
    # Es decir (b * g) == c mod Zn == 1
    if (maximoComunDivisor != 1):
        print("Los numeros no son primos relativos")
        return -1
    else:
        # Si b y m son primos relativos,
        # El modulo inverso es b^(m-2) modulo Zn
        print("Los numeros son primos relativos")
        return pow(A, Zn - 2, Zn)  # Lo mismo que b^(Zn-2) mod Zn


if __name__ == '__main__':
    print('\n\n\nPARCIAL CRIPTOLOGIA MÉTODO 2')
    Zn = 431
    A = 29
    inverso = moduloInverso(A, Zn)
    print("El inverso calculado por MCD es: ", inverso)
