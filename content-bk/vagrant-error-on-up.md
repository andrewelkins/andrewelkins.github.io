Title: Vagrant error on up
Date: 2016-09-27 09:16
Author: Andrew Elkins
Category: Linux
Slug: vagrant-error-on-up
Status: published

I was executing a vagrant up on my machine. It was giving an nfs error.

~~~~  
mount -o 'vers=3,udp' 192.168.10.1:'/opt/&lt;snip&gt;/mozilla/kuma'
/home/vagrant/src

Stdout from the command:

Stderr from the command:

stdin: is not a tty  
mount.nfs: requested NFS version or transport protocol is not supported  
~~~~

I went hunting for a resolution. I need to install nfs libs.

~~~~  
sudo apt-get install nfs-common nfs-kernel-server  
~~~~

Then it would boot.
