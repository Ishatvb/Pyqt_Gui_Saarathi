import sys
import json
from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton, 
    QTableWidget, QTableWidgetItem, QWidget, QTextEdit, 
    QComboBox, QFileDialog, QCheckBox
)
from sidebar import Ui_MainWindow
from DataManager import DataManager  

class MedTable(QMainWindow):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        
        self.setWindowTitle("Prescribed Medicine Details")
        self.setGeometry(100, 100, 1000, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["S.No.", "Medicine Name", "Amount", "Dosage", "Before/After Meal", "Duration (in days)"])

        self.layout.addWidget(self.table)

        self.add_row_button = QPushButton("Add Row", self)
        self.add_row_button.clicked.connect(self.add_row)

        self.remove_row_button = QPushButton("Remove Last Row", self)
        self.remove_row_button.clicked.connect(self.remove_last_row)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.saveMed)

        self.layout.addWidget(self.add_row_button)
        self.layout.addWidget(self.remove_row_button)
        self.layout.addWidget(self.save_button)

        self.load_data()  # Load existing data when initialized

    def load_data(self):
        medicines = self.data_manager.get_medicines()
        for med in medicines:
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            self.table.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))
            self.table.setCellWidget(row_count, 1, QTextEdit(med["Medicine Name"]))
            self.table.setCellWidget(row_count, 2, QTextEdit(med["Amount"]))
            dosage_combo = QComboBox()
            dosage_combo.addItems(["1 - 0 - 0", "0 - 1 - 0", "0 - 0 - 1", "1 - 1 - 0", "0 - 1 - 1", "1 - 0 - 1", "1 - 1 - 1"])
            dosage_combo.setCurrentText(med["Dosage"])
            self.table.setCellWidget(row_count, 3, dosage_combo)
            before_after_combo = QComboBox()
            before_after_combo.addItems(["Before", "After"])
            before_after_combo.setCurrentText(med["Before/After Meal"])
            self.table.setCellWidget(row_count, 4, before_after_combo)
            self.table.setCellWidget(row_count, 5, QTextEdit(med["Duration (in days)"]))

    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))

        # Medicine Name as QTextEdit
        medicine_name = QTextEdit()
        medicine_name.setMinimumHeight(30)
        self.table.setCellWidget(row_count, 1, medicine_name)

        # Amount as QTextEdit
        amount = QTextEdit()
        amount.setMinimumHeight(30)
        self.table.setCellWidget(row_count, 2, amount)

        # Dosage as QComboBox
        dosage = QComboBox()
        dosage.addItems(["1 - 0 - 0", "0 - 1 - 0", "0 - 0 - 1", "1 - 1 - 0", "0 - 1 - 1", "1 - 0 - 1", "1 - 1 - 1"])
        self.table.setCellWidget(row_count, 3, dosage)

        # Before/After Meal as QComboBox
        before_after = QComboBox()
        before_after.addItems(["Before", "After"])
        self.table.setCellWidget(row_count, 4, before_after)

        # Duration as QTextEdit
        duration = QTextEdit()
        duration.setMinimumHeight(30)
        self.table.setCellWidget(row_count, 5, duration)

    def remove_last_row(self):
        row_count = self.table.rowCount()
        if row_count > 0:
            self.table.removeRow(row_count - 1)

    def saveMed(self):
        data = []
        row_count = self.table.rowCount()
        for row in range(row_count):
            medicine_name_item = self.table.cellWidget(row, 1)
            amount_item = self.table.cellWidget(row, 2)
            dosage_item = self.table.cellWidget(row, 3)
            before_after_item = self.table.cellWidget(row, 4)
            duration_item = self.table.cellWidget(row, 5)

            data.append({
                "S.No.": row + 1,
                "Medicine Name": medicine_name_item.toPlainText(),
                "Amount": amount_item.toPlainText(),
                "Dosage": dosage_item.currentText(),
                "Before/After Meal": before_after_item.currentText(),
                "Duration (in days)": duration_item.toPlainText()
            })
        self.data_manager.update_medicines(data)
        print("Medicines saved to JSON:", data)

class TestTable(QMainWindow):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager    
        self.setWindowTitle("Prescribed Tests")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["S.No.", "Name of Test"])

        self.layout.addWidget(self.table)

        self.add_test_button = QPushButton("Add Test", self)
        self.add_test_button.clicked.connect(self.add_test)

        self.remove_test_button = QPushButton("Remove Last Test", self)
        self.remove_test_button.clicked.connect(self.remove_last_test)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.saveTests)

        self.layout.addWidget(self.add_test_button)
        self.layout.addWidget(self.remove_test_button)
        self.layout.addWidget(self.save_button)

        self.load_data()  # Load existing data when initialized

    def load_data(self):
        tests = self.data_manager.get_tests()
        for test in tests:
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            self.table.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))
            self.table.setCellWidget(row_count, 1, QTextEdit(test["Name of Test"]))


    def add_test(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))

        # Name of Test as QTextEdit
        test_name = QTextEdit()
        test_name.setMinimumHeight(30)
        self.table.setCellWidget(row_count, 1, test_name)

    def remove_last_test(self):
        row_count = self.table.rowCount()
        if row_count > 0:
            self.table.removeRow(row_count - 1)

    def saveTests(self):
        data = []
        row_count = self.table.rowCount()
        for row in range(row_count):
            test_name_item = self.table.cellWidget(row, 1)

            data.append({
                "S.No.": row + 1,
                "Name of Test": test_name_item.toPlainText()
            })
        self.data_manager.update_tests(data)
        print(data)


