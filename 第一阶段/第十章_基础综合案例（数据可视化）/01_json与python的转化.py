import json

data = [{"name": "老王", "gender": "男"}, {"name": "老赵", "gender": "男"}]
data_json = json.dumps(data, ensure_ascii=False)  # 不使用ascii码表转换字符，直接显示字符
print(data_json)
print(type(data_json))
data_python = json.loads(data_json)
print(data_python)
print(type(data_python))

