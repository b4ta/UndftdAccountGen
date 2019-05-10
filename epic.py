import requests, time, random, os, time
import threading
proxyList = ['insertProxiesHere']
request_headers = [
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
	Accept-Encoding: gzip, deflate, br
	Accept-Language: en-US,en;q=0.9
	Cache-Control: max-age=0
	Connection: keep-alive
	Content-Length: 161
	Content-Type: application/x-www-form-urlencoded
	Cookie: _shopify_y=f70cbb20-92de-4452-853f-75fb2e281a16; cart_currency=USD; _orig_referrer=; secure_customer_sig=; _shopify_country=United+States; _landing_page=%2F; cart_sig=; _y=f70cbb20-92de-4452-853f-75fb2e281a16; _s=a2a4e12a-0B80-4DD3-AB23-0D40E02EA319; _shopify_s=a2a4e12a-0B80-4DD3-AB23-0D40E02EA319; _shopify_fs=2019-05-10T16%3A46%3A49.006Z; shopify_pay_redirect=pending; _shopify_sa_p=; _ga=GA1.2.583425682.1557506810; _gid=GA1.2.734530934.1557506810; sig-shopify=true; rskxRunCookie=0; rCookie=3uamgrvt2i2x3wgyt1y3b; lastRskxRun=1557506824166; _shopify_sa_t=2019-05-10T16%3A47%3A04.316Z; eu-opt-in=1
	Host: undefeated.com
	Origin: https://undefeated.com
	Referer: https://undefeated.com/account/login
	Upgrade-Insecure-Requests: 1
	User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
		]
response_headers = [
	Connection: keep-alive
	Content-Language: en
	Content-Security-Policy: block-all-mixed-content; frame-ancestors *; upgrade-insecure-requests; report-uri /csp-report?source%5Baction%5D=create&source%5Bapp%5D=Shopify&source%5Bcontroller%5D=storefront_section%2Fcustomers%2Faccounts&source%5Bsection%5D=storefront&source%5Buuid%5D=480a26b1-0a4c-4360-b7b3-62b771357edc
	Content-Type: text/html; charset=utf-8
	Date: Fri, 10 May 2019 16:49:39 GMT
	Location: https://undefeated.com/account/register
	NEL: {"report_to":"network-errors","max_age":2592000,"failure_fraction":0.01,"success_fraction":0.0001}
	Report-To: {"group":"network-errors","max_age":2592000,"endpoints":[{"url":"https://monorail-edge.shopifycloud.com/v1/reports/nel/20190325/shopify"}]}
	Server: nginx
	Set-Cookie: secure_customer_sig=; path=/; expires=Tue, 10 May 2039 16:49:38 -0000; secure; HttpOnly
	Set-Cookie: _secure_session_id=4a411ded69c694da817dc2568747b610; path=/; expires=Sat, 11 May 2019 16:49:38 -0000; secure; HttpOnly
	Set-Cookie: cart_sig=; path=/; expires=Fri, 24 May 2019 16:49:38 -0000; HttpOnly
	Strict-Transport-Security: max-age=7889238
	Transfer-Encoding: chunked
	X-Content-Type-Options: nosniff
	X-Dc: chi2,gcp-us-east1
	X-Download-Options: noopen
	X-Permitted-Cross-Domain-Policies: none
	X-Request-Id: 480a26b1-0a4c-4360-b7b3-62b771357edc
	X-ShardId: 72
	X-ShopId: 2825850
	X-Shopify-Stage: canary
	X-Sorting-Hat-PodId: 72
	X-Sorting-Hat-ShopId: 2825850
	X-XSS-Protection: 1; mode=block; report=/xss-report?source%5Baction%5D=create&source%5Bapp%5D=Shopify&source%5Bcontroller%5D=storefront_section%2Fcustomers%2Faccounts&source%5Bsection%5D=storefront&source%5Buuid%5D=480a26b1-0a4c-4360-b7b3-62b771357edc
	]

# To-Do List
# - Get it to work lol
# - Use proxies
# - Rotate proxies when captcha is detected
# - Be able to detect captchas with https://undefeated.com/challenge
# - Make it create (for example) 2 separate accounts instead of making the same account twice when count = 2
# - Simplify code
# - Pull proxies from proxies.txt so my proxies aren't public
# - Add a config.json
# - Maybe use selenium, would be slower but could fix captcha stuff
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
		account_request = s.post(url,json=data,headers=response_headers&request_headers)
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
