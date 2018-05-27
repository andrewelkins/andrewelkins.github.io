Title: How to install Tomcat7 on Linux Mint
Date: 2013-10-24 17:36
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-install-tomcat7-on-linux-mint
Status: published

How to install tomcat7 on linux mint is simple.

Run:

~~~~  
sudo apt-get install tomcat7 tomcat7-admin tomcat7-common  
~~~~

That's it.

Now to configure the users for the mangers.

Open the user file.

~~~~  
sudo vim /etc/tomcat7/tomcat-users.xml  
~~~~

Make it look like this:  
~~~~  
&lt;?xml version='1.0' encoding='utf-8'?&gt;  
&lt;tomcat-users&gt;

&lt;role rolename="manager-gui"/&gt;  
&lt;role rolename="manager-script"/&gt;  
&lt;role rolename="manager"/&gt;  
&lt;role rolename="admin-gui"/&gt;  
&lt;role rolename="admin-script"/&gt;  
&lt;role rolename="admin"/&gt;

&lt;user username="admin" password="admin"
roles="manager-gui,admin-gui,manager,admin,manager-script,admin-script"/&gt;

&lt;/tomcat-users&gt;

~~~~

Then restart tomcat

~~~~  
sudo service tomcat7 restart  
~~~~
