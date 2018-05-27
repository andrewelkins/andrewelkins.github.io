Title: How to set local environment as default in command line (CLI) for Larvel 4 artisan 
Date: 2013-02-25 10:36
Author: Andrew Elkins
Category: Linux, PHP, Programming
Tags: cli, framework, l4, laravel
Slug: how-to-set-local-environment-as-default-in-cli
Status: published

Typically when Laravel 4 artisan is run from the command line (cli) it
uses the production configuration files. This can be changed by using a
flag when running the command.

\[ps\]php artisan migrate --env=local\[/ps\]

However, adding *--env-=local* each time while running a script can slow
down development. I would recommend adding your development environment
hostname to the config file.

To do this Laravel 4 needs the hostname for your [development
environment](http://four.laravel.com/docs/configuration). I recommended
using a new file called **check.php** with the following contents:

\[php\]\#!/usr/bin/env php  
&lt;?php  
var\_dump(gethostname());  
\[/php\]

Run it from the command line:

\[php\]php check.php\[/php\]

This will output something like:

\[ps\]string(6) "ubuntu"\[/ps\]

In this case *ubuntu* is what is needed. We'll need to add it to the
environment array in **bootstrap/start.php**

\[php\]\$env = \$app-&gt;detectEnvironment(array(

'local' =&gt; array('\*.local','ubuntu'),

));  
\[/php\]

Now artisan should run with the local environment as default when run on
that machine.
