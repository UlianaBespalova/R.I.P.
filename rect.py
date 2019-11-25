from color import Color
from figure import Figure

class Rect (Figure):

    Figure_type = "Прямоугольник"

    def __init__(self, color_param, w_param, h_param):
        self.w = w_param
        self.h = h_param
        self.fig_color = Color()
        self.fig_color.color_property = color_param

    def Area (self):
        return self.w*self.h

    def __repr__ (self):
        return '{} {} цвета, шириной {} и высотой {}, площадью {}.'. format(Rect.get_figure_type(), self.fig_color.color_property, self.w, self.h, self.Area())

