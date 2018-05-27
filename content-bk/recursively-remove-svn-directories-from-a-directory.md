Title: Recursively remove svn directories from a directory
Date: 2012-01-13 11:47
Author: Andrew Elkins
Category: Linux
Slug: recursively-remove-svn-directories-from-a-directory
Status: published

Removing all .svn directories from a file structure in linux is as
simple as running a one liner.

> find . -name .svn -print0 | xargs -0 rm -rf
