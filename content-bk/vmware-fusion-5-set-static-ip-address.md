Title: VMWare Fusion 5 Set Static IP Address
Date: 2013-02-18 14:50
Author: Andrew Elkins
Category: Linux
Slug: vmware-fusion-5-set-static-ip-address
Status: published

I previously posted on setting a static ip address in [vmware fusion
4](http://andrewelkins.com/linux/vmware-fusion-4-set-static-ip-address/).
This also still works for VMWare Fusion 5.

Steps are the same.

First on your linux vm in terminal run the following command

> ifconfig

Then copy the HWaddr it varies from vm to vm so you need to get yours

> Link encap:Ethernet  HWaddr 00:0c:29:f4:13:e4

Next edit the dhcp.conf file on your mac

> sudo vim /Library/Preferences/VMware~~~~ Fusion/vmnet8/dhcpd.conf

After the

> \#\#\#\#\#\#\# VMNET DHCP Configuration. End of "DO NOT MODIFY
> SECTION" \#\#\#\#\#\#\#

Add your new configuration, replace "vmnamehere" with the name of your
vm.

> host vmnamehere {  
> hardware ethernet 00:0c:22:f6:11:e8;  
> fixed-address 192.168.115.50;  
> }

Now reboot your Mac or, as @splintax mentioned in the comments, restart
DHCP.

> cd /Applications/VMware Fusion.app/Contents/Library  
> sudo ./vmnet-cli --configure  
> sudo ./vmnet-cli --stop  
> sudo ./vmnet-cli --start

Your vm's ip address should be what you set.

If that doesn't work, you may need to remove the network adapter and
then re-add it. Make sure that your network adapter is connected to the
virtual machine by removing and re-adding it.

> a.  Shut down your virtual machine.
> b.  In Fusion, go to Virtual Machine &gt; Settings &gt; Network
>     Adapter (Fusion 4 and later) / Network (Fusion 3 and earlier).
> c.  Ensure that the network adapter is connected (that is, Enable
>     Network Adapter is ON or the **Connected** box is selected).
> d.  Ensure that the network adapter is configured for NAT or Bridged,
>     and not Host Only or Custom. Make a note of your setting.
> e.  Click triangle beside Advanced options and select Remove Network
>     Adapter (Fusion 4 and later) or click the **- (minus)** button at
>     the bottom of the Network pane (Fusion 3 and earlier) to remove
>     your current network adapter.
> f.  From the Settings pane select Add Device &gt; Network
>     Adapter (Fusion 4 and later) or the **+ (plus)** button at the
>     bottom of the Network pane to re-add your network adapter.
> g.  Verify that your new network adapter settings match your
>     old settings.
> h.  Restart your Mac.
> i.  Turn on your virtual machine.
>
> [From step
> 12](http://kb.vmware.com/selfservice/microsites/search.do?cmd=displayKC&externalId=1016466)
