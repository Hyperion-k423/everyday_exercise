#8.7
#主文件
import my_utils.str_util
from my_utils import file_util
print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima",0,4))
file_util.append_to_file("D:/test_append.txt","itheima")
file_util.print_file_info("D:/test_append.txt")
#st_util.py
"""
字符串相关的工具模块
"""
def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s: 被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]#序列切片语法完成反转从后向前反着取s[序列开始:序列结尾:步长]


def substr(s,x,y):
    """
        功能是按照给定的下标完成给定字符串切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]
if __name__=='__main__':
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员",1,3))
#file_util.py
"""
文件处理相关的模块
"""
def print_file_info(file_name):
    """
    功能是：将给定路径的文件内容输出到控制台中
    :param file_name:即将读取的文件路径
    :return:
    """
    f=None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是{e}")
    finally:
        if f:#如果变量是None，表示False,如果是任何内容，表示Ture
            f.close()

def append_to_file(file_name, data):
    """
    功能：将指定的数据追加到指定的文件中
    :param file_name: 指定的文件路径
    :param data:指定的数据
    :return: None
    """
    f=open(file_name, 'a', encoding='utf-8')
    f.write(data)
    f.write("\n")
    f.close()
if __name__ == '__main__':
    print_file_info('D:/bill.txtxxx')
    append_to_file("D:/test_append.txt","传智教育")