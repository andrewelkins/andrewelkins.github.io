Title: JS logging
Date: 2012-05-14 11:27
Author: Andrew Elkins
Category: Programming
Slug: js-logging
Status: published

I've been doing a fair about of js development lately and console.log
has been my friend. However, writing console.log() is a bit heavy. So
instead I've been adding this to my files as  a quick way to log in
javascipt.

> function log() {  
> if (window.console && console.log)  
> console.log('{product or sitename} ::  ' +
> Array.prototype.join.call(arguments,' '));  
> }
>
>  
