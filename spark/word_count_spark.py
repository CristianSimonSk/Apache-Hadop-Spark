from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext(appName="WordCount")
    text_file = sc.textFile("hdfs://hadoop-namenode:9000/input")
    counts = text_file.flatMap(lambda line: line.split()) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("hdfs://hadoop-namenode:9000/output")
