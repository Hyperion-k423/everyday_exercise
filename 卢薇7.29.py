"""
print("hi",end='')
print("ni")

print("q w")
print("qqqqqqqq w")
print("q\tw")
print("qqq\tw")
print("qqqq\tw")
"""
x=1
z=0
while x<10:
    y=1
    while y<=x:
        z=y*x
        print(f"{y}*{x}={z}\t",end='')
        y+=1
    x+=1
    print()