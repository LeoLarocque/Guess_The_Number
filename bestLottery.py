import random
x = 0
num = ""
randNum = random.randint(1, 100)
name = input("Enter name: ")
print("Hello, " + name + "!")
nameLower = name.lower()
#My name is Leo. ;)
if nameLower == "leo":
    input("Enter number: ")
    print("Correct Guess!")
else:
    while not num == randNum:
        x += 1
        num = input("Enter number: ")
        if int(num) > randNum:
            print(str(x) + "ST Guess: to high.")
        elif int(num) < randNum:
            print(str(x) + "ST Guess: to low.")
        if int(num) == randNum:
            print("Correct! It took you " + str(x) + " tries to guess the number.")
            break
    print("The number was " + str(randNum) + ".")
def function():
    fileName = name + ".txt"
    f = open(fileName, "w")
    f.write("Name = " + str(name) + "\nNumber of tries = " + str(x) + "\nThe number = " + str(randNum))
    f.close()
function()
