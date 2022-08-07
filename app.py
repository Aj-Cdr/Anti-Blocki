import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('⏪', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        reload_btn = QAction('🔄', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        forward_btn = QAction('⏩', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        home_btn = QAction('🏠', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        dev_btn = QAction('ℹ', self)
        dev_btn.triggered.connect(self.dev_info)
        navbar.addAction(dev_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def dev_info(self):
        self.browser.setUrl(QUrl("https://spaboi.github.io/Ajay/"))


app = QApplication(sys.argv)
QApplication.setApplicationName('Anti Blocki :D')
window = MainWindow()
app.exec_()
