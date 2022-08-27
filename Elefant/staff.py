#Класс для вещей, встреченных в вылазках
import random

"""V-объём вещи P-вес Pr-цена Ty-тип предмета для разделения"""
class Cstaff():#Обычные вещи, что можно пустить на продажу
    def __init__(self, V, P, Pr,Ty):
        self.v=V;self.p=P; self.pr=Pr; self.ty=Ty
    def __str__(self):
        v=f"Объём вещи: {self.v}"
        p=f"Вес вещи: {self.p}"
        pr=f"Предпологаемая цена: {self.pr}"
        t=type(self).__name__
        return f"{t}\n{v}\n{p}\n{pr}"
    def __repr__(self) -> str:
        return self.__str__()
    
"""V-объём вещи P-вес Pr-цена He-Количество восстанавливаемого здоровья Ty-тип предмета для разделения"""
class Hstaff():#Вещи,позволяющие восстановить здоровье
    def __init__(self, V, P, Pr,He,Ty):
        self.v=V;self.p=P; self.pr=Pr;self.he=He; self.ty=Ty
    def __str__(self):
        v=f"Объём вещи: {self.v}"
        p=f"Вес вещи: {self.p}"
        pr=f"Предпологаемая цена: {self.pr}"
        he=f"Количество восстанавливаемого здоровья: {self.he}"
        t=type(self).__name__
        return f"{t}\n{v}\n{p}\n{he}\n{pr}"
    def __repr__(self) -> str:
        return self.__str__()
    
    
"""тут начинаются сами вещи"""
class Toy(Cstaff):
    def __init__(self, V, P, Pr,Ty=0):
        self.v=V;self.p=P; self.pr=Pr; self.ty=Ty
Toy.__name__="Цацка"
class Toy2(Cstaff):
    def __init__(self, V, P, Pr,Ty=0):
        self.v=V;self.p=P; self.pr=Pr; self.ty=Ty
Toy2.__name__="Цацка с бриллиантом"

class Ring(Cstaff):
    def __init__(self, V, P, Pr,Ty=0):
        self.v=V;self.p=P; self.pr=Pr; self.ty=Ty
Ring.__name__="Кольцо с топазом"


"""тут начинаются вещи с отхилом"""
class Apple(Hstaff):
    def __init__(self, V=0.6, P=0.5, Pr=100, He=random.randint(25,40),Ty=1):
        self.v=V;self.p=P; self.pr=Pr;self.he=He; self.ty=Ty
Apple.__name__="Тыблоко"

class Heal_potion(Hstaff):
    def __init__(self, V=0.5, P=0.5, Pr=100, He=random.randint(40,65),Ty=1):
        self.v=V;self.p=P; self.pr=Pr;self.he=He; self.ty=Ty
Heal_potion.__name__="Лечебное зелье"

class Cherry(Hstaff):
    def __init__(self, V=0.1, P=0.1, Pr=100, He=random.randint(5,15),Ty=1):
        self.v=V;self.p=P; self.pr=Pr;self.he=He; self.ty=Ty
Cherry.__name__="Вишня"

class Strawberry(Hstaff):
    def __init__(self, V=0.1, P=0.1, Pr=100, He=random.randint(10,20),Ty=1):
        self.v=V;self.p=P; self.pr=Pr;self.he=He; self.ty=Ty
Strawberry.__name__="Клубника"
