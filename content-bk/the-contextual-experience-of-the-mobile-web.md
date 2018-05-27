Title: The Contextual Experience of the Mobile Web
Date: 2011-10-29 22:29
Author: Andrew Elkins
Category: Events
Slug: the-contextual-experience-of-the-mobile-web
Status: published

The contextual experience on the web was a talk by Jeff Carouth of Texas
A&M University. The ZendCon summary:

> The great native apps vs mobile web debate will live on for a little
> while longer, but more and more we are realizing that we can get the
> best of both worlds with mobile web apps. However, there is an
> expectation of context on mobile devices, and ignoring that experience
> expectation is a mistake. Let's look at the contextual experience of
> the mobile web.

My summary would be history of developing for a mobile client and
the emergence of adaptive design as a solution.

One of the interesting points that he brought up was something that had
been going around my office lately as well.

> What determines a mobile client?

Meaning an iPad and netbook have the same resolution, which one is
mobile? Both? iPad only?

Within CSS3 theres specification for media queries. One of these queries
that we use is to base the design on resolution. In doing so you are
basing the display on the size of screen. At the outset this seems like
a great idea. However, there is a drawback. The design to fit the size
doesn't account for data size. You could design a photo heavy site to
fit in a 600 wide window but if you don't compensate for data size
performance on a 3G network user experience will still suck. So while
media queries are part of the answer they are not all of the answer.

To fix the second part, one option discussed was image compression or
replacement. For compression there's JS resizing. It works but it is
ugly. You look at that code and the processing overhead and cringe.

Then there's responsive images, downloading a small image and replacing
it with a higher quality one. This adds overhead and bandwidth. You're
download two images for every image on your page. Not ideal.

Ideally this should be done on the server side. The technology and/or
programs haven't been written for this yet. You'd need to inspect the
client agent and then respond with the appropriate image size and
resolution. According to him, there's not a good implementation of this
at the moment. However, I think there's vast opportunity for someone to
develop such a tool.

 
