Title: Install VirtualBox Guest Additions Command Line
Date: 2014-03-08 13:46
Author: Andrew Elkins
Category: Command Line, Linux
Slug: install-virtualbox-guest-additions-command-line
Status: published

I was digging around searching on how to install the VirtualBox Guest
additions without the GUI using the command line. Most of the tutorials
out there were of no help. Either with bad or outdated information. I
found one article on
[xmodulo](http://xmodulo.com/2013/07/how-to-install-virtualbox-guest-additions-for-linux.html)
that worked for me.

Here's the steps I followed for my Ubuntu Server VM.

First downloaded the vbox guest addition. Replace X.X.X with your
version. You can find that by going to the about within your virtual box
install.

~~~~
wget
http://download.virtualbox.org/virtualbox/X.X.X/VBoxGuestAdditions\_X.X.X.iso
~~~~

Then install the packages that is requires.

~~~~
sudo apt-get install dkms gcc 
~~~~

Then mount.

~~~~
sudo mount -o loop VBoxGuestAdditions\_4.2.16.iso /mnt  
cd /mnt  
~~~~

and Install

~~~~
sudo ./VBoxLinuxAdditions.run 
~~~~

Visit the
[Source](http://xmodulo.com/2013/07/how-to-install-virtualbox-guest-additions-for-linux.html)
for additional information and how to on other distros.
