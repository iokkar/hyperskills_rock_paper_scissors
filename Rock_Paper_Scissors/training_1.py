
animals_file = open('animals.txt', 'r', encoding='utf-8')
animals_new_file = open('animal_new.txt', 'w', encoding='utf-8')
animals_list = [i.replace('\n','') for i in animals_file]
for animal in animals_list:
    animals_new_file.write(animal + ' ')
animals_file.close()
animals_new_file.close()


input_file = open('input.txt', 'w', encoding='utf-8')
input_string = input_file.write(input())
input_file.close()

f_name = open("test.txt","w")
my_string = "A string to be written to a file!"
print(my_string, file=f_name)
f_name.close()

# проверка в кортеже (имитирует файл) наличия имени

str = ('Tim 500','Dim 0')
name = 'Nina'

def check_name():
    global str
    for i in str:
        if i.startswith(name):
            return
    str = str + (name + ' 0',)

def check():
    for i in str:
        if i.startswith(name):
            print(name, i[i.index(' ')+1:])
            return

check_name()
check()

# срезы

str = ('Tim 500','Dim 0')
name = 'Nina'
names = {}
print(str[0][:str[0].rfind(' ')])
print(str[0][str[0].index(' ')+1:])
b = int(str[0][str[0].index(' ')+1:])
a = str[0][:str[0].rfind(' ')+1].replace(' ','')
#for i in str:
 #   names[i[]]
names[a] = b