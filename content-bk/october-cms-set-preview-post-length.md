Title: October CMS set preview post length
Date: 2014-10-07 09:05
Author: Andrew Elkins
Category: octobercms, PHP, Programming
Slug: october-cms-set-preview-post-length
Status: published

October CMS is a brilliant new developer focused CMS. It reminds me of
working on XenForo in it's ease of creating add-ons. A very nice system.

After configuring the blog I needed to limit the post except size for
post that didn't have an except. This meant shrinking the normal content
on category list view and post list view. It turned out to be simple.

First open both the blog list template and category list template. Find
the code tab and click it.

Then add this:

~~~~  
function onEnd()  
{  
if (isset(\$this\['posts'\]))  
foreach(\$this\['posts'\] as &\$post) {  
\$post-&gt;content\_html = wordwrap(\$post-&gt;content\_html, 250);  
\$post-&gt;content\_html = explode("~~~~n", \$post-&gt;content\_html);  
\$post-&gt;content\_html = \$post-&gt;content\_html\[0\] . '...';  
}  
}  
~~~~

Before is display it'll be parsed and limited. The code is a bit of code
that I modified from SO. I'd link back but can't find the source thread
anymore.
