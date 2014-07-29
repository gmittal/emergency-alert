from flask import Flask, request, redirect

import twilio.twiml
from twilio.rest import TwilioRestClient


account_sid = "ACba498d91d1312e0f4975eaac513d64be"
auth_token = "7c2bacbc7a9783c496e4af1af1a51a0b"
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def no_sms():

	phoneNumber = request.form["number"]
	user = request.form["userID"]
	# body = request.form["messageBody"]
	
	# print name.encode('utf-8')
	# print body.encode('utf-8')

	message = "EMERGENCY ALERT: " + user + " was just in an emergency"

	if (phoneNumber):
		if (user):
			smsMessage = client.messages.create(to=phoneNumber, from_="+14806481956", body=message)


	return "Success"


if __name__ == "__main__":
    app.run(debug=True)