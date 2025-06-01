import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QToolBar, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QDialog, QLabel
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

print("This is the PyBrowser console.\nDo not close this window while the browser is running.\n\n\n\n")

class SearchDialog(QDialog):
    def __init__(self, browser):
        super().__init__()
        self.browser = browser
        self.setWindowTitle("Lookup")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("Search for text:")
        self.input = QLineEdit()
        self.input.returnPressed.connect(self.find_text)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        self.setLayout(layout)

    def find_text(self):
        text = self.input.text()
        self.browser.findText(text)

class PyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBrowser 1.0 - Release")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        home_path = os.path.abspath("homepage.html")
        self.browser.setUrl(QUrl.fromLocalFile(home_path))

        # Toolbar
        nav_bar = QToolBar()
        nav_bar.setMovable(False)
        nav_bar.setStyleSheet("""
            QToolBar {
                background: #2e2e2e;
                spacing: 10px;
                padding: 8px;
            }
            QLineEdit {
                background: #202124;
                color: white;
                padding: 8px 12px;
                border-radius: 20px;
                border: 1px solid #444;
                font-size: 15px;
                selection-background-color: #3a3a3a;
            }
            QPushButton {
                background: #444;
                color: white;
                padding: 6px 12px;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background: #666;
            }
            QPushButton:pressed {
                background: #888;
            }
        """)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        btn_reload = QPushButton("Refresh")
        btn_reload.clicked.connect(self.browser.reload)

        btn_go = QPushButton("Search")
        btn_go.clicked.connect(self.navigate_to_url)

        btn_search = QPushButton("Lookup")
        btn_search.clicked.connect(self.open_search_dialog)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.url_bar)
        nav_layout.addWidget(btn_go)
        nav_layout.addWidget(btn_reload)
        nav_layout.addWidget(btn_search)

        nav_container = QWidget()
        nav_container.setLayout(nav_layout)
        nav_bar.addWidget(nav_container)

        self.addToolBar(nav_bar)
        self.setCentralWidget(self.browser)
        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def open_search_dialog(self):
        dialog = SearchDialog(self.browser)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyBrowser()
    window.show()
    sys.exit(app.exec_())
