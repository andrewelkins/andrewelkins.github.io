Title: Move files while preserving timestamps
Date: 2015-04-02 16:30
Author: Andrew Elkins
Category: Command Line, Linux
Slug: move-files-while-preserving-timestamps
Status: published

A quick way to move files in linux while keeping their timestamps. In
short mv doesn't support this. The work around is to copy instead.

~~~~  
cp -p -r -l source/date target/  
rm -rf source/data  
~~~~
