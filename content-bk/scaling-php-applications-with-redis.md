Title: Scaling PHP Applications with Redis
Date: 2011-11-24 12:00
Author: Andrew Elkins
Category: Events
Slug: scaling-php-applications-with-redis
Status: published

Redis is an important technology when dealing with caching. This was one
of the talks that I really wanted to attend at ZendCon. It was given by
[Josh Butts](http://twitter.com/#!/jimbojsb) of Vertive LLC.

> Redis is a NoSQL technology that rides a fine line between database
> and in-memory cache. Redis also offers "remote data structures", which
> gives it a significant advantage over other in-memory databases. This
> session will cover several PHP clients for Redis, and how to use them
> for caching, data modeling and generally improving application
> throughput.

[Redis](http://redis.io/) is an open source in memory key value store
with optional persistance. The current version is 2.4.2 as of this
writing. The latest stable version is 2.2.15 which what Josh recommended
as the minimum version you would want to use. He noted that 2.4 was
pretty stable in it's own right. Hoever, I have notice that since 2.4.0
release 10 days ago they have already release 2 patches (now at 2.4.2).
Thus, personally, unless a feature of 2.4 is necessary I'd say go with
2.2 latest or 2.3 latest.

Once Redis is installed how to connect to it becomes an issue. According
to Josh, there's not a good GUI tool to use with Redis. Instead it's
best to use the command line interface.

On the actual functioning of Redis, it functions on hash keys. Think of
it like associative arrays in PHP. However, there's a huge difference.
There is NO nesting. The array is only one level deep.

As far as connecting PHP to Redis there's two options that Josh
mentioned. Rediska and Predis.

[Rediska](http://rediska.geometria-lab.net/) is compatible with PHP 5.2+
and Zend Framework 1.x. A huge feature is the profiler. It allows you to
understand how your application is using Redis and optimize it from
there. Another positive is Rediska has native session handling.

[Predis](https://github.com/nrk/predis/wiki) is built for PHP 5.3+
giving it  the ability to being developed for the future and not being
locked in to older technology. It has profiling and lazy connections to
the redis server.

Josh's recommendation between the two was use Predis if you have 5.3
available to you, but Rediska was okay too. It seemed that one of his
main reason behind this was Predis has been seeing more recent activity
and was thus more likely to be maintained in the future.

My take, at the moment, is also to go with Predis since it seems like a
more active project. It also looks as if it is looking forward and being
developed for feature redis improvements. I haven't had an opportunity
to actively  test between the two, so my decision is temporary until I
have the opportunity to factually compare instead of going on hunches.
