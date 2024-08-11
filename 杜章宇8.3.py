my_str = "万过薪月，员序程马黑来，nohtyP学"
new_str = my_str[9:4:-1]
print(f"{new_str}")


my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast',]
niuniu = set()
for x in my_list:
    niuniu.add(x)
print(f"集合为：{niuniu}")



my_dir = {"王力宏": {
    "部门": "科技部",
    "工资": 3000,
    "级别": 1
}, "周杰伦": {
    "部门": "市场部",
    "工资": 5000,
    "级别": 2
}, "林俊杰": {
    "部门": "市场部",
    "工资": 7000,
    "级别": 3
}, "张学友": {
    "部门": "科技部",
    "工资": 4000,
    "级别": 1
}, "刘德华": {
    "部门": "市场部",
    "工资": 6000,
    "级别": 2
}}
print(f"全体员工信息如下：{my_dir}")
for name in my_dir:
    if my_dir[name]["级别"] == 1:
        my_dir[name]["级别"] = 2
        my_dir[name]["工资"] += 1000

print(f"调整后全体员工信息为：{my_dir}")
