Title: Depends: libssl0.9.8 (>= 0.9.8m-1) but it is not installable
Date: 2013-07-03 08:48
Author: Andrew Elkins
Category: Command Line, Linux
Tags: debian, server
Slug: depends-libssl0-9-8-0-9-8m-1-but-it-is-not-installable
Status: published

I was setting up a webserver on Debian 7 but ran in to a dependency
issue for nginx. It said I needed libssl0.9.8. Well I had libssl1.0.x
which left me wondering was it in compatible. Yes it is. I needed to
download the deb and install it.

~~~~  
root@web1:\~\# apt-get install nginx nginx-light php5-fpm php5-gd
php5-curl php5-mysql libssl-dev  
Reading package lists... Done  
Building dependency tree  
Reading state information... Done  
libssl-dev is already the newest version.  
Some packages could not be installed. This may mean that you have  
requested an impossible situation or if you are using the unstable  
distribution that some required packages have not yet been created  
or been moved out of Incoming.  
The following information may help to resolve the situation:

The following packages have unmet dependencies:  
nginx-light : Depends: libssl0.9.8 (&gt;= 0.9.8m-1) but it is not
installable  
E: Unable to correct problems, you have held broken packages.

~~~~

wget the correct deb
http://snapshot.debian.org/package/openssl098/0.9.8o-7/\#libssl0.9.8\_0.9.8o-7

~~~~  
wget
http://snapshot.debian.org/archive/debian/20110406T213352Z/pool/main/o/openssl098/libssl0.9.8\_0.9.8o-7\_i386.deb  
~~~~

Then install it.

~~~~  
sudo dpkg -i libssl0.9.8\_0.9.8o-7\_i386.deb  
~~~~
