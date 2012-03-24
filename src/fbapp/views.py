'''
Created on Mar 24, 2012

@author: aboujraf
'''

from constants import *

from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {'APP_URL': APP_URL,
                           'FB_APP_ID': FB_APP_ID,
                           'SITE': SITE,
                           'FB_LOGIN_SCOPE': FB_LOGIN_SCOPE,
                           'URL_TO_LOAD_AFTER_REGISTRATION': URL_TO_LOAD_AFTER_REGISTRATION }
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'index.html')
        self.response.out.write(template.render(path, template_values))

class AfterRegistration(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'afterregistration.html')
        self.response.out.write(template.render(path, template_values))