Title: How to specify specific engine in Laravel 4 migration
Date: 2013-04-24 20:54
Author: Andrew Elkins
Category: PHP, Programming
Slug: how-to-specify-specific-engine-in-laravel-4-migration
Status: published

Earlier today I needed to set up a specific database engine for a mysql
table that wasn't the databases's default. In this instance, the default
was INNODB and I needed it to be MyISAM. We could discuss the reasons
why I shouldn't use MyISAM but in this instance that's what I needed.

It's fairly straight forward. Take the following example migration
block.  
~~~~

'mysql' =&gt; array(  
'driver' =&gt; 'mysql',  
'host' =&gt; 'hostname',  
'database' =&gt; 'database\_name',  
'username' =&gt; 'username',  
'password' =&gt; 'password\_here',  
'charset' =&gt; 'utf8',  
'collation' =&gt; 'utf8\_unicode\_ci',  
'prefix' =&gt; '',  
),

~~~~

Then just add the engine configuration.

~~~~

'mysql' =&gt; array(  
'engine' =&gt; 'MYISAM',  
'driver' =&gt; 'mysql',  
'host' =&gt; 'hostname',  
'database' =&gt; 'database\_name',  
'username' =&gt; 'username',  
'password' =&gt; 'password\_here',  
'charset' =&gt; 'utf8',  
'collation' =&gt; 'utf8\_unicode\_ci',  
'prefix' =&gt; '',  
),

~~~~

\*\*UPDATE\*\*  
Thanks @unisys12 for the comment. This needed to be updated for the
Blueprint code in Laravel.  
Your "up" method might look like:  
~~~~

public function up()  
{  
// Create the \`Posts\` table  
Schema::create('posts', function(\$table)  
{  
\$table-&gt;increments('id')-&gt;unsigned();  
\$table-&gt;integer('user\_id')-&gt;unsigned();  
\$table-&gt;string('title');  
\$table-&gt;string('slug');  
\$table-&gt;text('content');  
\$table-&gt;timestamps();  
});  
}  
~~~~

In order to add the table type, you'll need to do this:  
~~~~

public function up()  
{  
// Create the \`Posts\` table  
Schema::create('posts', function(\$table)  
{  
\$table-&gt;engine = 'MYISAM';  
\$table-&gt;increments('id')-&gt;unsigned();  
\$table-&gt;integer('user\_id')-&gt;unsigned();  
\$table-&gt;string('title');  
\$table-&gt;string('slug');  
\$table-&gt;text('content');  
\$table-&gt;timestamps();  
});  
}  
~~~~
