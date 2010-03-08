FavIcon Locator Service
=======================

about
-----

Finding out the favicon of a site is a bit of a pain.  You have to hit the site and look for the link tag in the HTML, if that exists, you have to go try to get the destination object, if that 404's or there wasn't a link tag you can look at /favicon.ico and see if it's there.  All in all, to render a highly performant page, you don't want to do all of that.

This service provides two highly cached services.  Firstly you can use it instead of a favicon and it will return the image, meaning that you can render an img tag in HTML with it, and the users browser will do all that work.  This alone is not unique, there are at least 3 other services that do this.  But the extra service provided here is that you can also merely ask the service where the destination sites favicon is actually located, and it will tell you, in json, xml, html, or plain-text as you wish.

Examples
--------

<img src="http://faviconlocator.appspot.com/img/www.guardian.co.uk">

JSON
----
http://faviconlocator.appspot.com/json/www.guardian.co.uk => {"location": "www.guardian.co.uk/favicon.ico"}

JSONP
-----
http://faviconlocator.appspot.com/json/www.guardian.co.uk?callback=f1 => f1({"location": "www.guardian.co.uk/favicon.ico"});

XML
---
http://faviconlocator.appspot.com/xml/www.guardian.co.uk => <favicon><location>www.guardian.co.uk/favicon.ico</location></favicon>

