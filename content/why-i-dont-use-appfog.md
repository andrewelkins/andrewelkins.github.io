Title: Why I don't use AppFog
Date: 2013-03-15 20:31
Author: Andrew Elkins
Category: Linux
Tags: appfog, linux, server
Slug: why-i-dont-use-appfog
Status: published

Simple no persistant storage. Starting up, setting up, etc are all
great, but without persistance storage I'm forced to use S3 or the like.
If I'm doing a very simple app or a WordPress install it's not worth the
effort.

Does AppFog have a persistent file system?

Not yet. We're working on this feature, but in the meantime, the file
system is volatile. This means that any changes you make to the file
system through a web interface, including any admin changes and content
uploads, will be lost on the app's next start, stop, restart, deploy, or
resource change. Because of this, you should make any changes to the
file system on a local development environment and keep media assets and
content uploads on an external storage system like Amazon's S3.

[Source](https://docs.appfog.com/faq#persistentfs)
