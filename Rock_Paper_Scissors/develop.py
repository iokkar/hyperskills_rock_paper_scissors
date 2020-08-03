# development in progress 
# 03/08
# добавлено поиск в файле и вывод очков
# добавляет нового польльзователя, но выводит неправильно, нужна проверка
# добавил считывание из файла в словарь
# провека и добавление нового игрока в словарь, а не в файл

# нужно добавить:
# добавление нового игрока в файл
# не нужно добавлять нового игрока в файл, пока добавляем его в словарь с игроками!!!
# изменение очков для игрока после каждого раунда игры


# проверка добавленных игроков в словаре
# 

pl_ch = ''
pl_name = input('Enter your name: ')
print(f'Hello {pl_name}')
pl_names = {}


# есть проблема с добавлением 
def check_name(): # проверка имени перебором
    f_names = open("rating.txt","a+")
    for i in f_names:
        if i.startswith(pl_name):
            f_names.close()
            return
    #f_names.write('\n'+ pl_name + ' 0') - запись имени в файл
    pl_names[pl_name] = 0
    f_names.close()
    return

def ch_name(): # короткая версия
    f_names = open("rating.txt","a+")
    if pl_name not in f_names: # добавление имени нового игрока
        f_names.write('\n'+ pl_name + ' 0')
    f_names.close()

def f_rating(): # поиск в словаре
    if pl_name in pl_names:
        print(pl_name, pl_names[pl_name])
        return


def find_rating(): #поиск в файле
    f_names = open("rating.txt","r+")
    for name in f_names:
        if pl_name in name:
            print(pl_name, name[name.index(' ')+1:].replace('\n',''))
            f_names.close()
            break
    f_names.close()

def read_names(): # считываю имена из файла в словарь  - работате
    f_names = open("rating.txt","r+")
    for i in f_names:
            pl_names[i[:i.index(' ')]] = int(i[i.index(' ')+1:])
    f_names.close()

read_names()
check_name()
while pl_ch != '!exit':
    pl_ch = input()
    if pl_ch == '!rating':
        f_rating()
        #find_rating()
    #check_in()
    #state()
else:
    for i in pl_names: # тест 
        print(i, pl_names[i])
    print('Bye!')

