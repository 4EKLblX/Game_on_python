from static import *
"""D-Урон-защита Pr-цена R-ранг оружия St-прочность Ty-тип вещи"""
class Weapon:
    def __init__(self,D,Pr,R,St,Ty):
        self.d=D
        self.pr=Pr
        self.r=R
        self.st=St
        self.ty=Ty
    def __str__(self):
        D=f"Урон:{self.d}"
        St=f"Прочность:{self.st}"
        R=f"Ранг оружия:{self.r}"
        Pr=f"Цена:{self.pr}"
        t=type(self).__name__
        return f"{t}\n{D}\n{St}\n{R}\n{Pr}"
    def __repr__(self) :
        return self.__str__()
    
class Bat(Weapon):
    def __init__(self,D,Pr,R,St,Ty):
        self.d=D;self.pr=Pr;self.r=R;self.st=St;self.ty=Ty
Bat.__name__="Бита с шипами"

class Knife(Weapon):
    def __init__(self,D,Pr,R,St,Ty):
        self.d=D;self.pr=Pr;self.r=R;self.st=St;self.ty=Ty
Knife.__name__="Добротный нож"

class Spear(Weapon):
    def __init__(self,D,Pr,R,St,Ty):
        self.d=D;self.pr=Pr;self.r=R;self.st=St;self.ty=Ty
Spear.__name__="Копьё"

class Axe(Weapon):
    def __init__(self,D,Pr,R,St,Ty):
        self.d=D;self.pr=Pr;self.r=R;self.st=St;self.ty=Ty
Axe.__name__="Колун"

class War_Axe(Weapon):
    def __init__(self,D,Pr,R,St,Ty):
        self.d=D;self.pr=Pr;self.r=R;self.st=St;self.ty=Ty
War_Axe.__name__="Боевой топор"