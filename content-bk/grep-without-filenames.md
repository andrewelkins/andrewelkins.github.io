Title: grep without filenames
Date: 2016-11-01 11:26
Author: Andrew Elkins
Category: Command Line, Linux
Tags: cli, command, file, grep, linux
Slug: grep-without-filenames
Status: published

I needed to grep a directory, and sub directories, and not displaying
the filenames in the output. This is when the man page came to the
rescue.

~~~~  
man grep | grep filename  
~~~~

Output

~~~~  
-H, --with-filename  
-h, --no-filename  
~~~~

There we go, **-h, --no-filename**, is what I needed.

Example with output to a file:

~~~~  
grep -r "searching-for-this" . --no-filename &gt; /tmp/test.txt  
~~~~
