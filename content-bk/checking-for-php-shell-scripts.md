Title: Checking for php shell scripts
Date: 2013-03-07 17:13
Author: Andrew Elkins
Category: Linux, PHP
Slug: checking-for-php-shell-scripts
Status: draft

    A quick way to check for a php shell within a directory.
    [ps]
    grep -RPnDskip "(passthru|shell_exec|system|phpinfo|base64_decode|chmod|mkdir|fopen|fclose|readfile) *\(" *
    [/ps]
    Source
