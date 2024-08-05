my_str = "万过薪月，员序程马黑来，nohtyP学"
str = my_str[::-1][9:14:]
print(str)
str = my_str[5:10:][::-1]
print(str)
str = my_str.split("，")[1].replace("来","")[::-1]
print(str)


my_list = ["黑马程序员","传智播客","itheima","itcast","best","黑马程序员","传智播客","itheima","itcast"]
my_ste = set()
for i in my_list:
    my_ste.add(i)
print(my_ste)


info_dict = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友":{
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华":{
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
for name in info_dict:
    if info_dict[name]["级别"]==1:
        e_info_dict = info_dict[name]
        e_info_dict["级别"]+=1
        e_info_dict["工资"]+=1000
        info_dict[name]=e_info_dict
print(info_dict)