import json

from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = "E:\Python\Python98\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
rdd = sc.textFile("orders.txt")
print(rdd.collect())

rdd1 = rdd.flatMap(lambda x: x.split("|"))
print(rdd1.collect())

rdd2 = rdd1.map(lambda x: json.loads(x))
print(rdd2.collect())


rdd3 = rdd2.map(lambda a: (a["areaName"], float(a["money"])))
print(rdd3.collect())

rdd4 = rdd3.reduceByKey(lambda a, b: a + b)
print(rdd4.collect())

rdd5 = rdd4.sortBy(lambda a: a[1], False, 1)
print(f"各个城市销售额排名，从大到小:{rdd5.collect()}")

print(f"全部城市，有哪些商品在售卖:{rdd2.map(lambda x: x['category']).distinct().collect()}")

print(f"北京市，有哪些商品在售卖:{rdd2.filter(lambda x: x['areaName'] == '北京').map(lambda x: x['category']).distinct().collect()}")