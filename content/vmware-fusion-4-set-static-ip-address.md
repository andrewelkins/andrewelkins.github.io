Title: VMWare Fusion 4 - Set static IP address
Date: 2012-01-31 19:12
Author: Andrew Elkins
Category: Linux
Slug: vmware-fusion-4-set-static-ip-address
Status: published

In vmware Fusion 4 there is [no
boot.sh](kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1004023)that
is found in previous versions

> sudo "/Library/Application Support/VMware Fusion/boot.sh" --restart

So if you make a change to the network settings like setting a static ip
address you'll need to restart your computer for the settings to take
effect.

To set a static ip in VMWare Fusion 4 do the following:

First on your vm in terminal run

> ifconfig

Then edit the HWaddr

> Link encap:Ethernet  HWaddr 00:0c:29:f4:13:e4

Next copy the dhcp.conf file on your mac

> sudo vim /Library/Preferences/VMware\\ Fusion/vmnet8/dhcpd.conf

After the

> \#\#\#\#\#\#\# VMNET DHCP Configuration. End of "DO NOT MODIFY
> SECTION" \#\#\#\#\#\#\#

Add your new configuration, replace "vmnamehere" with the name of your
vm.

> host vmnamehere {  
> hardware ethernet 00:0c:22:f6:11:e8;  
> fixed-address 192.168.115.50;  
> }

Now reboot your Mac.

Your vm's ip address should be what you set.

If that doesn't work, you may need to remove the network adapter and
then re-add it. Make sure that your network adapter is connected to the
virtual machine by removing and re-adding it. [See Step
12](http://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC&externalId=1016466)
