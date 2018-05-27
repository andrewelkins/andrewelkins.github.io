Title: Add swap file in linux on debian
Date: 2014-03-11 09:02
Author: Andrew Elkins
Category: Command Line, Linux
Slug: add-swap-file-in-linux-on-debian
Status: published

How to add a swap file to an existing file system is almost trivial.

First decide how big you want it. I choose 1GB w/ a 1GB RAM machine.

Second create the file.  
~~~~  
dd if=/dev/zero of=/swapfile bs=1024 count=1048576  
~~~~

Next make it a swap.  
~~~~  
mkswap /swapfile  
~~~~

Add it as a swap.  
~~~~  
swapon /swapfile  
~~~~

Edit fstab.  
~~~~  
vim /etc/fstab  
~~~~

Add

~~~~  
/swapfile none swap sw 0 0  
~~~~

Save and verify output  
~~~~  
/swapfile none swap sw 0 0  
~~~~
