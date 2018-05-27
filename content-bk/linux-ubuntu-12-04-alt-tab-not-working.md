Title: Linux Ubuntu 12.04 alt-tab not working
Date: 2013-01-09 10:10
Author: Andrew Elkins
Category: Linux
Slug: linux-ubuntu-12-04-alt-tab-not-working
Status: published

I’ve recently installed Ubuntu 12.04 Prestige Pangolin (I use Gnome
Classic), and immediately noticed that the alt+tab shortcut wasn’t
working. I tried fixing it within Applications&gt;Systems
Tools&gt;System Settings, but that did not work. I have compiz Config
Manager already install so I figured I could use that version instead
(it looks nicer anyway).

<div>

Finally, I’ve found this solution on a forum, by installing Compiz
Config Settings Manager:
</p>
1.  Go then to Applications&gt;System Tools&gt;Preferences&gt;Compiz
    Config Manager
2.  Scroll down to the bottom of the window and where it says *Windows
    Management*, click on either Application Switcher (dynamic) or
    Static Application Switcher, depending on which you prefer.

If you need to install Compiz Config Manager:

1.  Click Alt+Ctrl+T, to open the Terminal
2.  Type this: `sudo apt-get install compizconfig-settings-manager`,
3.  Or search for **compizconfig-settings-manager** in the Software
    Center and install from there.

</div>
