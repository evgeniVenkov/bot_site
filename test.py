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
    mass = []
    for el in text.split('\n'):
        el = el.strip()
        if not el:
            continue
        mass.append(el)

    print(mass)


def task10():
    dct = {
        1: {
            1: {
                1: 111,
                2: 112,
                3: 113,
            },
            2: {
                1: 121,
                2: 122,
                3: 123,
            },
        },
        2: {
            1: {
                1: 211,
                2: 212,
                3: 213,
            },
            2: {
                1: 221,
                2: 222,
                3: 223,
            },
        },
        3: {
            1: {
                1: 311,
                2: 312,
                3: 313,
            },
            2: {
                1: 321,
                2: 322,
                3: 323,
            },
        },
    }
    count = 0
    for el in dct.values():
        for i in el.values():
            for j in i.values():
                count += int(j)
    print(count)


def task11():
    for i in range(10, 1000):
        st = str(i)
        num = int(st[-2])
        if num % 2 == 0:
            print(i)


def task12():
    mass = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    for m in mass:
        for el in m:
            print(el)
    print("---------------------")
    for el in [item for sub in mass for item in sub]:
        print(el)


def task13():
    lst = [
        {
            1: 11,
            2: 12,
            3: 13,
        },
        {
            1: 21,
            2: 22,
            3: 23,
        },
        {
            1: 24,
            2: 25,
            3: 26,
        },
    ]
    # count = 0
    # for el in lst:
    #     for i in el.values():
    #         count += int(i)
    count = sum(el for dict in lst for el in dict.values())
    print(count)


def task14():
    lst = [47, 80, 13, 5, 91, 36, 64, 78, 20, 509, 26, 88, 31, 707, 19, 95, 43, 11, 69, 54]
    new_mas = []
    # for el in lst:
    #     for i in str(el):
    #         if i == "0":
    #             new_mas.append(el)
    #             break
    nem_mass = [el for el in lst for i in str(el) if i == "0"]
    print(nem_mass)


def task15():
    lst = [
        'text1',
        'text2',
        'text3',
        'text4',
        'text5',
    ]
    st = "\n".join(lst)
    print(st)


def task16():
    mass = []
    for i in range(3):
        ms = []
        for e in range(3):
            ms.append("x")
        mass.append(ms)
    
    print(mass)


def task17():
    text = '''
            text1
            text2
            
            text3
            text4
            
            text5
        '''
    mass_text = text.splitlines()
    # mass = []
    # for el in mass_text:
    #     if not el or el == '\t':
    #         continue
    #     mass.append(el)
    mass = [el for el in mass_text if not el or el != '\t']
    new_text = '\n'.join(mass)

    print(new_text)


def filter_unique_words(answer_list: str) -> str:
    counts = {}
    mass = answer_list.split(' ')
    for word in mass:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    uniq_w = [word for word in mass if counts[word] == 1]
    if len(uniq_w) == 0:
        return -1
    return " ".join(uniq_w)


answer_list = input()
unique_words = filter_unique_words(answer_list)
print(unique_words)

task17()
