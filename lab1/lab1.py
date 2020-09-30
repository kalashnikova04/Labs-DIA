import sys

print("Калашникова А.В. ИУ5-54Б")
#считывание коэффициентов из командной строки
if len(sys.argv) > 1:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("Введены нечисловые значения коэффициентов!")
        while (True):
            print("Введите коэффициенты биквадратного уравнения снова!")
            try:
                a = float(input())
                b = float(input())
                c = float(input())
            except ValueError: print("Снова неверный ввод!")
            break
    print("Введенные значения: A = {}, B = {}, C = {}".format(a, b, c))

else:
    try:
        a = float(input("Введите коэффициент А: "))
        b = float(input("Введите коэффициент B: "))
        c = float(input("Введите коэффициент C: "))
    except ValueError:
        print("Введите корректные символы!")
print(f"Полученное биквадратное уравнение: {a}*x^4 + {b}*x^2 + {c} = 0")


def calcOfRoots(a, b, c) -> object:
    D = pow(b, 2) - 4 * a * c
    # Производим замену t=х^2 -> a*t^2 + b*t + c = 0
    if a == 0 and b == 0 and c == 0:
        print("Уравнение имеет бесконечное количество корней!")
    elif a == 0 and b == 0:
        print("Уравнение не имеет корней!")
    elif a == 0:
        print("Неполное квадратное уравнение!")
        x = -c / b
        if x == 0:
            x1 = 0
            print('Имеет единтсвенный корень: x = {x1}')
        elif x < 0:
            print("Уравнение не имеет корней!")
        else:
            y = pow(x, 0.5)
            print("Уравнение имеет два корня: x1 = {}, x2 = {}".format(y, -y))
    elif D < 0:
        print("Дескриминант отрицательный! Действительных корней нет!")
    elif D == 0:
        t = -b / 2 * a
        if t < 0:
            print("Действительных корней нет!")
        elif t == 0:
            print("Уравнение имеет единственный корень х=0")
        else:
            x = t ** 0.5
            print("Уравнение имеет два корня: x1 = {}, x2 = {}".format(x, -x))
    else:
        t1 = (-b + pow(D, 0.5)) / (2 * a)
        t2 = (-b - pow(D, 0.5)) / (2 * a)
        if (t1, t2) > (0, 0):
            x1 = pow(t1, 0.5)
            x3 = pow(t2, 0.5)
            print("Уравнение имеет четыре корня: x1 = {}, x2 = {}, x3 = {}, x4 = {}".format(x1,-x1,x3,-x3))
        elif t1 < 0 and t2 > 0:
            x = pow(t2, 0.5)
            print("Уравнение имеет два корня: x1 = {}, x2 = {}".format(x, -x))
        elif t2 < 0 and t1 > 0:
            x = pow(t1, 0.5)
            print("Уравнение имеет два корня: x1 = {}, x2 = {}".format(x, -x))
        else:
            print("Действительных корней нет!")


calcOfRoots(a, b, c)
