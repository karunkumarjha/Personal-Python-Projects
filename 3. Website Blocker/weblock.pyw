import time
from datetime import datetime as dt

hostPath = r"C:\Windows\System32\drivers\etc\hosts"
hostTemp = r"D:\Python Programs\3. Website Blocker\hosts"
redirect = "127.0.0.1"
websites = ['www.facebook.com','facebook.com']

while  True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
		print("working hours")
		with open(hostTemp,"r+") as file:
			content = file.read()
			i=0
			for website in websites:
				if website in content:
					pass
				else:
					if i==1:
						print("\n")
					file.write(redirect +" "+website+"\n")
	else:
		print("fun hours")
		with open(hostTemp,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any (website in line for website in websites):
					file.write(line)
			i=1
			file.truncate()
	time.sleep(5)