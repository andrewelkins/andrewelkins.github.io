Title: Error starting Tomcat7 “no JDK found – please set JAVA_HOME”
Date: 2013-08-26 17:30
Author: Andrew Elkins
Category: Command Line, Linux
Slug: error-starting-tomcat7-no-jdk-found-please-set-java_home
Status: published

After I had set JAVA\_HOME in the /etc/profile

~~~~  
export JAVA\_HOME=/usr/lib/jvm/java-7-oracle/bin/java  
~~~~

But Tomcat wasn't happy with that. So I went to Tomcat configuration
directly. File: /etc/default/tomcat7

~~~~  
\$ vim /etc/default/tomcat7  
~~~~

~~~~  
...

\# The home directory of the Java development kit (JDK). You need at
least  
\# JDK version 1.5. If JAVA\_HOME is not set, some common directories
for  
\# OpenJDK, the Sun JDK, and various J2SE 1.5 versions are tried.  
\#JAVA\_HOME=/usr/lib/jvm/openjdk-6-jdk  
JAVA\_HOME=/usr/lib/jvm/java-7-oracle

...  
~~~~
