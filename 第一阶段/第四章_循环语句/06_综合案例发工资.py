# 公司账上余额10000元，一共20名员工，这月发工资，每名员工1000元，绩效取1~10，如果绩效小于等于5则没有工资，公司账上余额用完后面的员工就不发工资了
import random

rest = 10000
for x in range(1, 21):
    grade = random.randint(1, 10)
    if grade > 5:
        print(f"员工{x}绩效为:{grade},大于5，发给{x}号员工1000元")
        rest -= 1000
        print(f"公司现在余额:{rest}")

    else:
        print(f"员工{x}绩效为{grade},没有大于5，所以不发工资，下一个")
        continue
    if rest <= 0:
        print("钱发完了，下个月领取吧!")
        break
