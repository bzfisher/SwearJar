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




