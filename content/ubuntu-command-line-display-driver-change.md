Title: Ubuntu Command line Display Driver Change
Date: 2015-10-30 08:24
Author: Andrew Elkins
Category: Command Line, Linux
Slug: ubuntu-command-line-display-driver-change
Status: published

Recently upgraded to 15.10 and that looked okay at first. However, the
displa driver that it installed, NVIDIA, was causing issues. So I
defaulted back to the open source driver and reboot. MISTAKE! Ended up
causing the system to crash and couldn't do anything about it.

I rebooted into root terminal. Then ran a command to display the
available drivers.

> ubuntu-drivers devices

The spit out a list of drivers. Then I reinstalled the latest available
nvidia driver.

> apt-get install nvidia-352-updates
