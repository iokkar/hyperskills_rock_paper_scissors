# development in progress 
# 01/08
# добавлено поиск в файле и вывод очков
# добавляет нового польльзователя, но выводит неправильно, нужна проверка

# нужно добавить:
# добавление дового игрока в файл
# изменение очков для игрока после каждого раунда игры

# (по умолчанию выводится до 3 цифр, но возможно нужно сделать проверку
# через len, до пробела посчитать кол-во симовол и только потом распечатать)


pl_ch = ''
pl_name = input('Enter your name: ')
print(f'Hello {pl_name}')

def check_name(): # проверка имени перебором
    f_names = open("rating.txt","a+")
    for i in f_names:
        if i.startswith(pl_name):
            f_names.close()
            return
    f_names.write('\n'+ pl_name + ' 0')
    f_names.close()
    return

def ch_name(): # короткая версия
    f_names = open("rating.txt","a+")
    if pl_name not in f_names: # добавление имени нового игрока
        f_names.write('\n'+ pl_name + ' 0')
    f_names.close()

def find_rating():
    f_names = open("rating.txt","r+")
    for name in f_names:
        if pl_name in name:
            print(pl_name, name[name.index(' ')+1:].replace('\n',''))
            f_names.close()
            break
    f_names.close()

ch_name()
while pl_ch != '!exit':
    pl_ch = input()
    if pl_ch == '!rating':
        find_rating()
    #check_in()
    #state()
else:
    print('Bye!')

