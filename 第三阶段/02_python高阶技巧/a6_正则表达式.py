import re

s = 'python itheima python itheima python itheima python'
result = re.match('python', s)
print(result)
print(result.span())
print(result.group())

s = '1python2 3itheima4 5python7 itheima 1000p***ython ###itheima python'
# 从头匹配
result = re.match('python', s)
print(result)
# 搜索匹配
result = re.search('python', s)
print(result)
# findall 搜索全部匹配
result = re.findall('python', s)
print(result)

# 元字符匹配
# 我一直认为从事脑力劳动，这种思考的活动，完全可以做到体力劳动者做不到的，劳动14个小时甚至更久，并且是越用越强。 从此观点上看，自己美好的生活令我十分的
# 宽慰畅心，并且可以开心的同时创造更多的价值产出，充实我的人生，追逐我的梦想。
# 找出第一个数字
result = re.search(r"\d", s)
print(result)
# 找出特殊字符
result = re.findall(r"\W", s)
print(result)
# 找出全部英文字母
result = re.findall(r"[a-zA-Z]", s)
print(result)

# 案例练习
# 邮箱
result = r"(^[\w-]+(\.[\w-]+)*@(qq|com|gmail)(\.[\w-]+)+$)"
s = 'a.b.c.d.e.f.g@qq.com.a.z.q.d.e'
print(re.findall(result, s))

