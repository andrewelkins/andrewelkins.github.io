Title: How to format hdfs in AWS Elastic Map Reduce
Date: 2014-07-08 07:57
Author: Andrew Elkins
Category: Command Line, hadoop, Linux, Programming
Slug: how-to-format-hdfs-in-aws-elastic-map-reduce
Status: published

It's insanely simple. Connect to your master node within AWS Elastic Map
Reduce. Then you'll want to connect to the hadoop cluster and reset the
NameNode file handlers.

~~~~  
hadoop namenode -format  
~~~~

That's it. That's how you format the hdfs file system.
