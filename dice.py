import random
def rollDice(d,s):
    x = 0
    for i in range(d):
        x = x+random.randint(1,s)
    return x
q = rollDice(2,6)
print(q)
counter= 0
for i in range(1000):
    q = rollDice(2,6)
    if q == 7:
        counter+=1
print(counter/1000)
        
    