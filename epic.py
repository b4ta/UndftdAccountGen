import requests, time, random, os, time
import threading

# To-Do List
# - Get it to work lol
# - Use proxies
# - Rotate proxies when captcha is detected
# - Be able to detect captchas with https://undefeated.com/challenge
# - Simplify code
# - Maybe use selenium, would be slower but could fix captcha stuff
def start():
	s = requests.session()
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
		random_username = username + "+" + str(random.randint(1,1000))
		email = random_username + "@" + domain
		data["customer[email]"] = email
		account_request = s.post(url,json=data)
		if account_request.status_code == 302:
			print("Account: " + email + " made successfully.")
			account_string = email + ":" + password
			open("accounts.txt", "a").write("\n" + account_string)
		else:
			print("Failed to make account " + email)
			print("Exited with status code: ".format(account_request.status_code))
			time.sleep(3)
start()
