#8.5-1
f=open("C:/word.txt","r",encoding="utf-8")
count=0
for line in f:
    print(f"读取每一行数据：{line}")#读取每一行的内容
    line=line.strip()#消除首尾空格以及字符串内部空格
    i=line.split(" ")#空格切分每一个单词
    print(f"输出分隔后的结果{i}")
    i.count("itheima")
    count=count+1
print(f"输出统计itheima的个数有:{count}")
f.close()
gr=open("C:/bill.txt","r",encoding="utf-8")
gw=open("C:/bill.txt.back","w",encoding="utf-8")
for line in gr:
    line=line.strip()
    if line.split(",")[4]=="测试":
        continue
    gw.write(line)
    gw.write("\n")
gr.close()
gw.close()



























































