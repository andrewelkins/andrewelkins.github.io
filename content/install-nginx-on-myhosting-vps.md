Title: Install nginx, php-fpm, and mysql on CentOS myhosting.com VPS
Date: 2012-09-21 13:45
Author: Andrew Elkins
Category: Linux
Slug: install-nginx-on-myhosting-vps
Status: draft

###### Warning note: This is how I performed this, use the instructions at your own risk.

Basics
======

Things you'll need for this:

-   [myhosting
    VPS](http://myhosting.com/virtual-server-hosting/custom-vps.aspx) Centos
-   myhosting parallels control panel access
-   terminal / ssh access

How to
======

The default install of Centos from MyHosting includes Apache as the web
server. The first thing you'll want to do is remove it.

> Login to the VPS panel <https://manage.myhosting.com/>

Then go to the VPS Management tab

[![](http://andrewelkins.com/wp-content/uploads/2012/09/vps-management-300x223.png "vps-management"){.size-medium
.wp-image-145 .aligncenter width="300"
height="223"}](http://andrewelkins.com/wp-content/uploads/2012/09/vps-management.png)

Login  to the VZPP either by "Login to VZPP via VPS IP address" or
"Login to VZPP via VPS host name". This will take you to the Parallels
Power Panel.

[![](http://andrewelkins.com/wp-content/uploads/2012/09/parallels-home-screen-300x179.png "parallels-home-screen"){.aligncenter
.size-medium .wp-image-146 width="300"
height="179"}](http://andrewelkins.com/wp-content/uploads/2012/09/parallels-home-screen.png)

From there choose "Software Packages",Where going to remove apache. In
order to do this we need to remove a few modules first. mod\_ssl and
mod\_perl otherwise removing apache will error out.

[![](http://andrewelkins.com/wp-content/uploads/2012/09/mod-ssl-package-300x127.png "mod-ssl-package"){.aligncenter
.size-medium .wp-image-147 width="300"
height="127"}](http://andrewelkins.com/wp-content/uploads/2012/09/mod-ssl-package.png)

[![](http://andrewelkins.com/wp-content/uploads/2012/09/mod-perl-300x126.png "mod-perl"){.aligncenter
.size-medium .wp-image-148 width="300"
height="126"}](http://andrewelkins.com/wp-content/uploads/2012/09/mod-perl.png)

With each of those search, then select the module and uninstall. With
those uninstalled we'll uninstall Apache which in CentOS terms is http.

[![](http://andrewelkins.com/wp-content/uploads/2012/09/software-packages-300x95.png "software-packages"){.aligncenter
.size-medium .wp-image-149 width="300"
height="95"}](http://andrewelkins.com/wp-content/uploads/2012/09/software-packages.png)

So procedure here, search, check http and choose uninstall.

Now that we have apache removed, time to install nginx/php-fpm/mysql via
commandline.

INSTALL NGINX / PHP\_FPM
========================

I decided to go with Remi's packages for this. You'll need to set those
up.

> rpm -Uvh
> http://download.fedoraproject.org/pub/epel/6/x86\_64/epel-release-6-7.noarch.rpm
>
> rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm

Now we'll add nginx to the config so it knows about the different repo:

> vim /etc/yum.repos.d/nginx.repo

Input and save

> \[nginx\]  
> name=nginx repo  
> baseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/  
> gpgcheck=0  
> enabled=1

Install the modules. When it asks to download new modules accept by
typing "y"

> yum --enablerepo=remi,remi-test install nginx php php-fpm
> php-common php-pear php-pdo php-mysql php-pgsql
> php-pecl-memcache php-gd php-mbstring php-mcrypt php-xml

It might not work with php-mcrypt and say that it cannot download it. If
that's the case remove it from the previous statement.

> yum --enablerepo=remi,remi-test install nginx php php-fpm
> php-common php-pear php-pdo php-mysql php-pgsql
> php-pecl-memcache php-gd php-mbstring php-mcrypt php-xml

Then run this:

wget
http://dl.fedoraproject.org/pub/epel/5/x86\_64/libmcrypt-2.5.7-5.el5.x86\_64.rpm
