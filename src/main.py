from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from fbapp.views import MainPage, AfterRegistration, FBCanvasFluid

   
application = webapp.WSGIApplication([('/', MainPage),
                                      ('/AfterRegistration', AfterRegistration),
                                      ('/FBCanvasFluid', FBCanvasFluid),
                                      ], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
