my_dict = {"地址": "安阳", "姓名": "赵阳", "年龄:": 17}
empty_dict = dict()
# empty_dict = {}

my_dict = {"地址": "安阳", "姓名": "赵阳", "年龄:": 17, "地址": "安阳"}
print(my_dict)

print(my_dict.get("地址"))
print(my_dict["地址"])

stu_score_set = {
    "赵四": {
        "数学": 66,
        "英语": 77,
        "语文": 88,
    },
    "王五": {
        "数学": 13,
        "英语": 14,
        "语文": 15,
    }
}
print(stu_score_set)

# 赵四的数学成绩
print(stu_score_set["赵四"]["数学"])

# 字典添加和更新
print(stu_score_set)
stu_score_set["赵四"] = {"数学": 88, "英语": 77, "语文": 88}
print(stu_score_set)
stu_score_set["张三"] = {"数学": 88, "英语": 77, "语文": 88}
print(stu_score_set)
# 删除
value = stu_score_set.pop("赵四")
print(f"删除的元素key:'赵四'，value:{value}")
# del stu_score_set["赵四"]
print(stu_score_set)
# 获取全部key
keys = stu_score_set.keys()
print(keys)
# 遍历
for key in keys:
    print(stu_score_set[key])
for element in stu_score_set:
    print(f"key:{element}")
    print(f"value:{stu_score_set[element]}")
# 统计字典元素个数
print(len(stu_score_set))
# 清空
stu_score_set.clear()
print(stu_score_set)
# 练习题
staff_info = {
    "王力宏": {
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
    }
}
print(f"原职工信息：{staff_info}")
for key in staff_info:
    if staff_info[key]["级别"] == 1:
        staff_info[key]["级别"] += 1
        staff_info[key]["工资"] += 1000
print(f"现职工信息,涨级别，薪资后：{staff_info}")