# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
# from pymongo import MongoClient

# class CRUDApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("CRUD Application")

#         self.client = MongoClient('mongodb+srv://prathameshgarade:masaladosa@ads.ddoy7h9.mongodb.net/')
#         self.db = self.client['test_database']
#         self.collection = self.db['test_collection']
# # mongodb+srv://prathameshgarade:masaladosa@ads.ddoy7h9.mongodb.net/
#         self.init_ui()

#     def init_ui(self):
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)

#         layout = QVBoxLayout()

#         self.name_input = QLineEdit()
#         self.age_input = QLineEdit()
#         self.update_input = QLineEdit()

#         layout.addWidget(QLabel("Name:"))
#         layout.addWidget(self.name_input)
#         layout.addWidget(QLabel("Age:"))
#         layout.addWidget(self.age_input)

#         insert_button = QPushButton("Insert")
#         insert_button.clicked.connect(self.insert_data)
#         layout.addWidget(insert_button)

#         layout.addWidget(QLabel("Update Age (by Name):"))
#         layout.addWidget(self.update_input)

#         update_button = QPushButton("Update")
#         update_button.clicked.connect(self.update_data)
#         layout.addWidget(update_button)

#         delete_button = QPushButton("Delete")
#         delete_button.clicked.connect(self.delete_data)
#         layout.addWidget(delete_button)

#         retrieve_button = QPushButton("Retrieve")
#         retrieve_button.clicked.connect(self.retrieve_data)
#         layout.addWidget(retrieve_button)

#         self.central_widget.setLayout(layout)

#     def insert_data(self):
#         name = self.name_input.text()
#         age = self.age_input.text()

#         if name and age:
#             data = {'name': name, 'age': age}
#             self.collection.insert_one(data)
#             QMessageBox.information(self, "Success", "Data inserted successfully!")
#             self.name_input.clear()
#             self.age_input.clear()
#         else:
#             QMessageBox.warning(self, "Error", "Please fill in both name and age fields!")

#     # def update_data(self):
#     #     name = self.update_input.text()
#     #     new_age = self.age_input.text()

#     #     if name and new_age:
#     #         query = {'name': name}
#     #         new_values = {"$set": {'age': new_age}}
#     #         self.collection.update_one(query, new_values)
#     #         QMessageBox.information(self, "Success", "Data updated successfully!")
#     #         self.update_input.clear()
#     #         self.age_input.clear()
#     #     else:
#     #         QMessageBox.warning(self, "Error", "Please fill in both name and age fields!")
#     def update_data(self):
#        name = self.name_input.text()
#        new_age = self.update_input.text()

#        if name and new_age:
#            query = {'name': name}
#            new_values = {"$set": {'age': new_age}}
#            result = self.collection.update_one(query, new_values)
#            if result.modified_count > 0:
#                QMessageBox.information(self, "Success", "Data updated successfully!")
#                self.update_input.clear()
#                self.age_input.clear()
#            else:
#             QMessageBox.warning(self, "Error", "No data found with that name!")
#        else:
#         QMessageBox.warning(self, "Error", "Please fill in both name and age fields!")


#     def delete_data(self):
#         name = self.name_input.text()

#         if name:
#             query = {'name': name}
#             result = self.collection.delete_one(query)
#             if result.deleted_count > 0:
#                 QMessageBox.information(self, "Success", "Data deleted successfully!")
#                 self.name_input.clear()
#             else:
#                 QMessageBox.warning(self, "Error", "No data found with that name!")
#         else:
#             QMessageBox.warning(self, "Error", "Please fill in the name field!")

#     def retrieve_data(self):
#         name = self.name_input.text()

#         if name:
#             query = {'name': name}
#             result = self.collection.find_one(query)
#             if result:
#                 QMessageBox.information(self, "Data Retrieved", f"Name: {result['name']}\nAge: {result['age']}")
#                 self.name_input.clear()
#             else:
#                 QMessageBox.warning(self, "Error", "No data found with that name!")
#         else:
#             QMessageBox.warning(self, "Error", "Please fill in the name field!")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CRUDApp()
#     window.setGeometry(100, 100, 400, 300)
#     window.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from pymongo import MongoClient

class CRUDApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Application")

        self.client = MongoClient('mongodb+srv://prathameshgarade:masaladosa@ads.ddoy7h9.mongodb.net/')
        self.db = self.client['test_database']
        self.collection = self.db['test_collection']

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Set background color and border-radius for the central widget
        self.central_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px;")

        self.name_input = QLineEdit()
        self.set_stylesheet(self.name_input)  # Apply styles to name_input

        self.age_input = QLineEdit()
        self.set_stylesheet(self.age_input)  # Apply styles to age_input

        self.update_input = QLineEdit()
        self.set_stylesheet(self.update_input)  # Apply styles to update_input

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)

        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.insert_data)
        self.set_button_style(insert_button)  # Apply styles to insert_button
        layout.addWidget(insert_button)

        layout.addWidget(QLabel("Update Age (by Name):"))
        layout.addWidget(self.update_input)

        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update_data)
        self.set_button_style(update_button)  # Apply styles to update_button
        layout.addWidget(update_button)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_data)
        self.set_button_style(delete_button)  # Apply styles to delete_button
        layout.addWidget(delete_button)

        retrieve_button = QPushButton("Retrieve")
        retrieve_button.clicked.connect(self.retrieve_data)
        self.set_button_style(retrieve_button)  # Apply styles to retrieve_button
        layout.addWidget(retrieve_button)

        self.central_widget.setLayout(layout)
        self.setStyleSheet("background-color: #d0d0d0;") 

    def set_stylesheet(self, widget):
        widget.setStyleSheet(
            """
            background-color: #ffffff; /* White background */
            color: #333; /* Dark text color */
            border-radius: 5px; /* Rounded corners */
            border: 2px solid #ccc; /* Gray border */
            padding: 5px 10px; /* Padding */
            """
        )

    def set_button_style(self, button):
        button.setStyleSheet(
            """
            background-color: #4CAF50; /* Green background */
            color: #ffffff; /* White text color */
            border-radius: 5px; /* Rounded corners */
            border: none; /* No border */
            padding: 5px 10px; /* Padding */
            """
        )

    def insert_data(self):
        name = self.name_input.text()
        age = self.age_input.text()

        if name and age:
            data = {'name': name, 'age': age}
            self.collection.insert_one(data)
            QMessageBox.information(self, "Success", "Data inserted successfully!")
            self.name_input.clear()
            self.age_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please fill in both name and age fields!")

    def update_data(self):
        name = self.name_input.text()
        new_age = self.update_input.text()

        if name and new_age:
            query = {'name': name}
            new_values = {"$set": {'age': new_age}}
            result = self.collection.update_one(query, new_values)
            if result.modified_count > 0:
                QMessageBox.information(self, "Success", "Data updated successfully!")
                self.update_input.clear()
                self.age_input.clear()
            else:
                QMessageBox.warning(self, "Error", "No data found with that name!")
        else:
            QMessageBox.warning(self, "Error", "Please fill in both name and age fields!")

    def delete_data(self):
        name = self.name_input.text()

        if name:
            query = {'name': name}
            result = self.collection.delete_one(query)
            if result.deleted_count > 0:
                QMessageBox.information(self, "Success", "Data deleted successfully!")
                self.name_input.clear()
            else:
                QMessageBox.warning(self, "Error", "No data found with that name!")
        else:
            QMessageBox.warning(self, "Error", "Please fill in the name field!")

    def retrieve_data(self):
        name = self.name_input.text()

        if name:
            query = {'name': name}
            result = self.collection.find_one(query)
            if result:
                QMessageBox.information(self, "Data Retrieved", f"Name: {result['name']}\nAge: {result['age']}")
                self.name_input.clear()
            else:
                QMessageBox.warning(self, "Error", "No data found with that name!")
        else:
            QMessageBox.warning(self, "Error", "Please fill in the name field!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CRUDApp()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