class DietTable(QMainWindow):
    def __init__(self, data_manager):
        super().__init__()

        self.data_manager = data_manager
        self.setWindowTitle("Prescribed Diet")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.nutrients = [
            "Vitamin A", "Vitamin B", "Protein", "Omega-3", "Fiber",
            "Calcium", "Iron", "Magnesium", "Potassium", "Zinc",
            "Vitamin C", "Vitamin D", "Vitamin E", "Folic Acid", 
            "Sodium", "Saturated Fat", "Trans Fat", "Cholesterol", 
            "Sugar", "Carbohydrates", "Fat"
        ]

        self.checkboxes = {}
        for nutrient in self.nutrients:
            checkbox = QCheckBox(nutrient)
            self.layout.addWidget(checkbox)
            self.checkboxes[nutrient] = checkbox

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.saveDiet)
        self.layout.addWidget(self.save_button)

        self.load_data()  # Load existing data when initialized

    def load_data(self):
        selected_nutrients = self.data_manager.get_diet()
        for nutrient in selected_nutrients: 
            if nutrient in self.checkboxes:
                self.checkboxes[nutrient].setChecked(True)
    
    def saveDiet(self):
        selected_nutrients = [nutrient for nutrient, checkbox in self.checkboxes.items() if checkbox.isChecked()]
        self.data_manager.update_diet(selected_nutrients)
        print(json.dumps(selected_nutrients))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.data_manager = DataManager()
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        assign_button = QPushButton("Assign Prescription", self)
        assign_button.clicked.connect(self.on_assign_prescription_click)


        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.scada_btn_2.setChecked(True)

        self.connect_signals()

    def on_assign_prescription_click(self):
        self.data_manager.assign_prescription()

    def open_dynamic_table(self):
        self.dynamic_table_window = MedTable(self.data_manager)
        self.dynamic_table_window.show()

    def open_test_table(self):
        self.test_table_window = TestTable(self.data_manager)
        self.test_table_window.show()

    def open_diet_table(self):
        self.diet_table_window = DietTable(self.data_manager)
        self.diet_table_window.show()

    def connect_signals(self):
        self.ui.scada_btn_1.toggled.connect(self.on_scada_btn_1_toggled)
        self.ui.scada_btn_2.toggled.connect(self.on_scada_btn_2_toggled)
        self.ui.luna_btn_1.toggled.connect(self.on_luna_btn_1_toggled)
        self.ui.luna_btn_2.toggled.connect(self.on_luna_btn_2_toggled)
        self.ui.hopper_btn_1.toggled.connect(self.on_hopper_btn_1_toggled)
        self.ui.hopper_btn_2.toggled.connect(self.on_hopper_btn_2_toggled)
        self.ui.head_btn_1.toggled.connect(self.on_head_btn_1_toggled)
        self.ui.head_btn_2.toggled.connect(self.on_head_btn_2_toggled)
        self.ui.tail_btn_1.toggled.connect(self.on_tail_btn_1_toggled)
        self.ui.tail_btn_2.toggled.connect(self.on_tail_btn_2_toggled)
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.dynamic_table_btn.clicked.connect(self.open_dynamic_table)  # Dynamic table for medicines
        self.ui.dynamic_table_btn_2.clicked.connect(self.open_test_table)  # Dynamic table for tests
        self.ui.dynamic_table_btn_3.clicked.connect(self.open_diet_table)  # Dynamic table for diet
        self.ui.stackedWidget.currentChanged.connect(self.on_stackedWidget_currentChanged)

    ## Function for searching   
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):   
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        search_text = self.ui.search_input.text().strip()
        
        if search_text:
            try:
                results = self.data_manager.get_patients(search_text)
                print(results)
                
                if results:  # Ensure results is not an empty list
                    first_patient = results[0]  # Access the first patient in the list
                    
                    # Extract patient details
                    patient_details = {
                        "user_id": first_patient.get("user_id"),
                        "full_name": first_patient.get("full_name"),
                        "age": first_patient.get("other_details", {}).get("age")
                    }

                    # Save patient details to data.json
                    with open("data.json", "w") as json_file:
                        json.dump(patient_details, json_file, indent=4)
                    
                    print(f"Patient details saved to data.json: {patient_details}")
                    
                    # Display results on the UI (if applicable)
                    self.display_patient_results_hist(results)
                    self.display_patient_results_pres(results)
                    
                else:
                    self.ui.label_15.setText("No patient found.")
                    self.ui.label_8.setText("")

            except Exception as e:
                self.ui.label_15.setText("Error fetching data.")
                self.ui.label_8.setText("")
                print(e)



    def display_patient_results_pres(self, results):
        if results:
            # Assuming you want to display details for the first matching patient
            patient = results[0]
            self.ui.label_15.setText(f"Name: {patient['full_name']}")
            # Accessing the 'age' field from the 'other_details' dictionary
            self.ui.label_8.setText(f"Age: {patient['other_details']['age']}")
        else:
            # Clear labels if no results found
            self.ui.label_15.setText("~ No results found ~")
            self.ui.label_8.setText("~")

    
    def display_patient_results_hist(self, results):
        if results:
            # Assuming you want to display details for the first matching patient
            patient = results[0]
            
            self.ui.label_25.setText(f"Name: {patient['full_name']}")
            self.ui.label_57.setText(f"Age: {patient['other_details']['age']}")
        else:
            # Clear labels if no results found
            self.ui.label_25.setText("~ No results found ~")
            self.ui.label_57.setText("~")

    ## functions for changing menu page
    def on_scada_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_scada_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_luna_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_luna_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_hopper_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_hopper_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_head_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_head_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_tail_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_tail_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_power_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_power_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_history_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_history_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def on_stackedWidget_currentChanged(self, index):
        if index == 0:
            # Update SCADA page elements
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load style file
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())   