Title: HTML5 WebSockets - Presented by Scott Mattocks
Date: 2011-11-09 06:19
Author: Andrew Elkins
Category: Events
Slug: html5-websockets-presented-by-scott-mattocks
Status: published

This was the first talk I went to at ZendCon. The provided description:

> The emergence of HTML 5 and related technologies opens up a new world
> of possibilities for web applications. Among those new technologies
> are WebSockets, which allow for bi-directional communication between
> the browser and the server. This session will introduce WebSockets by
> exploring a few practical applications before diving into the
> JavaScript API and the WebSocket communication protocol.

What I gained most from the talk was when he talked about websockets. In
a gross generalization, they can be used to replace some common
applications of ajax communication between the server and the client.
Instead of using long polling in a web application, which
has unnecessary overhead when sending small bits of data, using a web
socket connection for the communication is a better solution.

Web socket communication requires work on both the server side and
client side to enable the two way communication.

On the client side, like ajax, it relies heavily on javascript.
Processes information in a similar fashion to AJAX. Web sockets at it's
heart is about the communication of data between the server and client.
There's some work on the client side to allow the setting up and
maintaining of the connection, but really less than with a long polling
ajax setup.

On the server side it's a little bit more work. The original request for
a connection is sent over the standard http port for the site. Then the
web socket server will respond with the port to set the connection up
with the web socket server.

 

More Information:

-   [Web Socket Browser Test](http://websocket.org/echo.html)
-   [Web Socket
    Tutorial ](http://net.tutsplus.com/tutorials/javascript-ajax/start-using-html5-websockets-today/)
-   [Nodejs Websocket Server
    Test](https://github.com/remy/html5demos/tree/master/server/)
-   [Slides](http://spoutserver.com/talks/websockets.html#slide1)

