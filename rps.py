import random
m = str(input("what do u want to play? (r/p/s)"))
def comp():
    return random.choice(["r", "p", "s"])
computer= comp()
def winner(s, computer):
    if s == computer:
        return "tied"
    elif s == "r" and computer == "s":
        return "you won"
    elif s == "p" and computer == "r":
        return "you won"
    elif s == "s" and computer == "p":
        return "you won"
    elif s not in ["r","p","s"]:
        return "thats not a move you idiot"
    else:
        return "you lost"
print(winner(m,computer))