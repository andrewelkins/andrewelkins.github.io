Title: Convert pdf to png easily
Date: 2014-11-23 12:29
Author: Andrew Elkins
Category: Command Line, Linux
Slug: convert-pdf-to-png-easily
Status: published

I need to quickly convert odfs to image for both online processing and
one off processing. Luckily imagemagick had me covered for both.

First install imagemagick:

~~~~  
sudo apt-get install imagemagick  
~~~~

Then use the convert function to do the work:

~~~~  
convert example.pdf example.png  
~~~~

This will append \#\# to the file name if the pdf is multiple pages.
convert also has a few options that effect the quality, size, trimming,
etc.
