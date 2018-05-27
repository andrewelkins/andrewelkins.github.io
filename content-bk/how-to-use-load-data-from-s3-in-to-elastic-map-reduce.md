Title: How to use load data from s3 in to elastic map reduce
Date: 2014-05-14 17:48
Author: Andrew Elkins
Category: Command Line, Linux, pig, Programming
Slug: how-to-use-load-data-from-s3-in-to-elastic-map-reduce
Status: published

How to load data from s3 in to Amazon Elastic Map Reduce is fairly easy.
The trick is to use s3n or s3 at the data source.

~~~~  
A = LOAD 's3n://AWSKEY:AWSTOKEN@your-s3-bucket/file-name\*' as
(col1:chararray, col12:chararray, col3:chararray, \[...\]);  
~~~~
