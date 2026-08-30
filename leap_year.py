y = int(input("year: "))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("that is a leap year")
        else:
            print("not a leap year")
    else:
        print("thats a leap year")
else:
    print("not a leap year")

