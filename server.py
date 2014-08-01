from flask import Flask, request, redirect

import twilio.twiml
from twilio.rest import TwilioRestClient

import json
import urllib2

import ast


account_sid = "ACba498d91d1312e0f4975eaac513d64be"
auth_token = "7c2bacbc7a9783c496e4af1af1a51a0b"
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def no_sms():

	# phoneNumber = request.form["number"]

	phoneNumbers = request.form["number"]
	phoneNumbers = ast.literal_eval(phoneNumbers)

	print phoneNumbers

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
		url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + lon + "&sensor=false"

		# url = "http://pelias.test.mapzen.com/reverse?lat=" + lat + "&lng=" + lon
		jsonFile = urllib2.urlopen(url).read()

		data = json.loads(jsonFile)
		# data = json.load(jsonFile)

		if (len(data["results"]) != 0):
			# print "Array empty."

			# streetNumber = data["results"][0]["address_components"][0]["long_name"]
			# street = data["results"][0]["address_components"][1]["short_name"]
			# city = data["results"][0]["address_components"][3]["long_name"]
			# state = data["results"][0]["address_components"][5]["short_name"]
			# country = data["results"][0]["address_components"][6]["short_name"]
			# zipCode = data["results"][0]["address_components"][7]["short_name"]

			# location = streetNumber + " " + street + ", " + city + ", " + state + ", " + country

			location = data["results"][0]["formatted_address"]
		else:
			location = "("+ lat +", " + lon + ") -- [Unknown Address]"
	
	else:

		location = "unknown location (GPS unavailable)."

	message = "EMERGENCY ALERT: " + user + " was just in an emergency at " + location

	# message = "EMERGENCY ALERT: " + user + " was just in an emergency"


	

	if (phoneNumbers):
		if (user):
			print message
			for number in range(0, len(phoneNumbers)):
				print phoneNumbers[number]
				# smsMessage = client.messages.create(to=phoneNumbers[number], from_="+16506660889", body=message)


	return message


if __name__ == "__main__":
    app.run(debug=True)

