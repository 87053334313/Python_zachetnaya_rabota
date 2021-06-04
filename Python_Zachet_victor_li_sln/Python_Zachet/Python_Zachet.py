import datetime
import time
import json

class Products:
    Category=""
    Product=""
    Cost=0
    Date=datetime.datetime.now()


    def __init__(self,cat,prod,cost):
        self.Category=cat
        self.Product=prod
        self.Cost=cost
        self.Date=datetime.datetime.now()
    
    def ToString(self):
        return "[ Category="+str(self.Category)+", Name="+str(self.Product)+", Cost="+str(self.Cost)+", Date="+str(self.Date)+" ]"


filenamestring = 'test.txt';

def Show_all():
    myfile=open(filenamestring,'r')
    alltext=myfile.read()
    print(alltext)
    myfile.close()

def Add_1(_string):
    myfile=open(filenamestring,'a')
    myfile.write(str(_string)+"\n")
    myfile.close()


def Add(_category,_product,_cost):
    prod_1 =Products(_category,_product,_cost)
    str_prod=prod_1.ToString()
    Add_1(str_prod)
    print("Продукт был успешно добавлен")
 

def Find_Kategory(string_category,full_str):

    str_all_text=full_str

    


    int_otkriv_kvad_skobka=str_all_text.find("[",0)
    int_dlina=len(string_category)
    first_index_iz_all_text=str_all_text.find(string_category)


    index_category=str_all_text.find("Category=")
    len_category=len("Category=")


    if(str_all_text[(index_category+len_category):(index_category+len_category+len(string_category))]==string_category):
        index_kvad_zakr=str_all_text.find("]",first_index_iz_all_text)
        print("ваша искомая строка:\n",str_all_text[int_otkriv_kvad_skobka:index_kvad_zakr])



def ReadPostrochno(_string_category):
    with open("test.txt") as file:
        array = [row.strip() for row in file]
        for eachline in array:
                        new_str=eachline
                        Find_Kategory(_string_category,new_str);




def Find_Date(string_category,full_str):

    str_all_text=full_str

    


    int_otkriv_kvad_skobka=str_all_text.find("[",0)
    int_dlina=len(string_category)
    first_index_iz_all_text=str_all_text.find(string_category)


    index_category=str_all_text.find("Date=")
    len_category=len("Date=")


    if(str_all_text[(index_category+len_category):(index_category+len_category+len(string_category))]==string_category):
        index_kvad_zakr=str_all_text.find("]",first_index_iz_all_text)
        print("ваша искомая строка:\n",str_all_text[int_otkriv_kvad_skobka:index_kvad_zakr])



def ReadPostrochnoData(_string_category):
    with open("test.txt") as file:
        array = [row.strip() for row in file]
        for eachline in array:
                        new_str=eachline
                        Find_Date(_string_category,new_str);


















def Test():
    with open("test.txt","r") as ins:

        array={}
        for line in ins:
            index_cost_name=line.find("Cost=")
            line_cost_name=len("Cost=")
            fine_true_zapyat=line.find(",",index_cost_name)
            need_str_cost=line[(index_cost_name+line_cost_name):fine_true_zapyat]
            int_cost=int(need_str_cost)
            array[line]=int_cost

        for i in sorted(array.items(), key=lambda para:para[1]):
            print(i)
            
       

def Test2():
    with open("test.txt","r") as ins:

        array={}
        for line in ins:
            index_cost_name=line.find("Cost=")
            line_cost_name=len("Cost=")
            fine_true_zapyat=line.find(",",index_cost_name)
            need_str_cost=line[(index_cost_name+line_cost_name):fine_true_zapyat]
            int_cost=int(need_str_cost)
            array[line]=int_cost

        for i in reversed(sorted(array.items(), key=lambda para:para[1])):
            print(i)
                       
        
def DeleteStr(__string):
    array=[]
    with open("test.txt","r") as ins:
        for line in ins:
            array.append(line)

    int_kolvo=len(array)
    i=0;
    while(i<int_kolvo):
        if(str(array[i]).find(__string)!=-1):
            array[i]=""
        i+=1

    myfile=open(filenamestring,'w')
    for str_arr in array:
        myfile.write(str_arr)
    myfile.close()



    print("Всё прошло успешно строка удалена")







