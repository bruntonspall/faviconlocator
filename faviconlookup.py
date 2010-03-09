#
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup
import logging
import urlparse
import helpers

def find_favicon(html):
    soup = BeautifulSoup(html)
    icons = soup.findAll('link', rel="shortcut icon")
    if icons:
        return [v for k,v in icons[0].attrs if k=='href'][0]
    icons = soup.findAll('link', rel="icon")
    if icons:
        return [v for k,v in icons[0].attrs if k=='href'][0]
    return None

def format_url(url):
    if not url.startswith('http://'):
        return 'http://'+url
    return url

def fetch_url(url):
    logging.info("Fetching: %s" % (format_url(url)))
    result = urlfetch.fetch(format_url(url))
    logging.info("Got %d response code" % (result.status_code))
    if is_valid_response(result.status_code):
        return result
    return None

def is_valid_response(code):
    if code / 100 == 2 or code / 100 == 3:
        return True
    return False

@helpers.autocached   
def getfavicon(url):
    logging.info("Working out favicon for %s" % (url))
    result = fetch_url(url)
    favicon_url = None
    if result:
        favicon_url = find_favicon(result.content)
    if favicon_url:
        if favicon_url.startswith('/'):
            favicon_url = url+favicon_url
        if fetch_url(favicon_url):
            return favicon_url
   
    # At this point try site/favicon.ico
    if not url.endswith('/favicon.ico'):
        default_url = urlparse.urlparse(format_url(url)).netloc+"/favicon.ico"
        result = fetch_url(default_url)
        if result:
            return default_url

