from django.http import HttpResponse
from swear_jar_core.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def newUser(request):
	if request.method == 'POST':
		userRequest = request.POST
		user = User()
		user.userName = userRequest["username"]
		user.password = userRequest["password"]
		user.phoneNumber = userRequest["phonenumber"]
		user.momsNumber = userRequest["momsnumber"]
		user.swears=""
		user.save()
		return HttpResponse(True)
	return HttpResponse(False)

@csrf_exempt
def userSwore(request):
	if request.method == 'POST':
		userRequest = request.POST
		user = User.objects.get(userName=userRequest["username"])
		swearList = user.swears
		badWord = userRequest["swearword"]+","
		user.swears=swearList + badWord
		user.swearCount = user.swearCount+1
		user.save()
		return HttpResponse(True)
	else:
		return HttpResponse(False)
		
@csrf_exempt
def userPaid(request):
	if request.method == 'POST':
		userRequest=request.POST
		user = User.objects.get(userName=userRequest["username"])
		user.lastChecked = datetime.datetime.now()
		user.swearCount = 0
		user.swears=""
		user.save()
		return HttpResponse(True)
	else:
		return HttpResponse(False)

@csrf_exempt
def signIn(request):
	if request.method == 'POST':
		userRequest=request.POST
		try:
			user=User.objects.get(userName=userRequest["username"])
			return HttpResponse(user.password == userRequest["password"]) 
		except Exception:
			return HttpResponse(False)
	else:
		return HttpResponse(False)

@csrf_exempt
def amountDue(request):
	if request.method == 'GET':
		user=User.objects.get(userName=request.GET["username"])
		return HttpResponse((user.swearCount)/10.0)
	else:
		return HttpResponse(0)

from twilio.rest import TwilioRestClient 
from django.db import models
 
@csrf_exempt
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
 
     client.messages.create( to=number, from_="+14387937802",body=message  )

@csrf_exempt  
def send_all(request):
	for u in User.people.all():
		send_text(u.swearCount,u.phoneNumber)
	return HttpResponse(0)
@csrf_exempt
def send_text_mom(u,request):
	if not u.swearCount==0:
		message = "Look ma!! Your darling child swore "+u.swearCount+" today! Want a list? Here ya go "+u.swears
		f = open("Twilio",r).readLines()
		ACCOUNT_SID =  f[0]
  		AUTH_TOKEN = f[1] 
 
  		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
  		client.messages.create( to=u.momsNumber, from_="+14387937802",body=message  )

@csrf_exempt
def send_all_mom():
	for u in User.people.all():
		send_text_mom(u)
		u.swearCount=0
	return HttpResponse(0)


