Title: Find loaded modules in Apache 2.x
Date: 2012-01-05 22:07
Author: Andrew Elkins
Category: Linux
Slug: find-loaded-modules-in-apache-2-x
Status: published

I was trying to figure out how to find the loaded modules in Apache and
came across this nice command.

> httpd -M

Used like:

> \$ httpd -M  
> Loaded Modules:  
> core\_module (static)  
> mpm\_prefork\_module (static)  
> http\_module (static)  
> so\_module (static)  
> authn\_file\_module (shared)  
> authn\_default\_module (shared)
>
> ......
>
> rewrite\_module (shared)  
> php5\_module (shared)  
> extract\_forwarded\_module (shared)  
> geoip\_module (shared)  
> Syntax OK
