

mass = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

num = int(input("Enter a number: "))


sdvig = len(mass)-num
sdvig = mass[sdvig:] + mass[:sdvig]
print(sdvig)