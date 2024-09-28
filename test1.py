import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class DynamicTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Table Example")
        self.setGeometry(100, 100, 600, 400)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create a table with 3 columns
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Button to add a new row
        self.add_row_button = QPushButton("Add Row", self)
        self.add_row_button.clicked.connect(self.add_row)

        # Button to remove the last row
        self.remove_row_button = QPushButton("Remove Last Row", self)
        self.remove_row_button.clicked.connect(self.remove_last_row)

        # Add table and buttons to the layout
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.add_row_button)
        self.layout.addWidget(self.remove_row_button)

    def add_row(self):
        # Get the current number of rows
        row_count = self.table.rowCount()

        # Insert a new row at the end
        self.table.insertRow(row_count)

        # Optionally, populate the row with default values
        self.table.setItem(row_count, 0, QTableWidgetItem(f"Item {row_count + 1}-1"))
        self.table.setItem(row_count, 1, QTableWidgetItem(f"Item {row_count + 1}-2"))
        self.table.setItem(row_count, 2, QTableWidgetItem(f"Item {row_count + 1}-3"))

    def remove_last_row(self):
        # Remove the last row
        row_count = self.table.rowCount()
        if row_count > 0:
            self.table.removeRow(row_count - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DynamicTable()
    window.show()
    sys.exit(app.exec_())