print("Данная программа работает если в этой же папке есть файл'test.txt'\n Здравствуйте, хотите ли вы добавить продукт?(Это быстрое меню чтобы только добавлять продукты) \n введите 'yes' или 'no' \n Если хотите посмотреть все команды введите любую другую комбинацию символов и нажмите enter\n рекомендую нажать просто 'enter(тогда откроется меню)'")
str_first=input()    
if(str_first=="yes"):
    try:
        print("Отлично введите \n Сейчас будут по очереди выводиться характеристики объекта добавления\nчто будем добавлять(сорт):")
        str_prod=input("(сейчас введите на английском  и в последующем все что касается товаров на английском) тип добавляемого товара:")
        str_name=input("Введите название товара:")
        int_cost=int(input("Введите цену товара:"))
        print("добавление...")
        Add(str_prod,str_name,int_cost)
        time.sleep(1)
        print("Всё успешно добавилось")
        print("Хотите ли  вы помотреть что есть на данный момент в файле \n введите 'yes' или 'no' \n В любом случае если вы пошли по этой ветке это последняя команда, но я предусмотрел  другую возможность когда вы введете при старте программы что нибудь наугад!!!")
        str_otvet_dva=input()
        if(str_otvet_dva=="yes"):
            print("загружаю.... немного подождите")
            time.sleep(1)
            Show_all()
        elif str_otvet_dva=="no":
            print("Ну как хочешь \n Сразу тогда закрою программу")
        else:
            print("Вы ввели не те команды,я закрываю всё'")



    except BaseException:
        print("Произошла ошибка")

        print("Это конец программы спасибо, всего хорошего!\n Если хочешь посмотреть все функци перезапусти программу и введи enter")

elif str_first=="no":
    print("Хотите посмотреть текущий список товаров напиште 'yes' или 'no'")
    str_third=input()
    if(str_third=="yes"):
        print("Ща загружаю...")
        time.sleep(1)
        Show_all()
        print("Конец программы")
    else:
        print("Ну раз нет то пока!")
else:

     print("Меню доступных команд:")
     print("если хочешь найти по типу товар введи'type'")
     print("если хочешь найти по дате товар введи'datas'(вводить нужно будет через'-'год,месяц,дату)")
     print("для ввывода всех товаров по стоимости по возрастанию введите 'sort'")
     print("для ввывода всех товаров по стоимости по убыванию введите 'desc'")
     print("ecли хочешь выйти введи exit")
     print("если хочешь посмотреть всю базу данных введи showall")
     print("eсли хочешь добавить товар введи add")
     print("если хочешь удалить строку запись введенными тобой символами напиши 'del'")
     str_4=input()
     if(str_4=="type"):
         print("Введи тип товара:")
         str_type=input()
         ReadPostrochno(str_type)
     elif(str_4=="datas"):
        print("Введи искомую дату в формате год месяц день аля:'xxxx-xx-xx'")
        str_find_date=input()
        ReadPostrochnoData(str_find_date)
     elif(str_4=="del"):
          del_str=input("Введи символы из неугодной записи, и данная строка будет удалена:")
          DeleteStr(del_str)
     elif(str_4=="sort"):
         Test()
     elif(str_4=="desc"):
         Test2()
     elif(str_4=="exit"):
         print("Всего хорошего!")
     elif(str_4=="showall"):
         print("загружаю.... немного подождите")
         time.sleep(1)
         Show_all()
     elif(str_4=="add"):
        try:
            print("Отлично введите \n Сейчас будут по очереди выводиться характеристики объекта добавления\nчто будем добавлять(сорт):")
            str_prod=input("(сейчас введите на английском  и в последующем все что касается товаров на английском) тип добавляемого товара:")
            str_name=input("Введите название товара:")
            int_cost=int(input("Введите цену товара:"))
            print("добавление...")
            Add(str_prod,str_name,int_cost)
            time.sleep(1)
            print("Всё успешно добавилось")
            
        except BaseException:
           print("Произошла ошибка")   
        
        
           
           
           
     
     while(str_4!="exit"):
        
         print("Меню доступных команд было приведено выше, они еще доступны(если хотите то exit - для выхода)")
         
         str_4=input()
         if(str_4=="type"):
             print("Введи тип товара:")
             str_type=input()
             ReadPostrochno(str_type)
         elif(str_4=="datas"):
            print("Введи искомую дату в формате год месяц день аля:'xxxx-xx-xx'")
            str_find_date=input()
            ReadPostrochnoData(str_find_date)
         elif(str_4=="del"):
              del_str=input("Введи символы из неугодной записи, и данная строка будет удалена:")
              DeleteStr(del_str)
         elif(str_4=="sort"):
             Test()
         elif(str_4=="desc"):
             Test2()
         elif(str_4=="exit"):
             print("Всего хорошего!")
         elif(str_4=="showall"):
             print("загружаю.... немного подождите")
             time.sleep(1)
             Show_all()
         elif(str_4=="add"):
            try:
                print("Отлично введите \n Сейчас будут по очереди выводиться характеристики объекта добавления\nчто будем добавлять(сорт):")
                str_prod=input("(сейчас введите на английском  и в последующем все что касается товаров на английском) тип добавляемого товара:")
                str_name=input("Введите название товара:")
                int_cost=int(input("Введите цену товара:"))
                print("добавление...")
                Add(str_prod,str_name,int_cost)
                time.sleep(1)
                print("Всё успешно добавилось")
            
            except BaseException:
               print("Произошла ошибка")   
        
        
           
           