SEND_MESSAGES = True

import webapp2
from models import Message
from secrets import TWILIO_NUMBER, ACCOUNT_SID, AUTH_TOKEN
from twilio.rest import TwilioRestClient
from google.appengine.api import users
from google.appengine.ext import ndb
import re

twilio_client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def standardize_phone_number(number):
    number = re.sub('[ \-()]', '', number)
    if number.isdigit() and len(number) == 10:
        return '+1' + number
    return number

def log_message(to, body):
    message = Message(parent=ndb.Key("Messages", "messages"),
                       to=to, body=body)
    message.put()
    print "message logged"


class MessageHandler(webapp2.RequestHandler):
    def post(self):
            to = self.request.get('to')
            to = standardize_phone_number(to)
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
      
        
app = webapp2.WSGIApplication([
    ('/send', MessageHandler),
], debug=True)
