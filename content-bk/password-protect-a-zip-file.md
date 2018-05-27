Title: Password protect a zip file
Date: 2015-04-19 16:42
Author: Andrew Elkins
Category: Command Line, Linux
Slug: password-protect-a-zip-file
Status: published

Sometime a simple encrypt with a password is needed. This isn't the
[most secure method (7z provides more secure
methods)](http://andrewelkins.com/linux/7z-file-encryption-with-password/ "7z file encryption with password"),
but is better than nothing. I simple way to do it is to create a zip
password protected with all the files.

~~~~  
zip --password yourpassword filename.zip file.doc file1.doc file2.doc  
~~~~

Often it's easier to just zip a whole directory.

~~~~  
zip --password yourpassword -r filename.zip files-to-be-zipped/  
~~~~
