Title: How to add a library folder to Laravel 4
Date: 2013-02-22 14:26
Author: Andrew Elkins
Category: PHP, Programming
Tags: framework, helper, laravel, php
Slug: how-to-add-a-helper-folder-to-laravel-4
Status: published

I typically use a library folder in my projects to group of files that
you want to use in different projects but don't want to use
[Satis](http://getcomposer.org/doc/articles/handling-private-packages-with-satis.md)
to manage the contained files. This folder could also be a helper folder
for functions that are static and are mainly generic helpers but don't
quite fit in a model. So in this example I'll be adding a library folder
and have it autoloaded by Laravel. The process for a helpers folder is
the same, just replace library with helpers.

First step is to create the folder. (I assume you're already in laravel
project.)

\[ps\]cd app/

mkdir library

cd library\[/ps\]

Now we need to add the folder to the autoload file. We will return to
laravel project root and view the composer file.

\[ps\]cd ..

vim composer.json\[/ps\]

Should look something like.

\[ps\]{  
"require": {  
"laravel/framework": "4.0.\*"  
},  
"autoload": {  
"classmap": \[  
"app/commands",  
"app/controllers",  
"app/models",  
"app/database/migrations",  
"app/tests/TestCase.php"  
\]  
},  
"minimum-stability": "dev"  
}\[/ps\]

We're going to add the library directory.

\[ps\]{  
"require": {  
"laravel/framework": "4.0.\*"  
},  
"autoload": {  
"classmap": \[  
"app/commands",  
"app/controllers",  
"app/library", /\* Added here \*/  
"app/models",  
"app/database/migrations",  
"app/tests/TestCase.php"  
\]  
},  
"minimum-stability": "dev"  
}\[/ps\]

Let's reload the autoload. (Assuming [composer is an
alias.](http://andrewelkins.com/programming/php/setting-up-composer-globally-for-laravel-4/ "Setting up Composer globally for Laravel 4"))

\[ps\]composer dump-autoload\[/ps\]

Now you can use the library folder.
