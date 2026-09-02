done=False
c=0
t=0
while done == False:
    f = input("number: ")
    if f == "done":
        done = True
    else:
        try:
            t+=int(f)
            c+=1
        except ValueError:
            print("error, try again.")
try:
    print("average: ", t/c)
except ZeroDivisionError:
    print("divided by zero, re run the script.")
