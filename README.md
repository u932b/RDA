http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/#test-your-code-cat-data--map--sort--reduce

cat input.txt |python mapper.py|sort -k1,1

export HADOOP_LIPATH=/opt/cloudera/parcels/CDH-5.8.0-1.cdh5.8.0.p0.42/lib

hadoop jar $HADOOP_LIPATH/hadoop-mapreduce/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/chc631/HW3/input.txt -output /user/chc631/HW3/output

hdfs dfs -rmdir -f HW3/output

hdfs dfs -cat /user/chc631/HW3/output
