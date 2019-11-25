# в общем:
# можно сделать метод класса его атрибутом, благодаря чему можно выводить комбинацию значений как одно

class Color:

    def __init__(self):
        self._color = None

    @property
    def color_property (self):
        return self._color

    @color_property.setter
    def color_property (self, value):
        self._color = value
