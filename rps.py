c = "s"
m = str(input("what do u choose? (r/p/s) "))
if m not in ["r", "p", "s"]:
    print("thats invalid")
else:
    if m == "r":
        print("u win")
    elif m == "p":
        print("u lose")
    else:
        print("tie")
