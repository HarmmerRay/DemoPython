from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile("search_log.txt")
print(rdd.collect())

rdd1 = rdd.map(lambda x: x.split("\t"))
print(rdd1.collect())

rdd2 = rdd1.map(lambda x: x[0])
print(rdd2.collect())

rdd3 = rdd2.map(lambda x: (x.split(":")[0], 1))
print(rdd3.collect())

rdd4 = rdd3.reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False).map(lambda x: x[0])
print(f"热门搜索时间TOP3:{rdd4.take(3)}")
print(
    f"热门搜索词TOP3:{rdd1.map(lambda x: (x[2], 1)).reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False).map(lambda x: x[0]).take(3)}")
tmp = rdd1.filter(lambda x: x[2] == '黑马程序员').map(lambda x: x[0]).map(lambda x: (x.split(':')[0], 1)).reduceByKey(
    lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False)
print(tmp.collect())
print(f"“黑马程序员”关键词在{tmp.flatMap(lambda x : x[0]).take(1)}这个时段被搜索最多，搜索{tmp.flatMap(lambda x : x[1]).take(1)}次")
# 将数据转为json文件并输出
