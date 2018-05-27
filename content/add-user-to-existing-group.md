Title: Add user to existing group
Date: 2015-07-14 13:50
Author: Andrew Elkins
Category: PHP
Slug: add-user-to-existing-group
Status: published

This is dead simple. I often need to add a new user to the sudoer group,
"sudo" by default.

> sudo usermod -a -G groupName userName

So for adding a user to the sudoers group.

> sudo usermod -a -G sudo {username}

 
