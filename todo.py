import sys,os,time
s=sys.argv
def deleteLine():
    fn = '.todo.txt'
    f = open(fn)
    output = []
    id_of_task=input("Enter task id to delete= ")
    for line in f:
        if not id_of_task in line:
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()
def counter():
	f=open(".counter.data","r")
	s=f.read()
	f.close()
	f1=open(".counter.data","w")
	f1.write(str(int(s)+1))
	return str(int(s)+1)
def add_todo():
	f=open('.todo.txt','a')
	time1=counter()+"\t"+str(time.strftime("%I:%M:%S"))+"\t"+str(time.strftime("%d/%m/%Y"))+"\t"
	data=str(' '.join(sys.argv[2:]))
	f.write(time1+data)
	f.write('\n')
	print("Your response is stored")
def show_todo():
	f=open('.todo.txt','r')
	print(f.read())
def set_alias():
	cmd="cd && "+"echo 'alias todo=python3 /etc/todo/todo.py' >> .bashrc"
def reset():
	if os.path.isdir("/etc/todo")==True:
		os.system("rm -rf /etc/todo/* && cat todo.py > /etc/todo/todo.py")
	else:
		os.system("mkdir /etc/todo && cat todo.py > /etc/todo/")
	os.system(cmd)
	f=open('.todo.txt','w')
	f.write("***************************************************\n")
	f.write("todo ID\t Time\t\tDate\t\t Task\n")
	f.write("---------------------------------------------------\n")
	f1=open(".counter.data","w")
	f1.write("0")
if (os.path.isfile(".todo.txt"))!=True:
	reset()
try:
	if s[1]=='-a':
		add_todo()
	elif s[1]=='-d':
		deleteLine()
	elif s[1]=='-v':
		show_todo()
	elif s[1]=='-r':
		reset()
	elif s[1]=='-s':
		set_alias()
except:
    print('use an arguments \n\t-a | add task + (task name )\n\t-d | delete tasks\n\t-v | view tasks\n\t-r | reset todo application\n\t-s | set alias if todo command not found')
