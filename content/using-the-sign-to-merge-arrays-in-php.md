Title: Using the + sign to merge arrays in php
Date: 2012-02-13 17:15
Author: Andrew Elkins
Category: Programming
Slug: using-the-sign-to-merge-arrays-in-php
Status: published

Today came across code that used the + sign to merge two associative php
arrays. At first I thought it was broken but turns out you can indeed
merge two arrays with the + sign.

> \$album = array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> );  
> \$album\_meta\_data = array(  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> );
>
> \$output = \$album + \$album\_meta\_data;
>
> --------OUTPUT--------  
> array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> )

Another way to use it would be to add the album meta data directly to
the album array.

> \$album = array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> );  
> \$album\_meta\_data = array(  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> );
>
> \$album += \$album\_meta\_data;
>
> --------OUTPUT--------  
> array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> )

If the key exists in both arrays then the first if used and the second
is discarded, same as with
[array\_merge](http://php.net/manual/en/function.array-merge.php).

> \$album = array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> );  
> \$album\_meta\_data = array(  
> 'title' =&gt; 'Coldplay',  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> );
>
> \$album += \$album\_meta\_data;
>
> --------OUTPUT--------  
> array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> )

the reverse

> \$album = array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Radiohead',  
> );  
> \$album\_meta\_data = array(  
> 'title' =&gt; 'Coldplay',  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> );
>
> \$album\_meta\_data += \$album;
>
> --------OUTPUT--------  
> array(  
> 'title' =&gt; 'King of Limbs',  
> 'band' =&gt; 'Coldplay',  
> 'upc' =&gt; '486898161589',  
> 'price' = '11.98'  
> )
