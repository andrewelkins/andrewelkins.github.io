Title: How to call a python function by using a variable python
Date: 2015-01-23 11:07
Author: Andrew Elkins
Category: Linux, Programming, python
Slug: how-to-call-a-python-function-by-using-a-variable-python
Status: published

I needed to, in a programmatic way, determine the function name and then
call the function.

Here's an example use case. I have a bunch of functions called,
\["function1", "function2", "function3", "function4", etc\] Then I have
a function that takes a number as a param. Then should return the proper
function.

~~~~  
class my\_awesome\_class():  
def function1(self, number):  
\# do something cool  
pass

def function2(self, number):  
\# do something cool  
pass

\[...\]

def test\_function(self, number, data):  
function\_string = ''.join(\['function',str(number)\])  
try:  
t = getattr(my\_awesome\_class(), function\_string)  
return t  
except AttributeError:  
print 'function not found "%s" (%s)' % (function\_string, data)  
~~~~
