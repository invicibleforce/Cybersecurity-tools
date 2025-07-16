from pwn import *
import sys

if len(sys.argv)!=2:
	print("Invalid argument!")
	print(">> {} <sha256sum>".format (sys.argv[0]))
	exit()

prefered_hash = sys.argv[1]

#you can change the file to the file you want to use or it's path
password_file = "/usr/share/wordlists/rockyou.txt"

attempts = 0

with log.progress("Attempting to crack: {}\n".format(prefered_hash)) as p:
	with open(password_file, "r" , encoding="latin-1") as password_list:
		for password in password_list:
			password = password.strip("\n").encode("latin-1")
			password_hash = sha256sum(password)
			p.status("[{}] {} == {}".format(attempts , password.decode("latin-1") , password_hash))
			if password_hash == prefered_hash:
				p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode("latin-1"),password_hash))
				exit()
			attempts += 1
		p.failure("Password not found!")	
