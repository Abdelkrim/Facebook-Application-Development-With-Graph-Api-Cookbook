from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from fbapp.views import MainPage
from fbapp.afterregistration import AfterRegistration
   
application = webapp.WSGIApplication([('/', MainPage),
                                      ('/AfterRegistration', AfterRegistration),
                                      ], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()