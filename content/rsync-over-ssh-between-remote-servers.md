Title: Rsync over ssh between remote servers
Date: 2013-03-20 18:18
Author: Andrew Elkins
Category: Linux
Slug: rsync-over-ssh-between-remote-servers
Status: published

In order to use rsync with a ssh key I used the -e flag on the rsync
command. It will allow rsync over ssh local to a remote server.

\[ps\]

\[\$ \~\] rsync -avz -e "ssh -i .ssh/id\_key.pem" /opt/stuff/here/
user@10.0.0.1:/opt/stuff/here/

\[/ps\]
