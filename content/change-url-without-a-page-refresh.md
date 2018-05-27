Title: Change url without a page refresh
Date: 2013-01-22 01:33
Author: Andrew Elkins
Category: js
Slug: change-url-without-a-page-refresh
Status: published

I wanted the url to change but there to be no redirect/refresh of the
page. I was able to do this by a little js.

> history.pushState('data', '', 'http://' + window.location.host +
> '/month/' + month );
