
# Sending and receiving messages using Twilio.

from flask import Flask, url_for, request, render_template
from jinja2 import Template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio import twiml
import urllib 
import random

#Twilio API call
accountSID = "Your_account_ID"
authenticationToken = "Your_token"

# Telephone number use for the From and To
fromNumber = 'from_number'
toNumber = 'to_number'
client = Client(accountSID, authenticationToken)

# Q Word + Verb + Subject + (object) + ?
# Yes and no questions, is, do, will
# Python list of question words; this can also be pick up from a database
qWords = ['hello', 'summer']

# Python list of verb
englishVerb = ['eat', 'buy']

# Python list of subject (for example pronoun). For now we are going to start with the pronouns
subject= ['I']

fileName = 'flaskTwilioResponse.txt'

app = Flask(__name__)

@app.route('/sms', methods=['POST', 'GET'])
def smsReply():   

    number = request.form['From']
    messageBodyReceived = request.form['Body']
    #toNumber = request.form['To']
    with open(fileName, "a") as receivedSMS:
            receivedSMS.write("\n" + messageBodyReceived)
    receivedSMS.close()

    goodSampleQuestions = (random.choice(qWords) + ' ' + random.choice(englishVerb) + ' ' + random.choice(subject) + '?')
    messageBodySend = goodSampleQuestions
    
    #TextMessage = client.messages.create( from_ = fromNumber, body = messageBodySend, to = toNumber)

    resp = MessagingResponse()
    resp.message(messageBodySend)
            
    #headLin = "TESTdd"
    #returnRender = render_template("login.html", headline=headLin)
      

    return str(resp)


if __name__ == "__main__":
    app.run()
#app.run(debug=True)
    
