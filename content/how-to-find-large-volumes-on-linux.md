Title: How to find large volumes on linux
Date: 2015-04-26 12:16
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-find-large-volumes-on-linux
Status: published

Running linux machines sometimes it's needed to figure out what is
taking up a large amount of room on a server. Here's an easy way to
investigate large directories.

~~~~  
du -h &lt;dir&gt; | grep '\[0-9:::.\]+G'  
~~~~
