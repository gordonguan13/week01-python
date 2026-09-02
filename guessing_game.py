import random
num=random.randint(1,100)
finished = False
tries = 0
def calculate(guess, num):
    if int(guess) != num:
        if int(guess) > num:
            return "high"
        else:
            return "low"
def getguess():
    a = True
    while a:
        try:
            return int(input("What number?"))
            a = False
        except ValueError:
            print("thats not a number.")
print(num)

while finished == False:
    g=getguess()
    if g == num:
        tries += 1
        print("You got it!") 
        finished = True
        print("Tries:", tries)
    else:
        print("Incorrect number. Too", calculate(g, num))
        tries += 1 