from lab_python_oop.GeometricFigure import geometricFigure
from lab_python_oop.FigureColor import figureColor


class Rectangle(geometricFigure):
    figure = "Прямоугольник"

    def printfigure(self):
        return self.figure

    def __init__(self, figcolor, width, height):
        self.w = width
        self.h = height
        self.col = figureColor()
        self.col.colorf=figcolor

    def area(self):
        return self.w * self.h

    def __repr__(self):
        return ("{}, {} цвет, ширина = {}; высота = {}; площадь = {}".format(self.figure, self.col.colorf, self.w, self.h, self.area()))