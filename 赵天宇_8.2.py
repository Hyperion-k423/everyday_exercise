# 列表的下标索引
my_list = [[1,2,3],[3,4,5]]
print(my_list[1][2])
list_2 = ["a","b","c"]
index = list_2.index("a")
print(f"list_2中,'a'的下标索引值是{index}")
list_2[0] = "f"
print(list_2[0])
list_2.insert(1,"g")
print(list_2)
list_2.append("h")
print(list_2)
list_3 = ["q","w","e"]
list_2.extend(list_3)
print(list_2)
del list_2[0]
print(list_2)
element = list_2.pop(0)
print(f"通过pop方法取出元素后列表内容为{list_2},取出的元素是{element}")
list_2.remove("e")
print(list_2)
list_2.clear()
print(list_2)
num = list_2.count("b")
print(num)
count = len(list_2)
print(count)

name = ["li","xiao","man"]
index = 0
while index < len(name):
    element = name[index]
    print(f"列表的第{index + 1}个元素：{element}")
    index += 1
for element in name :
    print(f"列表的元素有：{element}")