Title: MySQL 5.5+
Date: 2011-11-03 22:27
Author: Andrew Elkins
Category: Events
Slug: mysql-5-5
Status: published

The MySQL talk was given by Dave Stokes of Oracle. He's the MySQL
community manager. The ZendCon summary:

> MySQL had been evolving since the Oracle take over in 2010. This
> session will cover how new features like multi-threaded replication,
> InnoDB-Memcached plugin for NoSQL data access, or having InnoDB as the
> default storage engine will change life for PHP developers. Learn how
> partitioning and new performance metrics will allow allow better
> access speed and more control over your MySQL instances.

This talk was about the improvements with MySQL since the take over by
Oracle. Many in the community feared the Oracle take over, but in
reality it has been good for MySQL.

They are adding huge features to MySQL

-   Massive improvements for MySQL on Windows
-   RTMF method to setup replication
-   More secure
-   Innodb improvements

<div>

The key feature I was concern/interested in was the InnoDB improvements.
Something I ws unaware of since Oracle bought MySQL they brought
together the InnoDB team and MySQL Team leading to much tighter
integration and quicker bug fixes. It's also leading to adding features
to speed it up.

</div>

<div>

</div>

<div>

The new feature I was unaware of was the creation of nosql-style
memcached api access of the data. I haven't had a chance to use it in
practice but in theory this seems like an awesome step for MySQL.

</div>

<div>

</div>

<div>

On security, MySQL is doing more to protect/ensure data durability.
Meaning that the data will store correctly and be retrived each time.
Hoever, this does not replace developers escaping input. He restated
again and again, "Escape your data", "Escape your data", "Escape your
data". As a developer, do not trust users. Simple as that.

</div>

I was able to connect with Dave and get the slides. You can download
them below.

Download slides -&gt; [MySQL update
Zendcon](http://localhost/andrewelkins/wp-content/uploads/2011/11/MySQLupdateZendcon.ppt)
