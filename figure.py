from abc import ABC, ABCMeta, abstractmethod

class Figure (ABC):

    @abstractmethod
    def Area (self): #абстрактный метод
        pass      
    
    @classmethod
    def get_figure_type (cls):
        return cls.Figure_type