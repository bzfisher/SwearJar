import requests
from twilio.rest import TwilioRestClient 
 


def send_text(count, user, number):

  if (count == 0):
    message = "Congrats, you have a clean mouth!"
  elif (count == 1):
     message = "You only swore once today. Good job! Respond \"Charity\" to donate ten cents to charity, or \"Mom\" to tell your mum what you said"
  else:
     cnt = (int(count) / 10.0)
     message = "You swore " + count+" times today. Respond \"Charity\" to donate "+str(cnt)+" dollar(s) to charity, or \"Mom\" to tell your mum what you said"
  # put your own credentials here 
  ACCOUNT_SID = "XXXXXXX" 
  AUTH_TOKEN = "XXXXXXX" 
 
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
  client.messages.create( to=number, from_="+14387937802", body=message  )
  
