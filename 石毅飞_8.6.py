def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda x,y:x+y)

f = open("D:/test.py","r",encoding="utf-8")
content = f.read()
count = content.count("itheima")
print(count)
f.close()

import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

