from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = "E:\Python\Python98\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
rdd = sc.textFile("hello.txt")
print(rdd.collect())

rdd1 = rdd.flatMap(lambda x: x.split(" "))
print(rdd1.collect())

rdd2 = rdd1.map(lambda x: (x, 1))
print(rdd2.collect())

rdd3 = rdd2.reduceByKey(lambda a, b: a + b)
print(rdd3.collect())

rdd4 = rdd3.sortBy(lambda x: x[1], True, 1)
print(rdd4.collect())
