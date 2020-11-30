if __name__ == '__main__':
    print('PARCIAL CRIPTOLOGIA')
    Zn = 431
    A = 29
    for x in range(0, Zn, 1):
        if (A * x) % Zn == 1:
            print("El inverso es ", x)
