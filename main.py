#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.api import memcache

import helpers
import logging
import faviconlookup

class GenericHandler(webapp.RequestHandler):
    @helpers.write_response
    def get(self, type, url):
        faviconurl = faviconlookup.getfavicon(url)
        callback = self.request.get('callback')
        if type == 'json' and callback:
            type = 'jsonp'
        return helpers.render_template(self, 'webviews/%s.html' % (type), {'faviconurl': faviconurl, 'callback': callback})

class MainHandler(webapp.RequestHandler):
    @helpers.write_response
    def get(self):
        return helpers.render_template(self, 'webviews/home.html', {})

def main():
  application = webapp.WSGIApplication([
        ('^/$', MainHandler),
        ('^/([^/]*)/(.*)$', GenericHandler),
        ],    debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
