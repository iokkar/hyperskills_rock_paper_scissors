# development in progress 
# 05/08

# подготовка к проверке

import random

pl_ch = ''
pl_name = input('Enter your name: ')
print(f'Hello {pl_name}')
pl_names = {}

comp_choose = ['paper', 'rock', 'scissors']
cmp_ch = random.choice(comp_choose)
win = dict(rock='scissors', scissors='paper', paper='rock')
input_words = ('paper', 'rock', 'scissors', '!exit', '!rating')


def check_name(): # проверка имени перебором
    f_names = open("rating.txt","a+")
    for i in f_names:
        if i.startswith(pl_name):
            f_names.close()
            return
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

def read_names(): # считываю имена из файла в словарь  - работате
    f_names = open("rating.txt","r+")
    for i in f_names:
            pl_names[i[:i.index(' ')]] = int(i[i.index(' ')+1:])
    f_names.close()


def state():
    global pl_ch
    if pl_ch != '!exit' and pl_ch != '!rating':
        if pl_ch == cmp_ch:
            print(f"There is a draw ({cmp_ch})")
            pl_names[pl_name] += 50
        elif win[pl_ch] == cmp_ch:
            print(f'Well done. Computer chose {cmp_ch} and failed')
            pl_names[pl_name] += 100
        elif win[cmp_ch] == pl_ch:
            print(f'Sorry, but computer chose {cmp_ch}')
    else:
        return

def check_in():
    global pl_ch, cmp_ch
    while True:
        pl_ch = input() 
        if pl_ch not in input_words:
            print('Invalid input')
            return False
        else:
            cmp_ch = random.choice(comp_choose)
            return True
            
def main():
    read_names()
    check_name()
    while pl_ch != '!exit':
        if check_in():
            if pl_ch == '!rating':
                f_rating()
            state() 
        else:
            continue    
    else:
        print('Bye!')

main()

