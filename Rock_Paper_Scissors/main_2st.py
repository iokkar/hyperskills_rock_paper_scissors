# 2 этап 27/07

#Сегодня hyperskill лежит, написал задание по памяти, возможно не точно
#в таком виде работае, нужно уточнять 
# задание и условия когда сайт поднимут

import random

comp_choose = ('paper','rock','scissors')
cmp_ch = random.choice(comp_choose)
win = dict(rock='scissors', scissors='paper',paper='rock')
pl_ch = input() #'scissors'

def state():
    if pl_ch == cmp_ch:
        print("Draw")
    elif win[pl_ch] == cmp_ch:
        print('Player win')
    elif win[cmp_ch] == pl_ch:
        print('Computer win')

state()
    
