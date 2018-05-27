Title: Using xargs to parallel a process in the command line
Date: 2013-04-15 09:38
Author: Andrew Elkins
Category: Command Line, Linux
Tags: cli, grep, parallel, xargs
Slug: using-xargs-to-parallel-a-process-in-the-command-line
Status: published

Most of us have multiple CPUs in our personal machines. I would also
hope that your servers do too. If you're running an intensive command
line process, running them in parallel will speed it up by paralleling
the process.

Say you need to find a string in all of your log files. On any server
that has multiple programs running there's a lot of log files to run
though. Here's an example:

   
~~~~  
find /var/logs -type f | xargs -P 4 -n 10 grep -H 'string-to-search'  
~~~~

[Read more on
xargs](http://blog.labrat.info/20100429/using-xargs-to-do-parallel-processing/)  
and [even more examples](http://sidvind.com/wiki/Xargs_by_example)
