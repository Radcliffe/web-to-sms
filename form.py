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
        template = JINJA_ENVIRONMENT.get_template('form.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/compose', FormHandler),
], debug=True)
