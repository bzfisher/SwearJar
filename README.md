SwearJar
========

McHacks W2014 project!
<<<<<<< HEAD



Front End
=========
Chrome Extension:
- [ ] Key Logging
- [ ] Sign in
- [ ] Swear word check
- [ ] Swear Word DB
- [ ] Stripe


Back End
=========
django:
- [x] USER MANAGMENT
- [x] List of dirty words used for each user

- [ ] twilo
- [ ] Daily notfication




- [ ] data viz ?????
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

