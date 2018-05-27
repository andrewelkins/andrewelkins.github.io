Title: How to do decrypt a pgp message
Date: 2014-04-25 08:59
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-do-decrypt-a-pgp-message
Status: published

After sending my public pgp key and getting an encoded message back. I
need to decrypt a pgp message.

I made a pgp file by opening a text editor and saving it as
"mypgpfile.pgp"

~~~~  
gpg -o output.txt mypgpfile.pgp  
~~~~

The breakdown:  
gpg - the command to encode/decode pgp on linux. Package may need to be
installed.  
-o - specifies the output file  
output.txt - the output filename  
mypgpfile.pgp - the input encoded message
