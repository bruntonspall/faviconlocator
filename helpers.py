import os
import datetime
import random

from google.appengine.ext.webapp import template
from google.appengine.api.labs import taskqueue
from google.appengine.api import memcache
from google.appengine.api import users

import logging
import functools

def autocached(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        name = method.__name__+str(args)+str(kwargs)
        data = memcache.get(name)
        if not data:
            logging.info("CACHE MISS for "+name)
            data = method(self, *args, **kwargs)
            memcache.set(name, data, 60*60*24)
        return data
    return wrapper

def cached(name, timeout=60):
    def wrapper(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            data = memcache.get(name)
            if not data:
                logging.info("CACHE MISS for "+name)
                data = method(self, *args, **kwargs)
                memcache.set(name, data, timeout)
            return data
        return wrapper
    return wrapper

def set_content_type(content_type):
    def wrapper(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            self.response.headers["Content-Type"] = content_type
            return method(self, *args, **kwargs)
        return wrapper
    return wrapper

def write_response(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self.response.out.write(method(self, *args, **kwargs))
    return wrapper
   

def render_admin_template(self, end_point, template_values):
    user = users.get_current_user()
    if user:
        template_values['greeting'] = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                    (user.nickname(), users.create_logout_url("/admin/")))

    return render_template(self, end_point, template_values)

def render_template(self, end_point, template_values):
    path = os.path.join(os.path.dirname(__file__), "templates/" + end_point)
    return template.render(path, template_values)
