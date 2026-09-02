def grade(s):
    if s >=90 and s <= 100:
        return "A"
    elif s >=80 and s <= 89:
        return "B"
    elif s >=70 and s <= 79:
        return "C"
    elif s >=60 and s <= 69:
        return "D"
    elif s >=0 and s<= 59:
        return "F"
    else:
        print("the number wasnt in the 0-100 range.")
print(grade(78))