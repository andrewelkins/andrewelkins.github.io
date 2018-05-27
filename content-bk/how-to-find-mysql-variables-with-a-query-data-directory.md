Title: How to find mysql variables with a query, specifically data directory
Date: 2013-04-28 13:34
Author: Andrew Elkins
Category: Command Line, mysql, Programming
Slug: how-to-find-mysql-variables-with-a-query-data-directory
Status: published

I needed to find out the data directory for mysql. A quick way to do
this within mysql is to use the *show variables* command.

~~~~

mysql&gt; show variables;

~~~~

Which will output something like:

~~~~

+-----------------------------------------+-------------------------------------------------------------------------------------------+  
| Variable\_name | Value |  
+-----------------------------------------+-------------------------------------------------------------------------------------------+  
| auto\_increment\_increment | 1 |  
| auto\_increment\_offset | 1 |  
| autocommit | ON |  
| automatic\_sp\_privileges | ON |  
| back\_log | 50 |  
| basedir | /usr/ |  
| big\_tables | OFF |  
| binlog\_cache\_size | 32768 |  
| binlog\_direct\_non\_transactional\_updates | OFF |  
| binlog\_format | STATEMENT |  
| bulk\_insert\_buffer\_size | 8388608 |  
| character\_set\_client | latin1 |  
| character\_set\_connection | latin1 |  
| character\_set\_database | latin1 |  
| character\_set\_filesystem | binary |  
| character\_set\_results | latin1 |  
| character\_set\_server | latin1 |  
| character\_set\_system | utf8 |  
| character\_sets\_dir | /usr/share/mysql/charsets/ |  
| collation\_connection | latin1\_swedish\_ci |  
| collation\_database | latin1\_swedish\_ci |  
| collation\_server | latin1\_swedish\_ci |  
| completion\_type | 0 |  
| concurrent\_insert | 1 |  
| connect\_timeout | 10 |  
| datadir | /var/lib/mysql/ |  
| date\_format | %Y-%m-%d |  
| datetime\_format | %Y-%m-%d %H:%i:%s |  
| default\_week\_format | 0 |  
| delay\_key\_write | ON |  
| delayed\_insert\_limit | 100 |  
| delayed\_insert\_timeout | 300 |  
| delayed\_queue\_size | 1000 |

\[ .......\]

| version\_comment | (Ubuntu) |  
| version\_compile\_machine | i686 |  
| version\_compile\_os | debian-linux-gnu |  
| wait\_timeout | 28800 |  
| warning\_count | 0 |  
+-----------------------------------------+-------------------------------------------------------------------------------------------+

~~~~

You'll see on this development server the data directory was
in */var/lib/mysql/*
