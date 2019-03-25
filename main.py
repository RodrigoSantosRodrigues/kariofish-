import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 1300, 650)
		self.setWindowTitle("KarioFish")
		self.setWindowIcon(QtGui.QIcon('icone.png'))
		
		extractAction = QtWidgets.QAction("New Image", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Open new image for processing')
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&Image')
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		btn = QtWidgets.QPushButton("Play", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)
		self.show()

	def close_application(self):
		print("Hello mundo...")
		sys.exit()


app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())