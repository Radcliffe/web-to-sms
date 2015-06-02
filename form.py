import webapp2
import jinja2
from twilio.rest import TwilioRestClient
import cgi
from google.appengine.api import users
from google.appengine.ext import ndb
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FormHandler(webapp2.RequestHandler):
    def get(self):
        print "1"
        template = JINJA_ENVIRONMENT.get_template('form.html')
        print "2"
        self.response.write(template.render())
        print "3"


app = webapp2.WSGIApplication([
    ('/compose', FormHandler),
], debug=True)
