import requests, time, random, threading
# - Detect captcha and use proxies to get around it
# - What if I use selenium
def start():
	s = requests.session()
	print("UNDFTD Account Gen Beta")
	username = input("Enter a username:")
	domain = input("Enter a catchall domain:")
	count = input("Enter the number of accounts:")
	password = input("Enter your password:")
	print("Ok time to make " + count + " accounts with your weird domain name")
	data = {"form_type": "create_customer",
		"customer[email]": "email",
		"customer[password]": "password"}
		# - There is a weird utf-8: checkmark thingy here but it makes the script wonky so I can't use it
	url = "https://undefeated.com/account/"
	for i in range(int(count)):
		user = username + "+" + str(random.randint(1,10000))
		email = user + "@" + domain
		create = s.post(url,json=data)
		if create.status_code == 302:
			print("Account: " + email + " made successfully.")
			accounts = email + ":" + password
			open("accounts.txt", "a").write("\n" + accounts)
		else:
			print("Probably needed Captcha so haha stupid")
start()
