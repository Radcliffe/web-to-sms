from google.appengine.ext import ndb


class Message(ndb.Model):
    to = ndb.StringProperty()
    body = ndb.StringProperty()
    date =  ndb.DateTimeProperty(auto_now_add=True)
