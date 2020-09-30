class figureColor:

    def __init__(self):
        self._color = None

    # геттер
    @property
    def colorf(self):
        return self._color

    # сеттер
    @colorf.setter
    def colorf(self, value):
        self._color = value
