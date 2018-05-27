Title: How to run ghost in the background
Date: 2014-04-03 17:21
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-run-ghost-in-the-background
Status: published

For running ghost blog in the background manually, execute the following
within your blog directory.

~~~~  
cd /path/to/your/install/  
nohup npm start &lt;/dev/null 1&gt;/path/to/your/install/logs/stdout.log
2&gt;/path/to/your/install/logs/stderr.log &  
~~~~

I perfer to run ghost in the background by using Supervisor.

First install supervisor  
~~~~  
apt-get install supervisor  
~~~~

Make sure it's running  
~~~~  
sudo service supervisor start  
~~~~

Create the config file  
~~~~  
vim /etc/supervisor/conf.d/ghost.conf  
~~~~

~~~~  
\[program:ghost\]  
command = node /path/to/ghost/index.js  
directory = /path/to/ghost  
user = ghost  
autostart = true  
autorestart = true  
stdout\_logfile = /var/log/supervisor/ghost.log  
stderr\_logfile = /var/log/supervisor/ghost\_err.log  
environment = NODE\_ENV="production"  
~~~~

Start Ghost  
~~~~  
supervisorctl start ghost  
~~~~

\*EDIT\*

I've switched to use the npm package Forever.

To install forever type  
:::npm install forever -g  
To start Ghost using forever from the Ghost installation directory type  
:::NODE\_ENV=production forever start index.js  
To stop Ghost type  
:::forever stop index.js  
To check if Ghost is currently running type  
:::forever list

Sources:  
Supervisor information from [ghost
documentation](http://docs.ghost.org/installation/deploy/)
