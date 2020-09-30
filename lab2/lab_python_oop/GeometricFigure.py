from abc import ABC, abstractmethod

class geometricFigure(ABC):

    @abstractmethod
    def area(self) -> object: #абстрактный метод для нахождения площади фигуры
        pass

    @abstractmethod
    def printfigure(self):
        pass