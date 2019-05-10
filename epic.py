import requests, time, random, os, time
import threading
proxyList = ['insertProxiesHere']

# To-Do List
# - Get it to work lol
# - Use proxies
# - Rotate proxies when captcha is detected
# - Be able to detect captchas with https://undefeated.com/challenge
# - Make it create (for example) 2 separate accounts instead of making the same account twice when count = 2
# - Simplify code
# - Pull proxies from proxies.txt so my proxies aren't public
# - 
def start():
	s = requests.session()
	s.proxies = random.choice(proxyList)
	print("UNDFTD Account Gen Beta")
	username = input("Enter a username:")
	domain = input("Enter a catchall domain:")
	count = input("Enter the number of accounts:")
	password = input("Enter your password:")
	print("Now generating " + count + " accounts under the " + domain + " domain.")
	random_username = username + "+" + str(random.randint(1,1000))
	email = random_username + "@" + domain
	data = {
		"form_type": "create_customer",
		"customer[email]": "email",
		"customer[password]": "password"
		}
	url = "https://undefeated.com/account/"
	for i in range(int(count)):
		data["customer[email]"] = email
		account_request = s.post(url, json=data)
		if account_request.status_code == 302:
			print("Account: " + email + " made successfully.")
			account_string = email + ":" + password
			open("accounts.txt", "a").write("\n" + account_string)
		elif account_request.status_code == 429:
			print("Banned for the time being. Resting for three minutes")
			time.sleep(180)
		else:
			print("Failed to make account " + email)
			print("Exited with status code: ".format(account_request.status_code))
			time.sleep(3)
start()
