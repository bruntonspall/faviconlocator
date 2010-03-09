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
        return helpers.render_template(self, 'webviews/%s.html' % (type), {'faviconurl': faviconurl})

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
