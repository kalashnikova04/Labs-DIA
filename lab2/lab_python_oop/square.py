from lab_python_oop.rectangle import Rectangle
from lab_python_oop.FigureColor import figureColor


class Square(Rectangle):
    figure: str = "Квадрат"

    def printfigure(self):
        return self.figure

    def __init__(self, figcolor, side):
        self.s = side
        self.col = figureColor()
        self.col.colorf = figcolor

    def area(self):
        return pow(self.s, 2)

    def __repr__(self):
        return ("{}, {} цвет, сторона = {}; площадь = {}".format(self.figure, self.col.colorf, self.s, self.area()))
