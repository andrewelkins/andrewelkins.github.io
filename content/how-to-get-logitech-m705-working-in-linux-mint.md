Title: How to get logitech m705 working in linux mint
Date: 2013-05-28 17:29
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-get-logitech-m705-working-in-linux-mint
Status: published

I am using a new laptop, ASUS Zenbook, running linux mint cinnamon. My
preferred mouse is a logitech m705 for use on the go. I needed to get it
working since it wasn't out of the box. There's several ways to get the
unifying receiver working. The easiest for me was using a project on
github, [logitech unifier](https://github.com/treeder/logitech_unifier).

Simple to do.

~~~~

cd \~

wget https://github.com/treeder/logitech\_unifier/archive/master.zip

unzip master.zip

cd logitech\_unifier-master

./autopair.sh

~~~~

Then followed the prompts, turned it on and it worked. Much simpler than
the other options I considered.
