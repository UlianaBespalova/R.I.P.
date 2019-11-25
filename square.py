from rect import Rect

class Square (Rect):

    Figure_type = "Квадратик"

   # @classmethod
   # def get_figure_type (cls):
   #    return cls.Figure_type

    def __init__ (self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__ (self):
        return '{} {} цвета, со стороной {}, площадью {}.'. format(Square.get_figure_type(), self.fig_color.color_property, self.side, self.Area())

