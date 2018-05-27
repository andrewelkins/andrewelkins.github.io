Title: Find out what files are owned by apache
Date: 2013-03-09 09:57
Author: Andrew Elkins
Category: Linux
Slug: find-out-what-files-are-owned-by-apache
Status: published

In an audit of my system I needed to find all the files owned by apache.

\[ps\]  
find ./ -name apache  
\[/ps\]

Simple!

Here's the group and user example:

\[ps\]  
find ./ -group apache -name apache  
\[/ps\]
