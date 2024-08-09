class phone:
    __is_5g_enable=False
    def __check_5g(self):
        if self.__is_5g_enable==False:
            print("5g关闭，使用4g网络")
        else:
            print("5g开启")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

p=phone()
p.call_by_5g()