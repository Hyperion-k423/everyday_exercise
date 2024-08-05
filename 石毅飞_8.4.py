my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdef"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
print(tuple(my_dict))
print(tuple(my_str))


def user_info(name,age,gender="男"):
    print(name,age,gender)
user_info("小飞",11,"女")
def use_info(**kwaegs):
    print(kwaegs)
use_info(name="小飞",age=19,id=100)

def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return x+y
test_func(compute)
