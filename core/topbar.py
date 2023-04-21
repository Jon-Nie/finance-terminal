from PySide2.QtCore import (
    QStringListModel,
    Qt
)
from PySide2.QtWidgets import (
    QCompleter,
    QFrame,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)
from finance_database import Database

class TopBar(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedHeight(40)
        self.setStyleSheet(
            """
            QFrame {
                background-color: darkgrey;
            }
            """
        )

        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.btn_menu = QPushButton("Menu")
        self.btn_menu.setFixedSize(50, 40)
        self.picker = StockPicker()
        self.layout.setAlignment(Qt.AlignLeft)
        self.picker.setMaximumWidth(500)
        self.layout.addWidget(self.btn_menu)
        self.layout.addWidget(self.picker)

class StockPicker(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with Database() as db:
            tickers = db.companies()
            self.data = [item["ticker"] for item in tickers]
        self.model = QStringListModel(self.data)
        self.completer = QCompleter()
        self.completer.setModel(self.model)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity(0))
        self.completer.setCompletionColumn(0)
        self.completer.setMaxVisibleItems(10)
        self.setCompleter(self.completer)