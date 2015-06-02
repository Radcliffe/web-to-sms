SEND_MESSAGES = True

import webapp2
from models import Message
from secrets import TWILIO_NUMBER, ACCOUNT_SID, AUTH_TOKEN, API_KEY
from twilio.rest import TwilioRestClient
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from phonenumbers import parse, is_valid_number
from webapp2_extras import sessions

twilio_client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def standardize_phone_number(number):
    try:
        p = parse(number, 'US')
        if is_valid_number(p):
            return "+%d%d" % (p.country_code, p.national_number)
    except:
        pass
 
def log_message(to, body):
    message = Message(parent=ndb.Key('Messages', 'messages'),
                       to=to, body=body)
    message.put()


class MessageHandler(webapp2.RequestHandler):
    def post(self):
        api_key = self.request.get('api-key')
        if api_key != API_KEY:
            error = {'message': 'Invalid key'}
            self.response.write(template.render('form.html', error))
            return
        to = self.request.get('to')
        to = standardize_phone_number(to)
        if to is None:
            error = {'message': 'Invalid phone number'}
            self.response.write(template.render('form.html', error))
            return
        body = self.request.get('body')
        if SEND_MESSAGES:
            twilio_client.messages.create(
                to = to, 
                from_ = TWILIO_NUMBER,
                body = body)
        else:
            print "Send message to %s: %s" % (to, body)
        log_message(to, body)
        self.redirect('/compose')
        
    def get(self):
        return post(self)
        
      
        
app = webapp2.WSGIApplication([
    ('/send', MessageHandler),
], debug=True)
