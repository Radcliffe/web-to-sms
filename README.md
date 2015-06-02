# Web to SMS

This application sends an SMS text message from a web form and logs it to
a database. It runs on Google App Engine and it uses Twilio to send text
messages.

## Sending messages

Before sending text messages, you will need to request an API key from the
author, unless you deploy the application yourself. Send a POST request
to the address http://web-to-text.appspot.com/send containing the following
parameters:

* `to` : The phone number of the recipient (assumed to be in the US)
* `api-key` : The API key (obtained from the author)
* `body` : The message text

## Retrieving messages

To retrieve the messages from the database, send a GET request to
`/retrieve` with the parameters `api-key`, `to`, and `body`. 
Only the `api-key` parameter is required. 
Results are returned in JSON format in reverse chronological order.

## Sample HTML Code

This form creates a button that will remind someone to get the milk.

    <form action="http://web-to-text.appspot.com/send" method="POST">
    <input type="hidden" name="to" value="612-555-1212">
    <input type="hidden" name="body" value="Don't forget the milk">
    <input type="hidden" name="api-key" value="Your-API-Key">
    <input type="submit" value="Submit">
    </form>

The following URL retrieves all messages containing the word "milk".

    http://web-to-text.appspot.com/retrieve?body=milk&api-key=Your-API-Key
    

## Deployment

To deploy this application yourself, you will need:

* The Google App Engine SDK for Python
* A Twilio-enabled phone number
* Python libraries `twilio` and `phonenumbers`
* Probably some other stuff that I forgot to mention


Here are the steps:

* Rename the file `secrets_.py` to `secrets.py`
* Edit the file `secrets.py`, inserting your Twilio credentials
* Create a new project on Google App Engine
* Edit the file `app.yaml` to include the name of your project
* Install additional libraries
     $ mkdir lib
     $ pip install -t lib twilio
     $ pip install -t lib phonenumbers
* Deploy the application to Google Cloud

## Author

David Radcliffe (dradcliffe@gmail.com)
