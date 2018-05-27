Title: Clear Laravel 4 Autoload
Date: 2013-01-21 21:02
Author: Andrew Elkins
Category: Linux, PHP
Tags: composer, lavarel, php
Slug: clear-laravel-4-autoload
Status: published

Laravel 4 currently has a very frustrating issue. If you add a model it
will not know of it until you clear the autoload.

\[ps\]composer dump-autoload\[/ps\]

Make sure you have [setup composer to be accessed
globally](http://andrewelkins.com/programming/php/setting-up-composer-globally-for-laravel-4/).
Otherwise you'll need to do this command.

\[ps\]/usr/local/bin/composer.phar composer dump-autoload\[/ps\]

Further you may want to optimize your autoload. According to Taylor this
can speed up your application by 30%.  
\[ps\]composer dump-autoload --optimize\[/ps\]

Edit: Another option noted
by [luviyo](http://www.livefyre.com/profile/11398455/) is to do the
following.

Open *app/starts/global.php* and add:

\[ps\]ClassLoader::addDirectories(array( app\_path().'/libraries',
));\[/ps\]

Thanks for the tip!
