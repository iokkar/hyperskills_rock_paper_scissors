# development in progress 
# 31/07
# добавлено поиск в файле и вывод очков

# нужно добавить:
# добавление дового игрока в файл
# изменение очков для игрока после каждого раунда игры


pl_ch = ''
pl_name = input('Enter your name: ')
print(f'Hello {pl_name}')

def find_rating():
    f_names = open("rating.txt","r+")
    for name in f_names:
        if pl_name in name:
            print(name[-4:].replace('\n',''))
    f_names.close()

while pl_ch != '!exit':
    pl_ch = input()
    if pl_ch == '!rating':
        find_rating()
    #check_in()
    #state()
else:
    print('Bye!')

