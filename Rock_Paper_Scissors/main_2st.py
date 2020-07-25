# 2 этап 24/07

pl_choice = input()
option = ''

def check_win():
    global option
    if pl_choice == 'rock':
        option = 'paper'
    elif pl_choice == 'scissors':
        option = 'rock'
    elif pl_choice == 'paper':
        option = 'scissors'


check_win()
print(f'Sorry, but computer chose {option}')
