Title: How to checkout a remote branch in git
Date: 2013-07-02 07:58
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-checkout-a-remote-branch-in-git
Status: published

In order to avoid conflicts when checking out a branch from a remote
repo you need to check it out directly.

~~~~  
git fetch origin  
git branch -f remote\_branch\_name origin/remote\_branch\_name  
git checkout remote\_branch name  
~~~~

~~~~  
git checkout -b production origin/production  
~~~~

Simple.
