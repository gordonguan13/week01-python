def faren(c):
    return (c-32) * 5/9
def celc(f):
    return f * 9/5 + 32
print(faren(100))
print(celc(32))
print(faren(celc(50)))