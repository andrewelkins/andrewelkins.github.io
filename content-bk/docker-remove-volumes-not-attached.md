Title: Docker remove ALL volumes not attached
Date: 2016-11-15 12:51
Author: Andrew Elkins
Category: Command Line, Docker, Linux
Slug: docker-remove-volumes-not-attached
Status: published

Docker can be tricky to debug. There's instances where after upgrading a
container the volume that was previously attached fails to work.

In this case it was a dev image and the quickest, and dirtiest, option
was to clear out and rebuild. I could go one by one to delete the
specific volumes.

~~~~  
docker volume ls  
docker volume rm {specific\_docker\_container}  
~~~~

Instead I chose to delete all volumes not currently in use. This worked
for my use case as I only have two dockers setups, left the one I wanted
to keep running while executing the following commands.

~~~~  
docker volume rm \`docker volume ls -q -f dangling=true\`  
~~~~
