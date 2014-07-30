from flask import Flask, request, redirect

import twilio.twiml
from twilio.rest import TwilioRestClient

import json
import urllib2


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

	
	message = ""

	lon = request.form ["longitude"]
	lat = request.form["latitude"]

	location = ""

	print lon
	print lat

	str(lon)
	str(lat)

	if (lon != 0 and lat != 0):
		url = "http://pelias.test.mapzen.com/reverse?lat=" + lat + "&lng=" + lon
		jsonFile = urllib2.urlopen(url).read()

		data = json.loads(jsonFile)
		# data = json.load(jsonFile)

		if (len(data["features"]) != 0):
			print "Array empty."

			streetAddress = data["features"][0]["properties"]["name"]
			city = data["features"][0]["properties"]["locality_name"]
			state = data["features"][0]["properties"]["admin1_abbr"]
			country = data["features"][0]["properties"]["admin0_abbr"]

			location = streetAddress + ", " + city + ", " + state + ", " + country
		else:
			location = "("+ lat +", " + lon + ") -- [Unknown Address]"
	
	else:

		location = "unknown location (GPS unavailable)."

	message = "EMERGENCY ALERT: " + user + " was just in an emergency at " + location

	# message = "EMERGENCY ALERT: " + user + " was just in an emergency"


	

	if (phoneNumber):
		if (user):
			print message
			smsMessage = client.messages.create(to=phoneNumber, from_="+14806481956", body=message)


	return message


if __name__ == "__main__":
    app.run(debug=True)

