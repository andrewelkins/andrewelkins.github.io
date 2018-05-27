Title: How to specify a different git port
Date: 2014-01-03 11:09
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-specify-a-different-git-port
Status: published

I needed to figure out how to specify a different ssh port for git.
Turns out it's very easy.

Open up your ssh config file.

~~~~  
vim /home/your-user-name/.ssh/config  
~~~~

Add a new configuration declaration

~~~~  
Host git.example.org  
User your-user-name  
Port 22222  
~~~~

Save the new config and try that git clone again. It should work this
time.
