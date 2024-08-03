#8.3-1
str="万过薪月，员序程马黑来，nohtyP学"
newstr=str[::-1][9:14]#将序列整体倒过来,后面数格数分割取得黑马程序员
print(f"输出倒序的结果：{newstr}")
newstr1=str.split("，")[1].replace("来"," ")[::-1]
print(f"输出结果{newstr1}")
#8.3-2
mylist=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
mylist1=set()
for element in mylist:
    mylist1.add(element)
print(f"循环遍历列表{mylist}")
print(f"存入集合后结果是{mylist1}")#集合元素自身不允许重复
#8.3-3
my_dict={
    "王力鸿":{
        "部门":"科技部",
        "工资":3000,
        "级别":1},
    "周杰轮":{
        "部门":"市场部",
        "工资":5000,
        "级别":2},
    "林俊节":{
        "部门":"市场部",
        "工资":7000,
        "级别":3},
    "张学油":{
        "部门":"科技部",
        "工资":4000,
        "级别":1},
    "刘德滑":{
        "部门":"市场部",
        "工资":6000,
        "级别":2}}
print(f"输出未变前的结果：{my_dict}")
for name in my_dict.keys():
    if my_dict[name]["级别"]==1:
        my_dict1=my_dict[name]
        my_dict1["级别"]=2#级别加1
        my_dict1["工资"]+=1000#修改内层循环
        my_dict[name]=my_dict1#将修改后的内层循环代替原先的内层循环
print(f"对员工升职加薪后的结果是：{my_dict}")














































































