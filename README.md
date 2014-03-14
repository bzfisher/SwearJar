SwearJar
========

McHacks W2014 project!
<<<<<<< HEAD



Front End
=========
Chrome Extension:
- [X] Sign in
- [X] Sign up
- [X] Swear word check
- [X] Swear Word DB
- [ ] Keep track of logged in user
- [ ] Integration with back end
- [ ] implement two dictionaries - one for regrex matching, and one for all other words.


Back End
=========
django:
- [x] USER MANAGMENT
- [x] List of dirty words used for each user
- [X] Stripe
- [ ] twilio
- [ ] Weekly notfication
//- [ ] data viz ?????

Front-Back End Integration
=========


=======
Monitor your cussing
Donate money or tell ma!


backend API instructions
=======

1. Add a new user:
	* method: POST
	* url: http://107.170.73.156:8001/newuser/
	* required fields: username, password, phonenumber, momsnumber
	* returns: True if successfully created user, False otherwise.

2. A User has Sworn (Oh no!):
	* method: POST
	* url: http://107.170.73.156:8001/userswore/
	* required fields: username, swearword
	* returns: True if succesfully registered the swearword, False otherwise.

3. User paid:
	* method: POST
	* url: http://107.170.73.156:8001/userpaid/
	* required fields: username
	* returns: True if successfully registered the payment, False otherwise.

4. Sign in:
	* method: POST
	* url: http://107.170.73.156:8001/signin/
	* required fields: username, password
	* returns: True if sign-in successful, False otherwise.

5. Get amount due:
	* method: GET
	* url: http://107.170.73.156:8001/amountdue/
	* required fields: username
	* returns: amount due (in dollars)


March 14th update
=======
The following workflow now works: log in -> swear in the test.html webpage you are presented with -> swearword is logged to server. We have turned on debug/logging in settings.py, and fixed only the userSwore method in views (to grab the username form the session cookie).
We still need to fix the other methods in views.

