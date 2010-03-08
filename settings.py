# These are global settings
import logging

try:
    from settings_local import *
except ImportError:
    logging.error("Failed to import settings_local, Usernames and Passwords may not work")
    pass

