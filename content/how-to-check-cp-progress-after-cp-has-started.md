Title: How to check cp progress after cp has started
Date: 2015-11-02 11:02
Author: Andrew Elkins
Category: Command Line, Linux
Slug: how-to-check-cp-progress-after-cp-has-started
Status: published

First, the easier way to do this is to use rsync in the first place.

> rsync -avh --progress sourceDirectory destinationDirectory

However, sometime you think cp will be quick and you already kicked it
off. Here is a quick way to check the progress of a copy command after
you've already started.

> watch lsof -p\`pgrep -x cp\`

This will let you know what it is transferring and how much it has left
to do. In a way it provides a way to check the progress of the cp,
copy comand.

To find out more check out these two SO links:

[Check
progress](http://unix.stackexchange.com/questions/66795/how-to-check-progress-of-running-cp)

[CP Command
Help](http://unix.stackexchange.com/questions/65077/is-it-possible-to-see-cp-speed-and-copied)
