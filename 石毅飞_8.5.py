def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda x,y:x+y)

f = open("D:/test.py","r",encoding="utf-8")
content = f.read()
count = content.count("itheima")
print(count)
f.close()


