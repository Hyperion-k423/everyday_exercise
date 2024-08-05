#1
f=open("D:\wenben\word.txt","r",encoding='UTF-8')
with open("D:\wenben\word.txt","r",encoding='UTF-8') as f:
    string=f.read()
    count=string.count("itheima")
print(f"文件内容为：\n{string}\n其中，itheima有{count}个")
#2
t=open("D:\wenben\\bill.txt","r",encoding='UTF-8')
bak=open("D:\wenben\\bill.txt.bak","w",encoding='UTF-8')
for l in t:
    l=l.strip()
    lin=l.split(",")
    if lin[4]!="测试":
        print(f"{lin}")
        bak.write(l)
        bak.write("\n")

bak.close()
t.close()