Title: How to set Laravel 4 environments
Date: 2013-03-17 20:35
Author: Andrew Elkins
Category: PHP, Programming
Tags: laravel
Slug: how-to-set-laravel-4-environments
Status: published

The environment is based on url matches.

You'll find that configuration in /bootstrap/start.php

\[ps\]  
\$env = \$app-&gt;detectEnvironment(array(

'local' =&gt; array('your-machine-name'),

));  
\[/ps\]

Now say you are developing locally and use the prefix/postfix local.
E.g: my-new-site.local or local.my-new-site

\[ps\]  
\$env = \$app-&gt;detectEnvironment(array(

'local' =&gt; array('local.\*','\*.local'),

));  
\[/ps\]

That sets the environment, now to use it you'll need to create a local
folder in /app/config/

\[ps\]  
mkdir app/config/local  
\[/ps\]

And so you want to have a different database configuration for local.
Just copy the database config file in to the local directory and modify
it.

\[ps\]  
cp app/config/database.php app/config/local/database.php  
\[/ps\]
