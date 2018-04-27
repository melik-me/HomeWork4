# Задание 1. Со значениями по умолчанию
#
# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По
# умолчанию 3
# 3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!». По умолчанию 0

def naughty_boy(strings=3, nla=3, exclamation=0):
    string = ['la' for i in range(nla)]

    if exclamation:
        end_string = '!\n'
    else:
        end_string = '.\n'

    strings -= 1

    s = ("-".join(string) + "\n") * strings
    s += "-".join(string) + end_string
    return s


n = int(input('Please enter quantity of "la" in our song:\n'))
number = int(input('Please enter quantity of strings in our song:\n'))
ex = int(input('Please enter 1 if you need exclamation (otherwise string will end with a dot):\n'))

song = naughty_boy(n, number, ex)
print(song)