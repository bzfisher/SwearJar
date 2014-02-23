from django.http import HttpResponse
from swear_jar_core.models import User
import datetime


def newUser(request)
	return HttpResponse("Hello, world. You're at the poll index.")
	if request.Method == 'POST':
		userRequest = request.POST
		user = User()
		user.userName = userRequest["username"]
		user.password = userRequest["password"]
		user.phoneNumber = userRequest["phonenumber"]
		user.momsNumber = userRequest["momsnumber"]
		user.swears=""
		user.save()


def userSwore(request):
	if request.Method == 'POST':
		userRequest = request.POST
		user = User.objects.get(userName=userRequest["username"])
		swearList = users.swears
		badWord = ","+userRequest[swearword]
		user.swears=swearList + badWord
		user.swearCount++
		return HttpResponse(True)
	else:
		return HttpResponse(False)
		

def userPaid(request):
	if request.Method == 'POST':
		userRequest=request.POST
		user = User.objects.get(userName=userRequest["username"])
		user.lastChecked = datetime.datetime.now()
		user.swearCount = 0
		user.swears=""
		return HttpResponse(True)
	else:
		return HttpResponse(False)

def signIn(request):
	if request.Method == 'POST':
		userRequest=request.POST
		try:
			user=User.objects.get(userName=userRequest["username"],password=userRequest[password])
			return HttpResponse(True)
		catch Exception:
			return HttpResponse(False)
	else: 
		return HttpResponse(False)
def amountDue(request):
	if requests.Method == "Get":
		user=User.objects.get(userName=request.POST["username"]
		return HttpResponse((user.swearCount)/10.0)
	else:
		return HttpResponse(0)




