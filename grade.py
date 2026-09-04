def letter_grade(s):
    if s >=90 and s <= 100:
        return "A"
    elif s >=80:
        return "B"
    elif s >=70:
        return "C"
    elif s >=60:
        return "D"
    elif s >=0:
        return "F"
    else:
        return "the number wasnt in the 0-100 range."
print(letter_grade(78))