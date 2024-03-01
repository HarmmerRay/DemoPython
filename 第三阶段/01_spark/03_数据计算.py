from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = 'E:\Python\Python98\python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# # 1.map
# rdd = sc.parallelize([1, 2, 3, 4, 5, 6])
# # def func(data):
# #     return data * 10
# rdd1 = rdd.map(lambda x: x * 2)
# print(rdd1.collect())
# # 链式调用
# rdd1 = rdd.map(lambda x: x * 2).map(lambda x: x + 3)
# print(rdd1.collect())

# 2.flatmap
# rdd = sc.parallelize(["itheima itcast 666", "itheima itcast 666", "itheima itcast 666"])
#
# rdd1 = rdd.flatMap(lambda x: x.split(" "))
# print(rdd1.collect())

# 3.reduceByKey
# rdd = sc.parallelize([("a", 1), ("a", 1), ("b", 1), ("b", 1), ("b", 1)])
# print(rdd.reduceByKey(lambda a,b: a+b).collect())

# 4.filter
# rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
# print(rdd.filter(lambda x: x % 2 == 0).collect())

# 5.distinct
# rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 7])
# print(rdd.distinct().collect())

# 6.sortBy
