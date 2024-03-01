import time
import threading


# # target参数的作用，传递处理函数
# def sing():
#     while (True):
#         print("我在唱歌，啦啦啦~~")
#         time.sleep(1)
#
#
# def dance():
#     while (True):
#         print("我在跳舞，呱呱呱~~")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     thread1 = threading.Thread(target=sing)
#     thread2 = threading.Thread(target=dance)
#
#     thread1.start()
#     thread2.start()

# args的作用，给处理函数穿参数
def sing(msg):
    while (True):
        print(msg)
        time.sleep(1)


def dance(msg):
    while (True):
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    thread1 = threading.Thread(target=sing, args=("我在唱歌，啦啦啦~~",))
    thread2 = threading.Thread(target=dance, args=("我在跳舞，哈哈哈~~~",))

    thread1.start()
    thread2.start()
