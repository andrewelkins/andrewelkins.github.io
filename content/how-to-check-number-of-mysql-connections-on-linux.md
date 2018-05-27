Title: How to check number of mysql connections on linux
Date: 2014-04-14 08:54
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-check-number-of-mysql-connections-on-linux
Status: published

I needed to check how many mysql connections my application currently
had. Not from the mysql side but from the application linux server. To
do so I checked how many connections where on the mysql port (3306).

~~~~  
netstat -antp | grep :3306 | wc -l  
~~~~
