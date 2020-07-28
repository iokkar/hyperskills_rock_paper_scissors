# 3 этап 28/07

# пройден тест

import random

comp_choose = ['paper', 'rock', 'scissors']
cmp_ch = random.choice(comp_choose)
win = dict(rock='scissors', scissors='paper', paper='rock')
input_words = ('paper', 'rock', 'scissors', '!exit')
pl_ch = ''

def state():
    global pl_ch
    if pl_ch != '!exit':
        if pl_ch == cmp_ch:
            print(f"There is a draw ({cmp_ch})")
        elif win[pl_ch] == cmp_ch:
            print(f'Well done. Computer chose {cmp_ch} and failed')
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
        else:
            cmp_ch = random.choice(comp_choose)
            return

def main():
    global pl_ch
    while pl_ch != '!exit':
        check_in()
        state()
    else:
        print('Bye!')


main()