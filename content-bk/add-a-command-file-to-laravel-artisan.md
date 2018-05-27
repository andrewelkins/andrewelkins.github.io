Title: Add a command file to Laravel artisan
Date: 2013-02-26 13:15
Author: Andrew Elkins
Category: Linux, PHP, Programming
Tags: artisan, cli, command line, l4, laravel
Slug: add-a-command-file-to-laravel-artisan
Status: published

In order to run a custom command from the command line utility called
artisan you need to do two things:

1.  Create a new CustomCommand file
2.  Register that command with artisan

Here's a sample Command file called *FooCommand.php* which should be
placed in *app/commands/ *

\[php\]&lt;?php

use Illuminate:::ConsoleCommand;  
use Symfony:::ComponentConsole:::InputInputOption;  
use Symfony:::ComponentConsole:::InputInputArgument;

class FooCommand extends Command {

/\*\*  
\* The console command name.  
\*  
\* @var string  
\*/  
protected \$name = 'foo:migrate';

/\*\*  
\* The console command description.  
\*  
\* @var string  
\*/  
protected \$description = '';

/\*\*  
\* Create a new command instance.  
\*  
\* @return void  
\*/  
public function \_\_construct()  
{  
parent::\_\_construct();  
}

/\*\*  
\* Execute the console command.  
\*  
\* @return void  
\*/  
public function fire()  
{  
\$this-&gt;info(' Step: 1');  
\$this-&gt;info(' Cool Stuff Here');

}

}\[/php\]

Then you'll need to register that in *app/start/artisan.php*

\[php\]

&lt;?php  
/\*  
|--------------------------------------------------------------------------  
| Register The Artisan Commands  
|--------------------------------------------------------------------------  
|  
| Each available Artisan command must be registered with the console so  
| that it is available to be called. We'll register every command so  
| the console gets access to each of the command object instances.  
|  
\*/

Artisan::add(new FooCommand);  
\[/php\]

Now you can run your command

\[ps\]php artisan foo:migrate\[/ps\]
