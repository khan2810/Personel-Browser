from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation menu
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction('Go to Home', self)
        home_button.triggered.connect(self.go_to_home)
        navbar.addAction(home_button)

        self.search_area = QLineEdit()
        self.search_area.returnPressed.connect(self.go_to_url)
        navbar.addWidget(self.search_area)

        self.browser.urlChanged.connect(self.update_url)

    def go_to_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    
    def go_to_url(self):
        url = self.search_area.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, par1):
        self.search_area.setText(par1.toString())

MyBrowser = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
window = MainWindow()
MyBrowser.exec_()