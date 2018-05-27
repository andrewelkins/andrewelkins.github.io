Title: Head all files in directory
Date: 2016-06-06 13:30
Author: Andrew Elkins
Category: Bash, Command Line, Linux, Programming
Tags: bash, head, loop
Slug: head-all-files-in-directory
Status: published

Needed to head all files in a directory.

~~~~  
\#!/usr/bin/env bash  
DEST=/tmp  
for i in /files/to/head/\*  
do  
head -10 "\${i}" &gt; \${DEST}/\$(basename \$i)  
done  
~~~~
