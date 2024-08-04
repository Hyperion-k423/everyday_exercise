def a(compute):
    b=compute(1,2)
    print(b)
    print(type(compute))

def compute(x,y):
    return x+y

a(compute)
