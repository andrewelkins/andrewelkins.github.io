Title: Bash test if file exists
Date: 2015-10-14 10:58
Author: Andrew Elkins
Category: Bash, Command Line, Linux
Slug: bash-test-if-file-exists
Status: published

Using bash I needed to check that a file exists, then do something. This
one turns out to be super simple. I wanted to conditionally load a db
file if it existed in this case.

What I needed was, a check for the file in bash. Then execute the
command. In this instance it was to load a postgres restore file.

> ``` {.bash}
> db_dump="/home/vagrant/files/db.dump"
> ```
>
> ``` {.bash}
> [ -f $db_dump ] && printf "Loading DB...\n";sudo su postgres -c "pg_restore -d db_name_here $db_dump;" || printf "No db dump to load\n"
> ```

Another way to write this is to use a full if/else conditional.
Admittedly this is a little cleaner.

> ``` {.bash}
> db_dump="/home/vagrant/files/db.dump"
> if [ -f "$db_dump" ]
> then
>     printf "Loading DB...\n";
>         sudo su postgres -c "pg_restore -d db_name_here $db_dump;"
> else
>     printf "No DB file found.\n";
> fi
> ```
