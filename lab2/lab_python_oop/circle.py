import math
from lab_python_oop.GeometricFigure import geometricFigure
from lab_python_oop.FigureColor import figureColor


class Circle(geometricFigure):
    figure = "Круг"

    def printfigure(self):
        return self.figure

    def __init__(self, figcolor, radius):
        self.r = radius
        self.col = figureColor()
        self.col.colorf=figcolor

    def area(self):
        return math.pi * pow(self.r, 2)

    def __repr__(self):
        return "{}, {} цвет, радиус = {}; площадь = {}".format(self.figure, self.col.colorf, self.r, self.area())
