from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os

APP_URL = 'http://alt-f1-social-graph.appspot.com'
FB_APP_ID = '311556765573729'
SITE = 'alt-f1-social-graph.appspot.com'
FB_LOGIN_SCOPE='user_likes,user_about_me,user_birthday,user_education_history,email,user_hometown,user_relationship_details,user_location,user_religion_politics,user_likes,user_likes,user_about_me,user_relationships,user_religion_politics,user_relationships,user_website,user_work_history'
URL_TO_LOAD_AFTER_REGISTRATION = APP_URL + '/AfterRegistration'

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {'APP_URL': APP_URL,
                           'FB_APP_ID': FB_APP_ID,
                           'SITE': SITE,
                           'FB_LOGIN_SCOPE': FB_LOGIN_SCOPE,
                           'URL_TO_LOAD_AFTER_REGISTRATION': URL_TO_LOAD_AFTER_REGISTRATION }
        path = os.path.join(os.path.dirname(__file__), 'templates','index.html')
        self.response.out.write(template.render(path, template_values))

class AfterRegistration(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'templates','afterregistration.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication([('/', MainPage),
                                      ('/AfterRegistration', AfterRegistration),
                                      ], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()