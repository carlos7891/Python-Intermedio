def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    # try:
    #     num = int(input("Ingresa un numero: "))
    #     print(divisors(num))
    #     print("Termino mi programa")
    # except ValueError:
    #     print("Debes ingresar un numero")
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Termino mi programa")


if __name__ == '__main__':
    run()