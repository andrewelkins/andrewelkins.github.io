Title: Install Jenkins on Debian 7
Date: 2013-07-29 21:42
Author: Andrew Elkins
Category: Command Line, Linux
Slug: install-jenkins-on-debian-7
Status: published

Here's how I installed Jenkins on Debian 7.  
~~~~  
\$ wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key |
sudo apt-key add -  
\$ sudo echo 'deb http://pkg.jenkins-ci.org/debian binary/' &gt;&gt;
/etc/apt/sources.list  
\$ sudo apt-get update  
\$ sudo apt-get install jenkins  
~~~~
