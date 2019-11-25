from figure import Figure
from color import Color
import math 

class Circle (Figure):
     Figure_type = "Круг"

     def __init__ (self, color_param, r_param):
         self.r = r_param
         self.fig_color = Color()
         self.fig_color.color_property = color_param

     def Area(self):
         return math.pi*(self.r**2)

     def __repr__ (self):
         return '{} {} цвета, радиусом {}, площадью {}.'.format (Circle.get_figure_type(), self.fig_color.color_property, self.r, self.Area())
