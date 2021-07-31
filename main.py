import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self): #Self Define function

        # HomePage
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.initUI()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation
        navbar = QToolBar()
        navbar.setIconSize(QSize(20, 20))
        self.addToolBar(navbar)
        navbar.show()

        back_btn = QAction(QIcon('back.png'), "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('forward.png'), "Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('reload.png'), "Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('home.png'), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        bing_btn = QAction(QIcon('bing.png'), 'Bing', self)
        bing_btn.triggered.connect(self.nav_bing)
        navbar.addAction(bing_btn)

        yahoo_btn = QAction(QIcon('yahoo.png'), 'Yahoo', self)
        yahoo_btn.triggered.connect(self.nav_yahoo)
        navbar.addAction(yahoo_btn)

        ddg_btn = QAction(QIcon('ddg.png'), 'DuckDuckGo', self)
        ddg_btn.triggered.connect(self.nav_ddg)
        navbar.addAction(ddg_btn)


        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def nav_bing(self):
        self.browser.setUrl(QUrl('http://bing.com'))

    def nav_yahoo(self):
        self.browser.setUrl(QUrl('http://yahoo.com'))

    def nav_ddg(self):
        self.browser.setUrl(QUrl('http://duckduckgo.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Arc Broswer')
        self.setWindowIcon(QIcon('browser.png'))

        self.show()



app = QApplication(sys.argv)
trayIcon = QSystemTrayIcon(QIcon('browser.png'), parent=app)
trayIcon.show()
window = MainWindow()
app.exec_()