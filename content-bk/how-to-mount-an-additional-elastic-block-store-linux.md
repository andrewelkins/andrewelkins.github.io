Title: How to mount an additional Elastic Block Store Linux
Date: 2014-03-10 10:58
Author: Andrew Elkins
Category: AWS, Command Line, Linux
Slug: how-to-mount-an-additional-elastic-block-store-linux
Status: published

I needed to add an elastic block store to a Ubuntu Linux Server. I
created the instance from with the [AWS admin
console](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html).
What was missing was how to have the Ubuntu instance recognize it. Turns
out it is fairly simple. Format, and mount.

**Mount**

SSH into the instance and become root.

~~~~  
\$ ssh ubuntu@my-server  
\$ sudo su  
~~~~

Find the new volume's name  
~~~~  
\$ fdisk -l

Disk /dev/xvda1: 8589 MB, 8589934592 bytes  
255 heads, 63 sectors/track, 1044 cylinders, total 16777216 sectors  
Units = sectors of 1 \* 512 = 512 bytes  
Sector size (logical/physical): 512 bytes / 512 bytes  
I/O size (minimum/optimal): 512 bytes / 512 bytes  
Disk identifier: 0x00000000

Disk /dev/xvda1 doesn't contain a valid partition table

Disk /dev/xvdf: 107.4 GB, 107374182400 bytes  
255 heads, 63 sectors/track, 13054 cylinders, total 209715200 sectors  
Units = sectors of 1 \* 512 = 512 bytes  
Sector size (logical/physical): 512 bytes / 512 bytes  
I/O size (minimum/optimal): 512 bytes / 512 bytes  
Disk identifier: 0x00000000

Disk /dev/xvdf doesn't contain a valid partition table

~~~~

In my case it's "/dev/xvdf"

We'll need to format the volume.

~~~~  
\$ mkfs -t ext3 /dev/xvdf

mke2fs 1.42 (29-Nov-2011)  
Filesystem label=  
OS type: Linux  
Block size=4096 (log=2)  
Fragment size=4096 (log=2)  
Stride=0 blocks, Stripe width=0 blocks  
6553600 inodes, 26214400 blocks  
1310720 blocks (5.00%) reserved for the super user  
First data block=0  
Maximum filesystem blocks=4294967296  
800 block groups  
32768 blocks per group, 32768 fragments per group  
8192 inodes per group  
Superblock backups stored on blocks:  
32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,  
4096000, 7962624, 11239424, 20480000, 23887872

Allocating group tables: done  
Writing inode tables: done  
Creating journal (32768 blocks): done  
Writing superblocks and filesystem accounting information: done  
~~~~

Now to mount it

~~~~  
\$ mkdir /mnt/ebs-volume-1  
\$ mount /dev/xvdf /mnt/ebs-volume-1/  
~~~~
