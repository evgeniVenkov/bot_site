import random


def task1():
    mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    num = int(input("Enter a number: "))

    sdvig = len(mass) - num
    sdvig = mass[sdvig:] + mass[:sdvig]
    print(sdvig)


def task2():
    num_rand = random.randint(1, 10000)
    num = num_rand
    while True:
        num_rand = num_rand / 10
        if num_rand < 10:
            print(int(num_rand))
            print(num)
            break


def task3():
    num = 0.00314567
    string = str(num)
    for i in string:
        if i.isdigit() and int(i) != 0:
            print("как видишь нет ошибки", i)
            break


def task4():
    num_rand = random.randint(1, 10000)
    num = num_rand

    num_rand = num_rand % 10
    print(num_rand)
    print(num)


def task6():
    num_rand = random.randint(1, 10000)
    right_num = num_rand % 10
    left_num = int(str(num_rand)[0])

    print(left_num)
    print(right_num)
    print(num_rand)
    print(left_num + right_num)


def task7():
    mass = [1, -2, 3, 4, -5, 6, 7, -8, 9, 10, -11, 12, 13, 14, 15]
    new_mass = [i for i in mass if i < 0]
    print(len(new_mass))


def task8():
    text = "Иногда достаточно просто остановиться. Не чтобы сдаться, а чтобы оглянуться. Мир не уходит вперёд без тебя — он ждёт, когда ты заметишь, как красиво свет падает сквозь листья, как тихо дышит утро, и как многое можно почувствовать, ничего не говоря."
    split = text.split(" ")
    count = 0
    mass_word = []
    for el in split:
        if el[0].lower() == "а":
            count += 1
            mass_word.append(el)

    print(count)
    print(mass_word)


def task9():
    text = '''
                text1
                text2
                text3
                text4
                text5
            '''
    mass= []
    for el in text.split('\n'):
        el = el.strip()
        if not el:
            continue
        mass.append(el)

    print(mass)
task9()
