# class Phone:
#     __current_voltage = 0
#
#     def __keep_single_core(self):
#         print("CPU切换为单核模式运行")
#
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print("5G通话已经开启")
#         else:
#             self.__keep_single_core()
#             print("电量不足5G，通话无法进行")
# phone = Phone()
# # phone.__keep_single_core()
# # print(phone.__current_voltage)
# phone.call_by_5g()

class Phone:
    __is_5g_enable = False

    def __init__(self, __is_5g_enable):
       self.__is_5g_enable = __is_5g_enable

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")

    def call_by_5G(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone(True)
phone.call_by_5G()
