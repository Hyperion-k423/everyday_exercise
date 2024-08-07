"""
                    文件操作
"""
import time

#文件编码:将内容翻译成二进制使计算机读懂，编码规则常用UTF—8
#文件操作
    #打开文件：open(name,mode,encoding)
        #name: 是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
        #mode：设置打开问价的模式（访问模式）：只读、写入、追加等。
        #encoding：编码格式（推荐使用UTF-8）
        #示例：f = open('python.txt','r',encoding = " UTF-8")   (其实open()函数的第三位参数不是encoding，所以必须是关键名encoding = "")
f = open("C:\\Users\\DELL\\Desktop\\gitcode\\hello.txt","r",encoding="UTF-8")  #复制完文件地址后，要把\全部改为\\
print(type(f))
    #读取文件 - read()
print(f"读取10个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果：{f.read()}")   #这次读文件是接着上一次读的末尾接着读
    #读取文件 - readlines()
lines = f.readlines()   #读取文件的全部行，封装到列表中
print(f"lines对象的类型是：{type(lines)}")
print(f"lines对象的内容是：{lines}")   #因为上一次read()已经读完了，所以这一次读的内容是空
    #读取文件 - readline()方法
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}")
print(f"第三行的数据是：{line3}")
    #for循环读取文件
for line in f:
    print(f"每一行的数据是：{line}")
    #关闭文件 - close()方法
f.close()
        #或者time.sleep(500000)   程序睡眠500000秒
with open("C:\\Users\\DELL\\Desktop\\gitcode\\hello.txt","r",encoding="UTF-8") as f:
     for line in f:
        print(f"{line}")
#time.sleep(500000)
        #with open()会自动关闭文件


#文件的写出操作
    # 打开一个不存在的文件
f = open("D:\\TEST.txt","w",encoding="UTF-8")
f.write("hello word")       #内容写入到内存中
#f.flush()                       #文件写入到硬盘中
f.close()                       #close方法，内置了flush功能
    #打开一个存在的文件,会清空文件里原有的内容，然后输入新内容
f = open("D:\\TEST.txt","w",encoding="UTF-8")
f.write("李小满")
f.close()


#文件追加操作
    #打开一个不存在的文件
f = open("D:\\TEST1.txt","a",encoding="UTF-8")
f.write("李小满")
f.close()
    #打开一个已经存在的文件
f = open("D:\\TEST1.txt","a",encoding="UTF-8")
f.write("w10")
f.close()
    #每打开一次"李小满w10"就会在文件中出现一次

# 8-5 文件备份
