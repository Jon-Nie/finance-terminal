from PySide2.QtWidgets import QFrame, QTabWidget
from pages.stocks.overview import StockOverview

class Content(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(
            """
            QTabWidget::pane {
                background-color: lightgrey;
                border: 0px;
            }
            """
        )

        self.overview = StockOverview()

        self.addTab(QFrame(), "Tab1")
        self.addTab(self.overview, "Tab2")
        self.addTab(QFrame(), "Tab3")