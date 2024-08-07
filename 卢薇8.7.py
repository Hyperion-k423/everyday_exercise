import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima",0,4))

file_util.append_to_file("D:/test_append.txt","itheima")
file_util.print_file_info("D:/test_append.txt")

def str_reverse(s):
    """
    将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]
def substr(s,x,y):
    """
    完成切片
    :param s:即将被切片的字符串
    :param x:切片的开始下标
    :param y:切片完成后的下标
    :return:切片完成后的字符串
    """
    return s[x:y]
if __name__ == '__main__':
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员",1,3))
def print_file_info(file_name):
    """
    文件输出到服务台
    :param file_name:即将读取的文件路径
    :return: None
    """
    f=None
    try:
        f=open(file_name,"r",encoding="UTF-8")
        content=f.read()
        print("文件全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序异常，原因是：{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name,data):
    f=open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.close()

if __name__ == '__main__':
    append_to_file("D:/test_append.txt","黑马程序员得得得")


if __name__ == '__main__':
    print_file_info("D:/bill.txt.a")
