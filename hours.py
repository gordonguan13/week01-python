hours=int(input("how many hours? "))
rate=int(input("at what rate?"))
pay=0
if hours > 40:
    hours -= 40
    pay= 40*rate
    rate=rate*1.5
    pay+= rate*hours
else:
    pay=rate*hours
print("Pay:", pay)