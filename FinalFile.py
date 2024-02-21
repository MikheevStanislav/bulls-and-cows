import time



def read_guess():
    while True:
        print("Введите число")
        a = input()
        if a.startswith("exit"):
            print("Ариведерчи")
            exit(0)
        if a.startswith("guess "):
            a = a[6:]
        a = a.strip()
        if not len(a) == 4:
            print("Слишком много символов")
            break
        if not len(set(a)) == 4:
            print("Повторяются символы")
            break
        if not a.isdigit():
            print("В введенном тескте есть не цифры")
            break
        return a


# а m и с константы, которые позволяют нам получать рандомные цифры#
# Х есть рандомные цифры#
#первый икс - время запуска программы#
x = round(time.time())
def rand():
    global x
    x = (211 * x + 1663) % 7875
    return x % 10


# собираем в конструктор#
def generate_secret():
    a = str(rand())
    b = str(rand())
    c = str(rand())
    d = str(rand())
    s = a + b + c + d

    return s


# проверка#
'''
i =0
while i != 10000:
    l = generate_secret()
    if(l[0] == l[1] or l[0] == l[2] or l[0] == l[3] or l[1] == l[2] or l[1] == l[3] or l[2] == l[3]):
        print("!")
        break


    
    i = i + 1
'''
# генерим строку с рандомными цифрами, затем в цикле считываем преположение игрока#
while True:
    k = str(generate_secret())
    while True:
        sr = str(read_guess())
        #счетчик быков#
        countB = 0
        #счетчик коров#
        countK = 0
        #счетчик для цикла подсчета быков и коров#
        i = 0
        while i != 4:
            if (sr[i] == k[i]):
                countB = countB + 1
            if sr[i] in k: countK = countK + 1
            i = i + 1
        #заметим что коровы у нас включают быков по по нашему методу, так что вычитаем из коров быков#
        countK = countK - countB
        #условие победы#
        if countB == 4:
            print("ПОБЕДА!")
            break
        #условие поражения#
        else:
            print("Быки", countB)
            print("Коровы", countK)
            continue
