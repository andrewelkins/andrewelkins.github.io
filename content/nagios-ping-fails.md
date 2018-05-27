Title: Nagios ping fails
Date: 2013-08-28 07:59
Author: Andrew Elkins
Category: Command Line, Linux, nagios
Slug: nagios-ping-fails
Status: published

I recently setup NagiosXI with their provided amazon ami. It was very
simple to setup and everything looked good. Added a couple servers and
they all could not be pinged from Nagios. I couldn't ping them from
Nagios' ping tool. I could ping them from the command line so I knew it
was a configuration error.

First I tried:  
~~~~  
\$ /usr/local/nagios/libexec/check\_ping -H www.google.com -c 100,90% -w
100,90%  
CRITICAL - Network Unreachable (www.google.com)  
~~~~

Then I [saw I needed to add the
-4](http://serverfault.com/questions/278196/nagios-bizare-ping-behaviour)
to the command.

~~~~  
\$ sudo vim /usr/local/nagios/etc/commands.cfg  
~~~~

Go to line 221 and add the "-4"

~~~~  
define command {  
command\_name check\_ping  
command\_line \$USER1\$/check\_ping -4 -H \$HOSTADDRESS\$ -w \$ARG1\$ -c
\$ARG2\$ -p 5  
}  
~~~~

Then you'll need to restart Nagios.

~~~~  
\$ sudo service nagios restart  
~~~~
