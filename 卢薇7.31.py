ey=5000000
name=None
name=input("xingming?")
def chaxun(show_header):
    print("------cha-----")
    print(f"{name},yue:{money}")
def cunkuan(num):
    global money
    money+=num
    print("-----cun-----")
    print(f"{name},cunkuan{num},yue{money}")
    chaxun(False)
def quqian(num):
    global money
    money -= num
    print("-----qu-----")
    print(f"{name},qukuan{num},yue{money}")
    chaxun(False)
def main():
    print("----zhu------")
    print(f"{name},hanying!")
    print("chaxun\t\t:1")
    print("cunkuan\t\t:2")
    print("qukuan\t\t:3")
    print("tuichu\t\t:4")
    return input("xuanzeshi?")
while True:
    jianpanshuru=main()
    if jianpanshuru=="1":
        chaxun(True)
        continue
    elif jianpanshuru=="2":
        num=int(input("cunqian?"))
        cunkuan(num)
        continue
    elif jianpanshuru=="3":
        num=int(input("qukuanwei?"))
        quqian(num)
        continue
    else:
        print("tichu")
        break




