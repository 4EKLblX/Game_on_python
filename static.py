#Метод выбора, заменяющий неудобный switch
import random
def Select(label, args):
        try:
            index =0
            print(label)
            for a in args:
                index+=1#инкрементация, для продолжения прокручивания и вывода всех вариантов
                print(f"{index}: {a}")
            index= int(input("?: "))#выбор варианта
            return index-1
        except Exception as ex:
            print(ex); return Select(label, args)
def Random_Choise(args, format=str):
    try:
        i=0
        for d in args:#подсчёт количества аргументов
            i+=1
        index=random.randint(0,i)#сам рандом
        return args[index-1]#возврат выбранного аргумента
    except Exception as ex:
        print(ex);return args
