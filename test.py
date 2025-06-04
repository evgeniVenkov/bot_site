import random
def task1():
    mass = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    num = int(input("Enter a number: "))


    sdvig = len(mass)-num
    sdvig = mass[sdvig:] + mass[:sdvig]
    print(sdvig)

def task2():
    num_rand = random.randint(1,10000)
    num = num_rand
    while True:
        num_rand = num_rand /10
        if num_rand < 10:
            print(int(num_rand))
            print(num)
            break


task2()