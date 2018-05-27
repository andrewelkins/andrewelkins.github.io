Title: Setting up Composer globally for Laravel 4
Date: 2013-01-06 18:03
Author: Andrew Elkins
Category: Linux, PHP
Tags: composer, laravel, php
Slug: setting-up-composer-globally-for-laravel-4
Status: published

An easy way to set up composer globally is to follow the instructions on
getcomposer.org site:

\[ps\]  
\$ curl -s http://getcomposer.org/installer | php  
\$ sudo mv composer.phar /usr/local/bin/composer  
\[/ps\]

Now I can use composer by invoking just the **composer** command.

Optional way to do it, is to set up an alias:

\[ps\]  
alias composer='/location/of/the/composer.phar'  
\[/ps\]
