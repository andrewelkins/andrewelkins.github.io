Title: Create a new ssh key
Date: 2013-02-03 11:18
Author: Andrew Elkins
Category: Linux
Slug: create-a-new-ssh-key
Status: published

I have to do this whenever setting up a new system. Makes the server
more secure to disable password based login and only allow ssh keys.

To create an ssh key it's as easy as running one of the two following
commands.

> **<kbd>ssh-keygen -t dsa</kbd>**

or

> **<kbd>ssh-keygen -t rsa</kbd>**

The rsa and dsa refer to different encryption methods. [DSA is the
preferred method at the
moment.](http://superuser.com/questions/13164/what-is-better-for-gpg-keys-rsa-or-dsa)
