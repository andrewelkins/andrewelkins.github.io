Title: How to set a password on pdf in Ubuntu
Date: 2015-04-10 14:32
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-set-a-password-on-pdf-in-ubuntu
Status: published

This one is super simple.

~~~~  
sudo apt-get install pdftk  
pdftk input-file.pdf output output-file.pdf userpw
mysupersecretpassword  
~~~~
