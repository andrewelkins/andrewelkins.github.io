Title: Remove empty values from an array.
Date: 2012-04-04 08:01
Author: Andrew Elkins
Category: Programming
Slug: remove-empty-values-from-an-array
Status: published

I developed this little one liner to remove empty values from an array
in php.

> \$tags = array( 'testtag', 'testtag2', ' ' );
>
> \$tagsCleaned = array\_filter( array\_map( 'trim', \$tags ),  
> create\_function( '\$a', 'return \$a!="";' ) );

Breaking that down inside out.

> array\_map( 'trim', \$tags )

[Array map](http://www.php.net/manual/en/function.array-map.php) the
trim function to all of the values within the array, removing removing
pre/post spaces. In this case it removes the space in the third item.

> array\_filter( array\_map( 'trim', \$tags ),  
> create\_function( '\$a', 'return \$a!="";' ) )

[Array filter](http://php.net/manual/en/function.array-filter.php)
allows us to remove the elements that do not match the function. In this
case, I've created a function to test if the value is an empty string.
If it is, the function returns true if it is not blank and false if it
is. The false return removes the value from the array.

The result will be an array of two items.

> \$tags = array( 'testtag', 'testtag2', ' ' );  
> \$tagsCleaned = array\_filter( array\_map( 'trim', \$tags ),
> create\_function( '\$a', 'return \$a!="";' ) );  
> print\_r(\$tagsCleaned);
>
>  
>
> Array  
> (  
> \[0\] =&gt; testtag  
> \[1\] =&gt; testtag2  
> )
