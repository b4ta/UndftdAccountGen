import requests, time, random, os, time
import threading
proxyList = [
'204.188.230.33:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.34:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.35:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.36:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.37:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.38:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.39:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.40:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.41:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.42:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.43:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.44:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.45:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.46:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.47:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.48:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.49:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.50:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.51:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.52:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.53:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.54:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.55:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.56:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.57:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.58:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.59:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.60:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.61:3128:flashproxieschi:maymonthly83ni43',
'204.188.230.62:3128:flashproxieschi:maymonthly83ni43']
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
		account_request = requests.post(url, json=data)
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