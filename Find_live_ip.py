import os
#---------------------------------------------
#made By Saurabh Londhe
#--------------------------------------------
def check():
	if os.system("arp-scan -l")==32512:
		os.system("clear")
		print "'arp'\t not installed\n\n\n try\n\t'sudo apt-get install arp-scan'\n\t\t\tor\n\t'dnf install arp-scan '"
	else:
		fun()
def fun():
	up_array=[]
	down_array=[]
	c=0
	os.system("arp-scan -l > ip.txt")
	cnt=0
	f=open("ip.txt","r")
	up=open("up.ip","w")
	down=open("down.ip","w")
	s=f.readlines()
	for linr in s:
		cnt+=1
	for line in s:
		if line.startswith("172.22."):
			c+=1
			print str(c)+"/"+str(cnt)
			response = os.system("ping -c 1 " +line.split()[0])
			os.system("clear")
			if response == 0:
				#print line.split()[0], 'is up!'
				up_array.append(line.split()[0])
				up.write(line.split()[0]+"\n")
			else:
				#print line.split()[0], 'is down!'
				down_array.append(line.split()[0])
				down.write(line.split()[0]+"\n")

check()
