# 2 этап 28/07

# работает
# тест пройден

import random

comp_choose = ('paper','rock','scissors')
cmp_ch = random.choice(comp_choose)
win = dict(rock='scissors', scissors='paper',paper='rock')
pl_ch = input() #'scissors'

def state():
    if pl_ch == cmp_ch:
        print("There is a draw ({cmp_ch})")
    elif win[pl_ch] == cmp_ch:
        print(f'Well done. Computer chose {cmp_ch} and failed')
    elif win[cmp_ch] == pl_ch:
        print(f'Sorry, but computer chose {cmp_ch}')

state()
    
