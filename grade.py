s=int(input("whats ur score? "))
if s >=90 and s <= 100:
    print("you got an A")
elif s >=80 and s <= 89:
    print("you got a B")
elif s >=70 and s <= 79:
    print("you got a C")
elif s >=60 and s <= 69:
    print("you got a D")
elif s >0 and s<= 59:
    print("you got a F")
else:
    print("the number wasnt in the 0-100 range.")