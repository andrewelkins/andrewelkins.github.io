Title: Find the collation of all tables within a mysql database
Date: 2013-04-29 10:32
Author: Andrew Elkins
Category: mysql, Programming
Slug: find-the-collation-all-tables-mysql
Status: published

Needing to find a collation of a mysql database for a migration I went
to google. Found several options, but the best was one from [stack
overflow](http://stackoverflow.com/questions/4948356/query-to-show-all-tables-and-their-collation).

~~~~

SELECT TABLE\_CATALOG, TABLE\_SCHEMA, TABLE\_NAME, COLUMN\_NAME,
COLLATION\_NAME

FROM INFORMATION\_SCHEMA.COLUMNS;

~~~~

This will output something like:

~~~~

mysql&gt; SELECT TABLE\_CATALOG, TABLE\_SCHEMA, TABLE\_NAME,
COLUMN\_NAME, COLLATION\_NAME  
-&gt; FROM INFORMATION\_SCHEMA.COLUMNS;  
+---------------+--------------------+---------------------------------------+-------------------------------+-------------------+  
| TABLE\_CATALOG | TABLE\_SCHEMA | TABLE\_NAME | COLUMN\_NAME |
COLLATION\_NAME |  
+---------------+--------------------+---------------------------------------+-------------------------------+-------------------+  
| NULL | information\_schema | CHARACTER\_SETS | CHARACTER\_SET\_NAME |
utf8\_general\_ci |  
| NULL | information\_schema | CHARACTER\_SETS | DEFAULT\_COLLATE\_NAME
| utf8\_general\_ci |  
| NULL | information\_schema | CHARACTER\_SETS | DESCRIPTION |
utf8\_general\_ci |  
| NULL | information\_schema | CHARACTER\_SETS | MAXLEN | NULL |  
| NULL | information\_schema | COLLATIONS | COLLATION\_NAME |
utf8\_general\_ci |  
| NULL | information\_schema | COLLATIONS | CHARACTER\_SET\_NAME |
utf8\_general\_ci |  
| NULL | information\_schema | COLLATIONS | ID | NULL |  
| NULL | information\_schema | COLLATIONS | IS\_DEFAULT |
utf8\_general\_ci |  
| NULL | information\_schema | COLLATIONS | IS\_COMPILED |
utf8\_general\_ci |  
| NULL | information\_schema | COLLATIONS | SORTLEN | NULL |  
| NULL | information\_schema | COLLATION\_CHARACTER\_SET\_APPLICABILITY
| COLLATION\_NAME | utf8\_general\_ci |  
| NULL | information\_schema | COLLATION\_CHARACTER\_SET\_APPLICABILITY
| CHARACTER\_SET\_NAME | utf8\_general\_ci |  
| NULL | information\_schema | COLUMNS | TABLE\_CATALOG |
utf8\_general\_ci |  
| NULL | information\_schema | COLUMNS | TABLE\_SCHEMA |
utf8\_general\_ci |

\[...\]

| NULL | information\_schema | VIEWS | SECURITY\_TYPE |
utf8\_general\_ci |  
| NULL | information\_schema | VIEWS | CHARACTER\_SET\_CLIENT |
utf8\_general\_ci |  
| NULL | information\_schema | VIEWS | COLLATION\_CONNECTION |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_commentmeta | meta\_id | NULL |  
| NULL | test\_db\_wp | wp\_commentmeta | comment\_id | NULL |  
| NULL | test\_db\_wp | wp\_commentmeta | meta\_key | utf8\_general\_ci
|  
| NULL | test\_db\_wp | wp\_commentmeta | meta\_value |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_ID | NULL |  
| NULL | test\_db\_wp | wp\_comments | comment\_post\_ID | NULL |  
| NULL | test\_db\_wp | wp\_comments | comment\_author |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_author\_email |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_author\_url |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_author\_IP |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_date | NULL |  
| NULL | test\_db\_wp | wp\_comments | comment\_date\_gmt | NULL |  
| NULL | test\_db\_wp | wp\_comments | comment\_content |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_karma | NULL |  
| NULL | test\_db\_wp | wp\_comments | comment\_approved |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_agent |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_comments | comment\_type | utf8\_general\_ci
|  
| NULL | test\_db\_wp | wp\_comments | comment\_parent | NULL |  
| NULL | test\_db\_wp | wp\_comments | user\_id | NULL |  
| NULL | test\_db\_wp | wp\_links | link\_id | NULL |  
| NULL | test\_db\_wp | wp\_links | link\_url | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_name | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_image | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_target | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_category | NULL |  
| NULL | test\_db\_wp | wp\_links | link\_description |
utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_visible | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_owner | NULL |  
| NULL | test\_db\_wp | wp\_links | link\_rating | NULL |  
| NULL | test\_db\_wp | wp\_links | link\_updated | NULL |  
| NULL | test\_db\_wp | wp\_links | link\_rel | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_notes | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_links | link\_rss | utf8\_general\_ci |  
| NULL | test\_db\_wp | wp\_options | option\_id | NULL |  
| NULL | test\_db\_wp | wp\_options | option\_name | utf8\_general\_ci
|  
| NULL | test\_db\_wp | wp\_options | option\_value | utf8\_general\_ci
|

~~~~

The first part of this shows the overall database collation. In this
case, it is utf8\_general\_ci.

Then the second part shows the collation per column with each table
within the database. In this case they are all the same as the default.
However, it should be noted that this isn't always the case. It can be
different then the default.
