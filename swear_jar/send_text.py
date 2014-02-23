import requests
from twilio.rest import TwilioRestClient 
from django.db import models
 
def send_text(count, number):

  if (count == 0):
    message = "Congrats, you have a clean mouth!"
  elif (count == 1):
     message = "You only swore once today. Good job! Pay your dues or else 	mommy will hear about what you said!"
  else:
     cnt = (int(count) / 10.0)
     message = "You swore " + count+" times today. Donate "+str(cnt)+	 	"dollar(s) to charity, or Mom will hear about what you said!"
  	# put your own credentials here 
  	f = open("Twilio",r).readLines()
	ACCOUNT_SID =  f[0]
  	AUTH_TOKEN = f[1] 
 
  	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
  	client.messages.create( to=number, from_="+14387937802", 		body=message  )
  
def send_all():
	for u in Models.User.people.all():
		send_text(u.swearCount,u.phoneNumber)

send_all()	







