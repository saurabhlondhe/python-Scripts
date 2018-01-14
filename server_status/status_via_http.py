import os,time,thread
def status():
    a=0
    try:
        while a!=100:
            os.system("date > data.txt")
            os.system("mpstat -P ALL >> data.txt")
            os.system("free -m >> data.txt")
            time.sleep(2)
            a+=1
    except KeyboardInterrupt:
        sys.exit()
thread.start_new_thread(status  ,())
try:
    os.system("python -m SimpleHTTPServer 12345")
except KeyboardInterrupt:
    sys.exit()
