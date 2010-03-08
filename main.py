#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.api import memcache

import helpers
import logging
import faviconlookup


class JSONHandler(webapp.RequestHandler):
    @helpers.write_response
    @helpers.autocached
    def get(self, url):
        faviconurl = faviconlookup.get(url)
        return helpers.render_template(self, 'webviews/json.html', {'faviconurl': faviconurl})


def main():
  application = webapp.WSGIApplication([
        ('/json/(.*)', JSONHandler),
        ],    debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
