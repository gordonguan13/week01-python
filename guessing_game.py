import random
best = None
def getdifficulty():
    choice=''
    while choice not in ["easy", "medium", "hard"]:
        choice = input("difficulty (easy,medium,hard)? ")
    if choice == 'easy':
        return 50
    elif choice == 'medium':
        return 100
    else:
        return 1000  
def calculate(guess, num):
    if guess > num:
        return "high"
    else:
        return "low"
def getguess():
    while True:
        try:
            return int(input("What number? "))
        except ValueError:
            print("thats not a number.")
def tryagain():
    ttt = ''
    while ttt not in ["y","n"]:
        ttt = input("Would you like to play again? (y or n)")
    if ttt == "n":
        return True
    else:
        return False

        

finish = False
while finish == False:
    difficulty=getdifficulty()
    num=random.randint(1,difficulty)
    complete = False
    tries = 0
    print(num)
    while complete == False:
        g=getguess()
        if g == num:
            tries += 1
            print("You got it!") 
            complete = True
            print("Tries:", tries)
            if best is None or tries < best:
                best = tries
            print("Best tries so far:", best)
            finish = tryagain()
        else:
            print("Incorrect number. Too", calculate(g, num))
            tries += 1
    # best tries