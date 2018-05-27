Title: How to get laravel database prefix
Date: 2013-06-14 12:39
Author: Andrew Elkins
Category: PHP, Programming
Tags: db, laravel, php, prefix
Slug: how-to-get-laravel-database-prefix
Status: published

I needed to get the db prefix for a raw insert query I was running. It's
an easy function call to get the current database prefix.

~~~~

DB::getTablePrefix();

~~~~

Will output the prefix for the current database. This will work in
laravel 4.
