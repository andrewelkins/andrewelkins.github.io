Title: How to install java 7 on debian
Date: 2013-08-26 16:55
Author: Andrew Elkins
Category: Command Line, Linux, Programming
Tags: java, nginx, server
Slug: how-to-install-java-7-on-debian-oracle-sucks
Status: published

HOW TO INSTALL JAVA 7 ON DEBIAN 7

Debian is my distro of choice for servers, but due to licencing issues
it cannot provide Oracle Java 7+ in the repos. Personally Oracle needs
to undo their restrictive licensing on a VERY popular language.

Need to add an older repository that has the stuff we need:

~~~~  
sudo su -  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main"
| tee -a /etc/apt/sources.list  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise
main" | tee -a /etc/apt/sources.list  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
apt-get update  
~~~~

This adds the packages that contain java7 by oracle.

Install:

~~~~  
sudo apt-get install oracle-java7-installer  
~~~~

Then you'll see a couple of screens asking you to accept their license.
It's fine, just accept both screens and it will now install.

Now you'll want to make sure java 7 is default.

~~~~  
sudo apt-get install oracle-java7-set-default  
~~~~

Verification

~~~~  
\$ java -version  
java version "1.7.0\_17"  
Java(TM) SE Runtime Environment (build 1.7.0\_17-b02)  
Java HotSpot(TM) 64-Bit Server VM (build 23.7-b01, mixed mode)  
~~~~  
Thanks to the
[blog](http://blog.retep.org/2013/04/13/installing-java-7-on-debian-squeeze/)
that had this information originally. Please visit them and give them a
little link juice.
[SOURCE](http://blog.retep.org/2013/04/13/installing-java-7-on-debian-squeeze/)
