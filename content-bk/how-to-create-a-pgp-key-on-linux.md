Title: How to create a PGP key on linux
Date: 2014-04-23 08:26
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-create-a-pgp-key-on-linux
Status: published

First you'll want to create your key.

~~~~  
gpg --gen-key  
~~~~

Then ascii armor it for sharing.

~~~~  
gpg --armor --export user@example.com  
~~~~

You can view your keys by using the list command.

~~~~  
gpg --list-keys  
~~~~
