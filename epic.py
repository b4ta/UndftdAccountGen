import requests, time, random, threading
# To-Do List
# - Detect captcha and use proxies to get around it
# - What if I use selenium
def start():
	s = requests.session()
	print("UNDFTD Account Gen Beta")
	username = input("Enter a username:")
	domain = input("Enter a catchall domain:")
	count = input("Enter the number of accounts:")
	password = input("Enter your password:")
	print("Ok time to make " + count + " accounts with your weird domain name.")
	data = {"form_type": "create_customer",
		"customer[email]": "email",
		"customer[password]": "password"
		# - There is a weird utf-8: checkmark thingy here but it makes the script wonky so I can't use it}
	url = "https://undefeated.com/account/"
	for i in range(int(count)):
		random_username = username + "+" + str(random.randint(1,10000))
		email = random_username + "@" + domain
		data["customer[email]"] = email
		data["customer[password]"] = password
		account_request = s.post(url,json=data)
		if account_request.status = 302:
			print("Account: " + email + " made successfully.")
			account_string = email + ":" + password
			open("accounts.txt", "a").write("\n" + account_string)
		else:
			print("Probably needed Captcha so haha stupid")
start()
