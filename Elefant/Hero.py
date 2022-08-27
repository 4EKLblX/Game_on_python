from operator import invert
import random
from mobs import *
from static import *
from staff import *
from Traider import Traider
from Armor import *


class Hero:
    
    hero_armor=None#переменная, в которую будет заноситься надетая броня
    Hero_weapon=None#переменная, в которую будет заноситься надетое оружие
    Hero_money=200
    Z=(
        Zombie(random.randint(85,115),random.randint(2,5)*1,random.randint(2,5)*1,1),
        Zombie(random.randint(100,125),random.randint(2,5)*2,random.randint(2,5)*2,2),
        Zombie(random.randint(115,140),random.randint(2,5)*3,random.randint(2,5)*3,3),
        Zombie(random.randint(125,150),random.randint(2,5)*4,random.randint(2,5)*4,4),
        Zombie(random.randint(140,175),random.randint(2,5)*5,random.randint(2,5)*5,5),
    )  
    
    Yes_no=(
        "Да",
        "Нет",
    )
    
    """Ar-защита персонажа(влияет на получаемый урон)"""
    Ar=0
    inventary=[]#это список, в который будут заноситься кортежи с данными вещей, найденых в вылазке
    inventary_V=15#макс. место инвентаря
    inventary_vm=15#остаток места
    inventary_P=20#макс. вес инвентаря
    inventary_pm=20#остаток веса
    hero_armor=None#переменная, в которую будет заноситься надетая броня
    Hero_weapon=None#переменная, в которую будет заноситься надетое оружие
    Hero_money=200
    
    H_staff=(
        Apple(V=0.6, P=0.5, Pr=100, He=30,Ty=1),
        Cherry(V=0.1, P=0.1, Pr=100, He=15,Ty=1),
        Strawberry(V=0.1, P=0.1, Pr=100, He=20,Ty=1),
        Heal_potion(V=0.5, P=0.5, Pr=100, He=50,Ty=1),
    )
    C_staff=(
        Toy(V=0.2, P=0.3, Pr=150,Ty=0),
        Toy2(V=0.3, P=0.6, Pr=400,Ty=0),
        Ring(V=0.5, P=0.7, Pr=300,Ty=0),
    )
    A_staff=(#Броня
        Shirt(5,150,1,50,3),
        Armored_Shirt(7,280,2,75,3),
        F_Leather_Armor(10,450,3,120,3),
        G_Leather_Armor(14,600,4,160,3),
    )
    chanse1=60
    chanse2=20
    chanse3=10
    Zhp=0
    Zsp=0
    Zap=0
    actions= (
        "Шагать вперёд",
        "Осмотреться",
        "Вернуться на базу",
        "Открыть инвентарь",
        
    )
    actions_on_base=(
        "Алхимик",
        "Оружейник",
        "Выйти с базы",
        "Открыть инвентарь",
    )
    actions2=(
        "Сражаться",
        "Убежать",
    )
    metrs=0#количество пройденых метров
    Fight_actions=(
        "Простой удар",
        "Сильный удар",
        "Лечение",
        "Убежать",
    )
    lvlUp=1
    def __init__(self,HP=150,AP=5,SP=5,Lvl=1):
        self.lvl=Lvl
        self.hp=HP*Lvl
        self.ap=AP*Lvl
        self.sp=SP*Lvl
        self.zhp=0
        
    def Choise_Action(self):
        print("--------- --------- --------- --------- --------- --------- ---------")
        self.choise=Select("Выбери действие",Hero.actions)
        """Шагать вперёд"""
        if(self.choise==0):
            self.chanse=random.randint(0,1)
            print("Ты продвинулся на 10 метров вперёд")
            self.metrs+=10
            if(self.chanse==0):
                print("Врагов не встречено")
                return self.Main()
                #Враг встречен, идёт рандомный выбор зомби
            elif(self.chanse==1):
                self.Z_enemy=Random_Choise(Hero.Z)
                print("Встречен враг:",self.Z_enemy)
                Hero.Zhp=self.Z_enemy.hp#заполнение переменных для боя
                Hero.Zap=self.Z_enemy.ap
                Hero.Zsp=self.Z_enemy.sp 
                self.Choise_to_Fight()#переход к бою
        elif(self.choise==1):
            
            """60% что ничего не будет найдено; 20, что будет найден предмет; 10, что будет найден враг"""
            i=random.choices([0,1,2], weights=[Hero.chanse1,Hero.chanse2,Hero.chanse3], k=1)[0]#Расчёт шанса на нахождение чего-либо
            if(i==0):
                print("Ничего не найдено")
                Hero.chanse1-=10
                Hero.chanse3+=10
                self.Choise_Action()
            elif(i==1):
                Hero.chanse1=60
                Hero.chanse2=20
                Hero.chanse3=10
                d=random.choices([0,1,2], weights=[70,25,5], k=1)[0]#Определение типа вещи(Обычной или Хилящей)
                if(d==0):#Обычная-----------------------------------------------------
                    c=Random_Choise(Hero.C_staff)
                    print(f"Найден предмет: {c}")
                    g=Select("Поднять?",Hero.Yes_no)
                    if(g==0):
                        Hero.inventary_vm-=c.v
                        Hero.inventary_pm-=c.p
                        Hero.inventary.append(c)
                        print(f"Вещь поднята \nОстаток места в рюкзаке: {Hero.inventary_vm}\nОстаток веса:{Hero.inventary_pm}")
                        self.Choise_Action()
                    elif(g==1):
                        self.Choise_Action()
                elif(d==1):#Хилящая-----------------------------------------------------
                    c=Random_Choise(Hero.H_staff)
                    print(f"Найден предмет: {c}")
                    g=Select("Поднять?",Hero.Yes_no)
                    if(g==0):
                        Hero.inventary_vm-=c.v
                        Hero.inventary_pm-=c.p
                        Hero.inventary.append(c)
                        print(f"Вещь поднята \nОстаток места в рюкзаке: {Hero.inventary_vm}\nОстаток веса:{Hero.inventary_pm}")
                        self.Choise_Action()
                    elif(g==1):
                        self.Choise_Action()
                elif(d==2):#Броня-----------------------------------------------------
                    c=Random_Choise(Hero.A_staff)
                    print(f"Найден предмет: {c}")
                    g=Select("Поднять?",Hero.Yes_no)
                    if(g==0):
                        Hero.inventary.append(c)
                        print(f"Вещь поднята \nОстаток места в рюкзаке: {Hero.inventary_vm}\nОстаток веса:{Hero.inventary_pm}")
                        self.Choise_Action()
                    elif(g==1):
                        self.Choise_Action()
            elif(i==2):
                
                self.Z_enemy=Random_Choise(Hero.Z)
                print("Встречен враг:",self.Z_enemy)
                Hero.Zhp=self.Z_enemy.hp#заполнение переменных для боя
                Hero.Zap=self.Z_enemy.ap
                Hero.Zsp=self.Z_enemy.sp
                self.Choise_to_Fight()#переход к бою
        elif(self.choise==2):#возврат на базу
            print(f"Ты вернулся на базу, хп восстановлены\nВсего пройдено {self.metrs} метров")
            self.Base()
        elif(self.choise==3):
            self.Inventory()
        
        
        
    def Base(self):
        base_choise=Select("Выбери действие",Hero.actions_on_base)
        if(base_choise==0):
            self.Use_Traider()
        elif(base_choise==1):
            pass
        elif(base_choise==2):
            print("Удачной вылазки")
            self.Main()
        elif(base_choise==3):
            self.Inventory()
            
    EC=20#шанс побега
    CF=80#шанс неудачного побега   
        
    indi=0#Индикатор того, что инвентарь был открыт в боюю
            
    def Inventory(self):
        #print('\n'.join(str(x) for x in Hero.inventary)) 
        g=0
        x=""
        print("СПИСОК ПРЕДМЕТОВ В ИНВЕНТАРЕ:")
        for x in Hero.inventary:
            g+=1
            print(x)
            print("------------")
        if(g>0):
            c=Select("Хочешь использовать предмет из инвентаря?",Hero.Yes_no)
            if(c==0):
                d=Select("Введи номер предмета",Hero.inventary)
                f=Hero.inventary[d]
                if(f.ty==1):#это проверка типа вещи переменная автоматически не прописывалась, поэтому пришлось писать вручную
                    self.hp+=f.he#восстановление хп
                    Hero.inventary_pm+=0.5
                    Hero.inventary_vm+=0.5
                    print(f"Восстановленно {f.he} хп")
                    Hero.inventary.pop(d)
                elif(f.ty==2):
                    print("Эту вещь можно только продать") 
                elif(f.ty==3):
                    yn=Select("Хочешь её надеть?",self.Yes_no)
                    if(yn==0):
                        self.inventary.append(self.hero_armor)
                        self.hero_armor=f
                        self.inventary.pop(self.hero_armor)
                        self.Ar=f.ar
                        print(f"Защита персонажа: {self.Ar}")
                    elif(yn==1):
                        self.Inventory()
                        
                        
                print(f"Всего хп: {self.hp}")  
                print("--------- --------- --------- --------- --------- --------- ---------")
                self.Choise_Action()
            elif(c==1):
                self.Choise_Action()
        else:
            print("Инвентарь пуст!")
            self.Choise_Action()
    
    exp=0
    
                  
    def Fight(self):
        Hero.indi=1
        Hero.chanse1=60
        Hero.chanse2=20
        Hero.chanse3=10

        print("Ход врага")
        self.hp=self.hp-Hero.Zsp+(self.Ar/2)
        if(self.hp<=0):
            print("Ты умер") 
        else:
            print(f"Враг нанес {Hero.Zsp+(self.Ar/2)} урона\nОстаток хп: {self.hp}")
            fa=Select("Выберите действие: ",Hero.Fight_actions)
            if(fa==0):#Простой удар
                attack_point=random.randint(5,15)#рандом наносимого урона
                Hero.Zhp-=attack_point
                print(f"Вы нанесли {attack_point} урона\nОстаток хп зомби: {Hero.Zhp}")
                if(Hero.Zhp<=0):
                    print("Враг повержен!")
                    i=random.randint(5,15)
                    Hero.exp+=i 
                    print(f"Получено {i} опыта")
                    if(Hero.exp>=100*self.lvl):
                        self.lvl+=1
                        print(f"Уровень повышен!\nТекущий уровень {self.lvl}")
                    else:
                        return self.Choise_Action()
                else:
                    return self.Fight() 
            elif(fa==1):#Сильный удар
                attack_point=random.randint(10,25)
                Hero.Zhp-=attack_point
                print(f"Вы нанесли {attack_point} урона\nОстаток хп зомби: {Hero.Zhp}")
                if(Hero.Zhp<=0):
                    print("Враг повержен!")
                    i=random.randint(5,15)
                    Hero.exp+=i
                    print(f"Получено {i} опыта")
                    if(Hero.exp>=100*self.lvl):
                        self.lvl+=1
                        print(f"Уровень повышен!\nТекущий уровень {self.lvl}")
                    else:
                        return self.Choise_Action()
                else:
                    return self.Fight()
            elif(fa==2):#Лечение
                print("Использовано лечение")
                heal=random.randint(10,15)
                self.hp+=heal
                print(f"Восстановлено хп: {heal}\nКоличество хп: {self.hp}")
                if(self.hp<150):
                    return self.Fight()
                elif(self.hp>150):
                    self.hp=150
                    return self.Fight()
            elif(fa==3):#Побег из боя
                print(f"Совершается попытка побега, шанс на успешный побег: {Hero.EC}")
                i=random.choices([0,1], weights=[Hero.CF,Hero.EC], k=1)[0]#Расчёт шанса на успешный побег
                if(i==0):
                    print("Попытка побега не удалась")
                    self.hp=self.hp-Hero.Zsp
                    print(f"Во время попытки побега враг нанес тебе {Hero.Zsp} урона\nОстаток хп: {self.hp}")
                    Hero.CF-=10
                    Hero.EC+=10
                    return self.Fight()
                elif(i==1):
                    print("Успешный побег!")
                    print(f"Оставшееся количество хп: {self.hp}")
                    Hero.CF=80
                    Hero.EC=20
                    self.Choise_Action()
    def Inspection(self):#метод для сбора лута с трупов врагов
        Ins=Select("Осмотреть тело?",Hero.Yes_no)
        if(Ins==0):
            pass
        elif(Ins==1):
            self.Choise_Action() 
            
            
    def Use_Traider(self):
        traider=Traider()
        traider.traid()
             
    def Choise_to_Fight(self):
        self.choise=Select("Выбери действие, человек!",Hero.actions2)
        if(self.choise==0):
            self.Fight()
        elif(self.choise==1):
            print("Вы вышли из боя")
            self.Choise_Action()
    def Main(self):
        self.Choise_Action()         
                
                
panzer=Hero()
panzer.Base()
