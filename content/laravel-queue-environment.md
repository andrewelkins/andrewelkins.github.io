Title: Laravel queue environment
Date: 2017-03-23 07:30
Author: Andrew Elkins
Category: PHP
Slug: laravel-queue-environment
Status: published

Ran in to an issue running queue through supervisor. I'll give a quick
rundown of my setup, the issue and solution.

I have supervisor running the queue daemon.  
~~~~  
\[program:laravel\_queue\]  
command=php /var/www/example.com/artisan queue:listen  
autostart=true  
autorestart=true  
stderr\_logfile=/var/log/laraqueue.err.log  
stdout\_logfile=/var/log/laraqueue.out.log  
~~~~

The key part check on is the env variable isn't set automatically for
the queue. You'll need to set it via the ---env flag.

~~~~  
\[program:laravel\_queue\]  
command=php /var/www/example.com/artisan queue:listen --env=prod  
autostart=true  
autorestart=true  
stderr\_logfile=/var/log/laraqueue.err.log  
stdout\_logfile=/var/log/laraqueue.out.log  
~~~~

That's what I was missing. Once I \`sudo supervisorctl restart
laravel\_queue\` all was well with the queue.
