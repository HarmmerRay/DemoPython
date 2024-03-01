import re

s = 'python itheima python itheima python itheima python'
result = re.match('python', s)
print(result)
print(result.span())
print(result.group())

s = '1python itheima python itheima python itheima python'

result = re.match('python', s)
print(result)