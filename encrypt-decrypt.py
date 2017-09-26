import os
def encrypt():
	text=raw_input("Enter text: ")
	os.system("touch passwd.txt")
	data=open("passwd.txt","w")
	s=""
	key=int(input("enter key int NUMBERS to encrypt: "))
	for i in text:
		s=s+str(ord(i)*(key**97))+"\n"
	data.write(s)
	data.close()
def decrypt():
	file_open=open("passwd.txt","r")
	pas=""
	key=int(input("enter key to decrypt: "))
	try:
		for line in file_open:
			pas=pas+chr(int(line)/(key**97))
	except Exception:
		print "entre correct key"
		decrypt()
		
	print pas
	file_open.close()

def main():
	print "1)Write msg\n2)Read msg"
	ch=int(input())
	if ch==1:
		encrypt()
	else:
		decrypt()
main()
