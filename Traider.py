#На самом деле это не класс торговца, а класс НПС
from staff import *
from static import *

class Traider:
    
    Yes_No=(
        "Да",
        "Нет",
    )
    staff=[Apple(V=0.6, P=0.5, Pr=250, He=30,Ty=1),
        Cherry(V=0.1, P=0.1, Pr=100, He=15,Ty=1),
        Strawberry(V=0.1, P=0.1, Pr=100, He=20,Ty=1),
        Heal_potion(V=0.5, P=0.5, Pr=400, He=50,Ty=1),]
    Sell_Buy=(
        "Продать",
        "Купить",
        "Отмена",
    )
    def __init__(self,money=0):
        self.M=money
    def traid(self):
        print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ")
        from Hero import Hero
        self.choise=Select("Продать или купить?",Traider.Sell_Buy)
        if(self.choise==0):#Продать
            print("Содержимое инвентаря:")
            j=0
            x=""
            for x in Hero.inventary:
                j+=1
                print(x)
                print("------------")
            if(j>0):
                choise2=Select("Хочешь что-то продать?",Traider.Yes_No)
                if(choise2==0):
                    d=Select("Введи номер предмета",Hero.inventary)
                    f=self.staff[d] 
                    g=Select("Уверен, что хочешь продать эту вещь?",Traider.Yes_No)
                    if(g==0):
                        Hero.inventary.pop(d)
                        Hero.inventary_pm+=0.5
                        Hero.inventary_vm+=0.5
                        Hero.Hero_money+=f.pr
                        print(f"Получено {f.pr} монет\nВсего на счету: {Hero.Hero_money}")
                        self.traid()
                    elif(g==1):
                        self.traid()
            elif(j==0):
                print("Инвентарь пуст! Тебе нечего продавать!")
                self.traid()
        elif(self.choise==1):#Купить
            x=""
            for x in self.staff:
                print(x)
                print("------------")
            choise2=Select("Хочешь что-то купить?",Traider.Yes_No)
            if(choise2==0):
                d=Select("Введи номер предмета",self.staff)
                f=self.staff[d]
                print(f"Цена данного предмета: {f.pr}")
                g=Select("Хочешь купить?",Traider.Yes_No)
                if(g==0):
                    if(Hero.Hero_money>=f.pr):
                        Hero.Hero_money=f.pr
                        Hero.inventary.append(f)
                        print(f"Покупка успешно совершена\nОстаток монет: {Hero.Hero_money}")
                        hero=Hero()
                        hero.Base()
                    elif(Hero.Hero_money<f.pr):
                        print("Недостаточно денег!")
                        self.traid()
            elif(choise2==1):#Отказ
                self.traid()
        elif(self.choise==2):
            hero=Hero()
            hero.Base()   


class Armorer:#Это класс для тогровца оружием и бронёй
      pass