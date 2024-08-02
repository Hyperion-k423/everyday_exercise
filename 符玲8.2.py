#8.2-1
mylist=[21,25,21,23,22,20]
print(f"输出列表所有元素：{mylist}")
mylist.append(31)#追加一个数字到末尾
print(f"输出追加后总的列表元素：{mylist}")
mylist.extend([29,33,30])#追加一个新列表到末尾
print(f"输出追加新列表后所有元素总和：{mylist}")
print(mylist[0])#取出下标为0的元素，也就是21
print(mylist[-1])#取出最后一个元素，也就是30
index=mylist.index(31)#查找元素31在列表中的下标引值
print(f"31在列表中的下标引值是：{index}")
print(f"列表最后的元素内容是：{mylist}")
#8.2-2
def list_while():
    list1=[1,2,3,4,5,6,7,8,9,10]
    list2=[]
    index=0
    while index<len(list1):
        num=list1[index]#将列表list1的每个数字依次赋值给num
        index+=1
        if num%2==0:
            list2.append(num)#将满足条件的数字（偶数）放入list2列表中
        else:
            continue
    print(f"输出偶数列表元素{list2}")
list_while()
def list_for():
    list1=[1,2,3,4,5,6,7,8,9,10]
    list3=[]
    for index in list1:
        if index%2==0:
            list3.append(index)#将满足条件的数字放入list3中
    print(f"输出偶数列表元素{list3}")
list_for()
#8.2-3
t1=('周杰伦',11,['football','music'])
index=t1.index(11)
print(f"查询年龄所在下标位置是：{index}")
num=t1[0]#输出元组第0个元素，即学生姓名
print(f"学生的姓名是：{num}")
del t1[2][0]#删除下标所代表的football元素
t1[2].insert(0,'cooding')#在所在[2][0]位置加入coding
print(f"重新输出元组内容：{t1}")
"""
列表.append（元素）向列表中追加一个元素
列表.extend(容器）将数据容器的内容依次取出，追加到列表尾部
列表.remove（元素)从前向后，删除此元素第一个匹配项
列表.clear()清空列表
列表.pop(下标）删除列表指定项目
"""
#8.2-4
str="itheima itcast boxuegu"
num=str.count('it')#字符串.count（字符串1）统计字符串内字符串1的出现次数
print(f"字符串itheima itcast boxuegu中有:it{num}个字符")
newstr=str.replace(" ",'|')#字符串.replace（字符串1，字符串2）是将字符串1全部替换成字符串2
print(f"字符串itheima itcast boxuegu,被替换空格后，结果：{newstr}")
newstr1=newstr.split("|")#按照给定字符串给给字符串分隔
print(f"字符串itheima itcast boxuegu,按照|分隔后，得到：{newstr1}")
"""
字符串[下标] 根据下标检索取出特定位置字符
len（字符串） 统计字符串的字符个数
字符串.strip()移除首尾空格和换行符
"""































































