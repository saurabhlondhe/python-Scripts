from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import thread,time,os,sys
ip=""
port=888
#s=sys.argv()
def title():
	i=0
	s="server is ready script written by Saurabh londhe"
	while True:
		if i==len(s):
			i=0
		print s[0:i]+s[i].upper()+s[i+1:]+" FTP ip ' "+str(ip)+":"+str(port)+"'"
		i+=1
		time.sleep(0.05)
		os.system("clear")
#-------------------------FTP--------------------------------------------
def start_ftp():
	authorizer = DummyAuthorizer()
	try:
		s=sys.argv
		if s[1]:
			authorizer.add_user("toretto", "toor",s[1], perm="elradfmw")
			authorizer.add_anonymous(s[1], perm="elradfmw")
	except:
		s=sys.argv
		authorizer.add_anonymous("/home", perm="elradfmw")
		authorizer.add_user("toretto", "toor", "/root/", perm="elradfmw")
		authorizer.add_user("user", "pass", "/home", perm="elradfmw")
	handler = FTPHandler
	handler.authorizer = authorizer
	global ip,port
	ip=get_ip()
	server = FTPServer((ip,port), handler)
	server.serve_forever()
	return ip,port

#-------------------------GET-IP-------------------------------------------
def get_ip():
	os.system("ifconfig > data.txt")
	f=open("data.txt")
	for i in f:
		if "inet " in i:
			#print i
			s=i
	global ip
	os.system("rm -rf data.txt")
	ip=s[13:27]
	return ip
#---------------------------------------------------------------------
thread.start_new_thread(title,())
get_ip()
start_ftp()
#title()
