Title: 7z file encryption with password
Date: 2015-04-19 16:47
Author: Andrew Elkins
Category: Command Line, Linux
Slug: 7z-file-encryption-with-password
Status: published

Previously I've transferred file with a pgp key, but this is an ok
alternative.

~~~~  
7za a -tzip -psuperSecurePassword -mem=AES256 filename.zip file.doc
file1.doc file2.doc  
~~~~

You can also checkout the easier and more supported [zip
method](http://andrewelkins.com/linux/password-protect-a-zip-file/ "Password protect a zip file").
