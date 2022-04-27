def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try: 
        num = int(input('Ingresa un nÃºmero: '))
        print(divisors(num))
        print("TerminÃ³ mi programa")
    except ValueError: 
        print("Debes ingresar un nÃºmero")


if __name__ == '__main__':
    run()