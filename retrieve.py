import webapp2
from secrets import API_KEY
from models import Message
import json
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

class RetrieveMessages(webapp2.RequestHandler):
    def get(self):
        api_key = self.request.get('api-key')
        if api_key != API_KEY:
            self.response.write('Invalid key')
            return
        to = self.request.get('to')
        body = self.request.get('body')
        
        ancestor_key = ndb.Key('Messages', 'messages')
        query = Message.query(ancestor=ancestor_key).order(-Message.date)
        if to:
           query = query.filter(Message.to == to)
        print type(query)
        messages = [dict(to=msg.to,
                     body=msg.body,
                     date=msg.date.isoformat()) for msg in query if body in msg.body]
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(messages))
        
app = webapp2.WSGIApplication([
    ('/retrieve', RetrieveMessages),
], debug=True)            
 
        
