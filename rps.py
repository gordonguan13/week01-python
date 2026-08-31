import random
m = str(input("what do u want to play? (r/p/s)"))
def comp():
    return random.choice(["r", "p", "s"])
computer= comp()
if m == computer:
    print("tie")
elif m == "r" and computer == "p":
    print("you lose")
elif m == "r" and computer == "s":
    print("you win")
elif m == "p" and computer == "r":
    print("you win")
elif m == "s" and computer == "p":
    print("you win")
else:
    print("you lose")