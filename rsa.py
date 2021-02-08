import math


def moduloInverso(A, Zn):
    print('PARCIAL CRIPTOLOGIA MÉTODO 1')
    for x in range(0, Zn, 1):
        resultado = A * x
        modulo = resultado % Zn
        if modulo == 1:
            return x


def calcularLlavePublica(fi):
    e = -1
    for x in range(2, fi, 1):
        e = x
        maximoComunDivisor = math.gcd(e, fi)
        if maximoComunDivisor == 1 and e % 2 != 0:
            break
    return e


def cifrarDescifrarMensaje(llave, primoGrande, mensaje):
    cifrado = []
    for x in mensaje:
        result = pow(x, llave, primoGrande)
        cifrado.append(result)
    return cifrado


if __name__ == '__main__':
    print('CRIPTOLOGIA ALGORITMO RSA')
    primoUno = 31
    primoDos = 17
    primoGrande = primoUno * primoDos
    fi = (primoUno - 1) * (primoDos - 1)
    llavePublica = calcularLlavePublica(fi)
    llavePrivada = moduloInverso(llavePublica, fi)
    if llavePublica == -1:
        print('NO SE PUEDE CALCULAR E')
    else:
        print('RESULTADO N: ', primoGrande)
        print('RESULTADO fi: ', fi)
        print('RESULTADO llave pública: ', llavePublica)
        print('RESULTADO llave privada: ', llavePrivada)
        mensaje = [18, 4, 6, 20, 17, 8, 3, 0, 3]
        mensajeCifrado = cifrarDescifrarMensaje(llavePublica, primoGrande, mensaje)
        print(mensajeCifrado)
        mensajeDescifrado = cifrarDescifrarMensaje(llavePrivada, primoGrande, mensajeCifrado)
        print(mensajeDescifrado)
