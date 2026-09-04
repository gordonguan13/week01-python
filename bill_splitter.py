b = int(input("bill:"))
t = int(input("tip percent"))
p = int(input("how many people?"))
t=t/100
bb=b*t
print("Total:",bb+b)
print("Total split per person:",(bb+b)/p)