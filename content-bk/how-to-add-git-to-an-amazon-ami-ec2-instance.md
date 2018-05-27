Title: How to add git to an amazon ami ec2 instance
Date: 2012-01-08 11:58
Author: Andrew Elkins
Category: Linux
Slug: how-to-add-git-to-an-amazon-ami-ec2-instance
Status: published

To install git on amazon ami is really simple. Make sure you have sudo
and then run yum to install it.

> sudo yum install git

That's it. The output should be something like:

> \$ sudo yum install git  
> Loaded plugins: fastestmirror, priorities, security  
> Determining fastest mirrors  
> amzn-main | 2.1 kB 00:00  
> amzn-main/primary\_db | 1.6 MB 00:00  
> amzn-updates | 2.3 kB 00:00  
> amzn-updates/primary\_db | 233 kB 00:00  
> Setting up Install Process  
> Resolving Dependencies  
> --&gt; Running transaction check  
> --&gt; Processing Dependency: git = 1.7.2.5-1.16.amzn1 for package:
> perl-Git-1.7.2.5-1.16.amzn1.i686  
> ---&gt; Package git.i686 0:1.7.4.5-1.21.amzn1 set to be updated  
> --&gt; Running transaction check  
> ---&gt; Package perl-Git.i686 0:1.7.4.5-1.21.amzn1 set to be updated  
> --&gt; Finished Dependency Resolution
>
> Dependencies Resolved
>
> ==============================================================================================================================  
> Package Arch Version Repository Size  
> ==============================================================================================================================  
> Updating:  
> git i686 1.7.4.5-1.21.amzn1 amzn-main 4.4 M  
> Updating for dependencies:  
> perl-Git i686 1.7.4.5-1.21.amzn1 amzn-main 16 k
>
> Transaction Summary  
> ==============================================================================================================================  
> Install 0 Package(s)  
> Upgrade 2 Package(s)
>
> Total download size: 4.4 M  
> Is this ok \[y/N\]: y  
> Downloading Packages:  
> (1/2): git-1.7.4.5-1.21.amzn1.i686.rpm | 4.4 MB 00:00  
> (2/2): perl-Git-1.7.4.5-1.21.amzn1.i686.rpm | 16 kB 00:00  
> ------------------------------------------------------------------------------------------------------------------------------  
> Total 7.9 MB/s | 4.4 MB 00:00  
> Running rpm\_check\_debug  
> Running Transaction Test  
> Transaction Test Succeeded  
> Running Transaction  
> Updating : git-1.7.4.5-1.21.amzn1.i686 1/4  
> Updating : perl-Git-1.7.4.5-1.21.amzn1.i686 2/4  
> Cleanup : git-1.7.2.5-1.16.amzn1.i686 3/4  
> Cleanup : perl-Git-1.7.2.5-1.16.amzn1.i686 4/4
>
> Updated:  
> git.i686 0:1.7.4.5-1.21.amzn1
>
> Dependency Updated:  
> perl-Git.i686 0:1.7.4.5-1.21.amzn1
>
> Complete!
