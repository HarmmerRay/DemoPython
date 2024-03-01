from pyspark import SparkContext, SparkConf
# import os
# os.environ['PYSPARK_PYTHON'] = '/path/to/pyhon.exe'
# os.environ['HADOOP_HOME'] = '/path/to/hadoop-3.3.1'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", 1)
sc = SparkContext(conf=conf)

rdd1 = sc.textFile("search_log.txt").map(lambda x: x.split("\t"))

task1 = rdd1.map(lambda x: x[0]). \
    map(lambda x: (x.split(":")[0], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False). \
    map(lambda x: x[0]).take(3)
print(f"热门搜索时间TOP3:{task1}")

task2 = rdd1.map(lambda x: (x[2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False). \
    map(lambda x: x[0]).take(3)
print(f"热门搜索词TOP3:{task2}")

task3 = rdd1.filter(lambda x: x[2] == '黑马程序员'). \
    map(lambda x: x[0]). \
    map(lambda x: (x.split(':')[0], 1)). \
    reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False)
print(f"“黑马程序员”关键词在{task3.take(1)}这个时段被搜索最多")
# 将数据转为json文件并输出
rdd1.map(lambda x: {"time": x[0], "user_id": x[1], "keyword": x[2], "rank1": x[3], "rank2": x[4],
                    "address": x[5]}).saveAsTextFile("search_logJson.txt")
