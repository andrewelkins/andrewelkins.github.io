Title: Display phpinfo from the command line
Date: 2011-12-02 11:37
Author: Andrew Elkins
Category: Linux
Slug: display-phpinfo-from-the-command-line
Status: published

This afternoon I was wanting to get a couple things from phpinfo but
didn't want to do the typical make a php file, put phpinfo, run it from
a browser or command prompt. There's a better, quicker way if you know
what you want. One will output it to a file for review:

> echo "&lt;?php phpinfo(); ?&gt;" | php &gt; phpinfo.txt

Second is the quickest. It output the info and the grep for the
information you need:

> php -i | grep 'version'

Replace version with your own search query.
