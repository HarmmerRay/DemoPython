from pyspark import SparkContext, SparkConf
import os

os.environ['HADOOP_HOME'] = "E:\BigData\hadoop-3.0.0"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set('spark.default.parallelism', '1')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7], 1)
# 1.collect
print(rdd.collect())
# 2.reduce
print(rdd.reduce(lambda x, y: x + y))
# 3.take
print(rdd.take(3))
# 4.count
print(rdd.count())
# 输出到文件中
rdd.saveAsTextFile("xxx.txt")
