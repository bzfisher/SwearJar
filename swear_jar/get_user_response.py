import requests
from twilio.rest import TwilioRestClient 
from django.db import models
 
def send_text(u):
	if not u.swearCount==0:
		message = "Look ma!! Your darling child swore "+u.swearCount+" today! Want a list? Here ya go "+u.swears
		f = open("Twilio",r).readLines()
		ACCOUNT_SID =  f[0]
  		AUTH_TOKEN = f[1] 
 
  		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
  		client.messages.create( to=u.momsNumber, from_="+14387937802", 		body=message  )

def send_all():
	for u in Models.User.people.all():
		send_text(u)
		u.swearCount=0
send_all()
