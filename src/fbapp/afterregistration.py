'''
Created on Mar 24, 2012

@author: aboujraf
'''

from google.appengine.dist import use_library
from fbapp.constants import FB_APP_ID
use_library('django', '1.2')
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os

class AfterRegistration(webapp.RequestHandler):
    def get(self):
        template_values = {'FB_APP_ID' : FB_APP_ID }
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'afterregistration.html')
        self.response.out.write(template.render(path, template_values))