Title: October CMS How to replace component templates from plugins
Date: 2014-10-07 10:34
Author: Andrew Elkins
Category: octobercms, PHP, Programming
Slug: october-cms-how-to-replace-component-templates-from-plugins
Status: published

How can you replace component templates from plugins? IE I want to
replace the posts default template in the blog plugin with my own
markup. [Post List from the blog
plugin](https://github.com/rainlab/blog-plugin/blob/master/components/posts/default.htm)

-- Edit --

Use the override of a template instead.
<https://octobercms.com/docs/cms/components#overriding-partials>

-- Old way --

Turns out it is easy, just copy and paste in to your own partial. I
typically name mine prefixed with the plug-in.
"blog-plugin/post-list.htm"

Then just modify to your specs and insert in the page.

Originally:  
~~~~  
{% component 'blogPosts' %}  
~~~~  
Becomes:  
~~~~  
{% partial 'blog-plugin/posts-list.htm' %}  
~~~~

See the comments below for other solutions. In the
[docs](https://octobercms.com/docs/cms/components#overriding-partials)
it notes that you can override the partial that is used.
