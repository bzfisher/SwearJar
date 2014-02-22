from django.http import HttpResponse
from swear_jar_core.models import User


def newUser(request)
	return HttpResponse("Hello, world. You're at the poll index.")
	if request.Method = 'POST':
		userRequest = request.POST
		user = User()
		user.userName = userRequest["username"]
		user.password = userRequest["password"]
		user.phoneNumber = userRequest["phonenumber"]
		user.momsNumber = userRequest["momsnumber"]
		user.save()


def userSwore(request)
	if request.Method = 'POST':


def userPaid(request)
	if request.Method = 'POST':


def signIn(request)
	if request.Method = 'POST':