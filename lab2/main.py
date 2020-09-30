from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rect = Rectangle("синий", 5, 5)
    circ = Circle("зеленый", 5)
    sq = Square("красный", 5)

    print(rect)
    print(circ)
    print(sq)

if __name__ == "__main__":
    main()
