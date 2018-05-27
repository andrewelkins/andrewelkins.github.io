Title: Linux rename a bunch of file's extensions
Date: 2013-01-20 18:52
Author: Andrew Elkins
Category: Linux, Programming
Slug: linux-rename-a-bunch-of-files-extensions
Status: published

In order to rename a whole folders file extensions from jpeg to jpg I
wrote this script called rename.sh in bash.

> \#!/bin/bash
>
> for filename in \*.jpeg  
> do  
> echo \$filename;  
> cleaned=\`basename \$filename .jpeg\`;  
> echo \$cleaned;  
> mv \$filename \$cleaned.jpg;  
> done

Then I made is executable from the command line.

> chmod +x rename.sh

Then ran it in the directory I needed to rename files in.

> ./rename.sh
