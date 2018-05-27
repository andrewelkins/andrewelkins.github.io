Title: LessPHP
Date: 2012-12-09 19:59
Author: Andrew Elkins
Category: Programming
Slug: lessphp
Status: published

Why would I want to use the php version of a native node.js project?
Well, for starters not all projects are deployed on servers that have
node.js installed. Second, well, the first one is pretty much the only
reason.

So with that out of the way, I ran in an issue with bootstrap and
lessphp. LessPHP doesn't allow the js parsing that less allows. In my
case, it was with bootstrap and mixins.less.

> parse error: failed at \`@props:
> \~\`"@{arguments}".replace(/\[:::\[\]\]|:::,sX/g, '')\`

Here's the code that is causing the error.

> // Drop shadows  
> .box-shadow(@shadowA, @shadowB:X, ...){  
> // Multiple shadow solution from
> http://toekneestuck.com/blog/2012/05/15/less-css-arguments-variable/  
> @props: \~\`"@{arguments}".replace(/\[:::\[\]\]|:::,sX/g, '')\`;  
> -webkit-box-shadow: @props;  
> -moz-box-shadow: @props;  
> box-shadow: @props;  
> }

There's a way around it.

> .box-shadow(@shadow) {  
> -webkit-box-shadow: @shadow;  
> -moz-box-shadow: @shadow;  
> box-shadow: @shadow;  
> }  
> // Aliases for up to 5 shadows to avoid the need for passing in
> escaped strings  
> .box-shadow(@a, @b) { @join: @a, @b; .box-shadow(@join); }  
> .box-shadow(@a, @b, @c) { @join: @a, @b, @c; .box-shadow(@join); }  
> .box-shadow(@a, @b, @c, @d) { @join: @a, @b, @c, @d;
> .box-shadow(@join); }  
> .box-shadow(@a, @b, @c, @d, @e) { @join: @a, @b, @c, @d, @e;
> .box-shadow(@join); }

Which basically hard codes 5 gradient positions. Which could be bad if
your code uses more than that. However, I don't believe bootstrap does
so it should be fine.

 
