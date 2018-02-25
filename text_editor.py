import sys,os,time
from PyQt4 import QtGui as qt
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class about(qt.QWidget):
    	def work(self):
		qt.QWidget.__init__(self,parent=None)
		about_data="<center>Copyright "+u"\N{COPYRIGHT SIGN}"+" 2018 Saurabh Londhe</center><br><center>Version 1.0"
		label1=qt.QLabel(about_data,self)
		label1.move(40,100)
		x=300
		y=250
		screen = qt.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		ht=(screen.height()-y)/2
		wd=(screen.width()-x)/2
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
	def __init__(self,parent=None):
		self.work()
class sau_edit(qt.QMainWindow):
    def __init__(self):
        super(sau_edit, self).__init__()
        screen = qt.QDesktopWidget().screenGeometry()
        self.ht=600#(screen.height())
        self.wd=1000#(screen.width())
        self.setGeometry((screen.width()-self.wd)/2,0,self.wd,self.ht-50)
        self.setFixedSize(self.wd,self.ht-50)
        #self.showFullScreen()
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("C -editor")
        self.setWindowIcon(qt.QIcon("notepad.png"))

        #---------------------------------status label-------------------------------------
        self.status=qt.QLabel(self)
        self.status.move(750,500)#self.wd-200,self.ht-200)
        self.status.setStyleSheet("QTextEdit {color:red;background-color:white}")
        #---------------------------------all menu bar entry--------------------------------
        new_file_key = qt.QAction("&New file", self)
        new_file_key.setShortcut("Ctrl+n")
        new_file_key.setStatusTip('New file')
        new_file_key.triggered.connect(self.new_file)

        new_window_file_key = qt.QAction("&New window", self)
        new_window_file_key.setShortcut("Ctrl+Shift+n")
        new_window_file_key.setStatusTip('New window')
        new_window_file_key.triggered.connect(self.new_window_file)

        open_file_key = qt.QAction("&Open file", self)
        open_file_key.setShortcut("Ctrl+o")
        open_file_key.setStatusTip('Open file')
        open_file_key.triggered.connect(self.open_file)

        save_key = qt.QAction("&Save", self)
        save_key.setShortcut("Ctrl+s")
        save_key.setStatusTip('Save file')
        save_key.triggered.connect(self.save_file)

        quit_key = qt.QAction("&Quit application !", self)
        quit_key.setShortcut("Ctrl+Q")
        quit_key.setStatusTip('Leave The App')
        quit_key.triggered.connect(self.close_application)

        copy_key = qt.QAction("&Copy", self)
        copy_key.setShortcut("Ctrl+c")
        copy_key.setStatusTip('copy')
        copy_key.triggered.connect(self.save_file)

        cut_key = qt.QAction("&Cut", self)
        cut_key.setShortcut("Ctrl+x")
        cut_key.setStatusTip('cut')
        cut_key.triggered.connect(self.save_file)

        paste_key = qt.QAction("&Paste", self)
        paste_key.setShortcut("Ctrl+v")
        paste_key.setStatusTip('paste')
        paste_key.triggered.connect(self.save_file)

        about_key = qt.QAction("&About", self)
        about_key.setStatusTip('About editor')
        about_key.triggered.connect(self.about_info)

        terminal_key = qt.QAction("&Terminal", self)
        terminal_key.setStatusTip('Open terminal')
        terminal_key.triggered.connect(self.show_terminal)

        self.statusBar()
        #-------------------------------------all menu-s-------------------------------------
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(new_file_key)
        fileMenu.addAction(new_window_file_key)
        fileMenu.addAction(open_file_key)
        fileMenu.addAction(save_key)
        fileMenu.addAction(quit_key)

        edit_menu=mainMenu.addMenu('&Edit')
        edit_menu.addAction(copy_key)
        edit_menu.addAction(cut_key)
        edit_menu.addAction(paste_key)

        help_menu=mainMenu.addMenu('&Tool')
        help_menu.addAction(terminal_key)

        help_menu=mainMenu.addMenu('&Help')
        help_menu.addAction(about_key)
        #-------------------------------------textEdit-----------------------------------------
        self.text_edit_field=qt.QPlainTextEdit(self)
        self.text_edit_field.setFixedSize(self.wd-300,self.ht-80)
        self.text_edit_field.move(0,30)
        self.font = qt.QFont()
        self.font.setFamily('Courier')
        self.font.setPointSize(10)
        self.text_edit_field.setFont(self.font)
        #self.text_edit_field.setFontItalic(True)
        self.text_edit_field.setStyleSheet("QPlainTextEdit {color:green;background-color:white}")
        #highlight = syntax.PythonHighlighter(self.text_edit_field.document())
        self.text_edit_field.show()
        self.terminal()
        self.file_datail()
        self.show()
    #-------------------------------------functions-----------------------------------

    def file_datail(self):
        self.file_name_title=qt.QLabel("name:\t",self)
        self.file_name_title.move(710,350)
        self.file_name_title.setFixedSize(250,30)

        self.file_size=qt.QLabel("size:\t",self)
        self.file_size.move(710,370)
        self.file_size.setFixedSize(250,30)
    def new_window_file(self):
        os.system("python text_editor.py")

    def show_terminal(self):
        path=os.getcwd()
        os.system("xterm")

    def terminal(self):
        self.process  = QProcess(self)
        self.terminal = QWidget(self)
        #layout = QVBoxLayout(self)
        #layout.addWidget(self.terminal)
        self.process.start(
            'xterm',
            ['-into', str(self.terminal.winId())]
        )
        self.terminal.move(700,30)
        self.terminal.setFixedSize(300,600)

    def syn(self):
        data=open(self.file_name,"r").read()
        data=data.replace("int","<font color='red'>int</font>")
        return data

    def resizeEvent(self, event):
        print("resize")

    def about_info(self):
        self.o=about()
        self.o.show()

    def close_application(self):
        choice = qt.QMessageBox.question(self,"Confirm Exit...",
                      "Are you sure you want to exit ?",
                      qt.QMessageBox.Yes| qt.QMessageBox.No)
        if choice == qt.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def new_file(self):
        print "new file"
        self.save_file()
        self.file_name=None
        self.text_edit_field.setPlainText("")

    def open_file(self):
        self.fileDialog = qt.QFileDialog(self)
        self.file_name=self.fileDialog.getOpenFileName()
        self.setWindowTitle("sau-edit: "+self.file_name)
        with open(self.file_name) as f:
            self.text_edit_field.setPlainText(f.read())
            #self.text_edit_field.appendHtml(f.read())
        #self.text_edit_field.appendHtml(self.syn())
        self.file_name_title.setText("<font color='red'>name:</font>"+self.file_name.split("/")[-1])
        self.file_size.setText("<font color='red'>size:</font>"+str(os.path.getsize(self.file_name))+" bytes")

    def save_file(self):
        print "saved"
        try:
            with open(self.file_name,"w") as f:
                f.write(self.text_edit_field.toPlainText())
            print "successful"
        except:
            try:
                name = qt.QFileDialog.getSaveFileName(self, 'Save File')
                file = open(name,'w')
                text = self.text_edit_field.toPlainText()
                file.write(text)
                file.close()
                self.file_name=name
            except:
                pass
        self.status.setText("saved")

    def closeEvent(self,event):
        result = qt.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      qt.QMessageBox.Yes| qt.QMessageBox.No)
        event.ignore()

        if result == qt.QMessageBox.Yes:
         event.accept()
def run():
    app = qt.QApplication(sys.argv)
    GUI = sau_edit()
    sys.exit(app.exec_())
run()
