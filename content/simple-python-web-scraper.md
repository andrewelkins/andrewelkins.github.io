Title: Simple Python Web Scraper
Date: 2016-02-22 10:52
Author: Andrew Elkins
Category: Linux, PHP, Programming, python
Slug: simple-python-web-scraper
Status: published

I needed a simple html only scraper. (This doesn't use js, won't pull
down data via AJAX). I found an example on another site,
[thetaranights.com](http://www.thetaranights.com/web-mining-login-to-any-website-using-mechanize-module-in-python/),
but it wasn't exactly what I needed. It only pulled the data and printed
it to screen. I added a list to loop through and auto saving by url name
to a html file.

~~~~  
import mechanize \#pip install mechanize

br = mechanize.Browser()  
br.set\_handle\_robots(False)  
br.addheaders = \[(&quot;User-agent&quot;,&quot;Mozilla/5.0 (X11; U;
Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick)
Firefox/3.6.13&quot;)\]

sign\_in = br.open(&quot;https://this.example.com/login&quot;) \#the
login url

br.select\_form(nr = 0) \#accessing form by their index. Since we have
only one form in this example, nr =0.  
\#br.select\_form(name = &quot;form name&quot;) Alternatively you may
use this instead of the above line if your form has name attribute
available.

br\[&quot;email&quot;\] = &quot;email or username&quot; \#the key
&quot;username&quot; is the variable that takes the username/email value

br\[&quot;password&quot;\] = &quot;password&quot; \#the key
&quot;password&quot; is the variable that takes the password value

logged\_in = br.submit() \#submitting the login credentials

logincheck = logged\_in.read() \#reading the page body that is
redirected after successful login

urls =
\[&quot;https://this.example.com/some/page&quot;,&quot;https://this.example.com/some/page2&quot;\]

for url in urls:  
req = br.open(url).read()  
filename = url.split('/')\[-1\] + &quot;.html&quot;  
f = open(filename, 'w')  
f.write(req)  
f.close()

~~~~

Which produces 2 files:  
page.html  
page2.html
