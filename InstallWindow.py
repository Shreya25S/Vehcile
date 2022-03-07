from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit
from LoginWindow import LoginScreen
import json
from DataBaseOperation import DBOperation

class InstallWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Install')
        self.resize(400,200)

        layout = QVBoxLayout()

        label_db_name = QLabel("Database name: ")
        label_db_username = QLabel("Database username: ")
        label_db_password = QLabel("Database password: ")
        label_admin_username = QLabel("admin username: ")
        label_admin_password = QLabel("admin password: ")
        label_no_of_two_seater = QLabel("No of 2 wheeler space: ")
        label_no_of_four_seater = QLabel("No of 4 wheeler space: ")

        self.input_db_name = QLineEdit()
        self.input_db_name.setText("vehicle_parking")

        self.input_db_username = QLineEdit()
        self.input_db_username.setText("vehicle_user")

        self.input_db_password = QLineEdit()
        self.input_db_password.setText("vehicle_password")

        self.input_admin_username = QLineEdit()
        self.input_admin_password = QLineEdit()
        self.input_two_wheeler = QLineEdit()
        self.input_four_wheeler = QLineEdit()

        buttonsave = QPushButton("save config")

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color:red")

        layout.addWidget(label_db_name)
        layout.addWidget(self.input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(self.input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(self.input_db_password)
        layout.addWidget(label_admin_username)
        layout.addWidget(self.input_admin_username)
        layout.addWidget(label_admin_password)
        layout.addWidget(self.input_admin_password)
        layout.addWidget(label_no_of_two_seater)
        layout.addWidget(self.input_two_wheeler)
        layout.addWidget(label_no_of_four_seater)
        layout.addWidget(self.input_four_wheeler)
        layout.addWidget(buttonsave)

        layout.addWidget(self.error_label)

        buttonsave.clicked.connect(self.showStepInfo)

        self.setLayout(layout)

    def showStepInfo(self):
        if self.input_db_name.text()=="":
            self.error_label.setText("Please enter DB name ")
            return

        if self.input_db_username.text()=="":
            self.error_label.setText("Please enter DB username ")
            return

        if self.input_db_password.text()=="":
            self.error_label.setText("Please enter DB password ")
            return

        if self.input_admin_username.text()=="":
            self.error_label.setText("Please enter Admin username ")
            return

        if self.input_admin_password.text()=="":
            self.error_label.setText("Please enter Admin password ")
            return

        if self.input_two_wheeler.text()=="":
            self.error_label.setText("Please enter Two wheeler space ")
            return

        if self.input_four_wheeler.text()=="":
            self.error_label.setText("Please enter four wheeler space ")
            return


        data = {"username":self.input_db_username.text(),"database":self.input_db_name.text(),"password":self.input_db_password.text()}
        file = open("./config.json","w")
        file.write(json.dumps(data))
        file.close()
        dbOperation = DBOperation()
        dbOperation.CreateTables()
        dbOperation.InsertAdmin(self.input_admin_username.text(),self.input_admin_password.text())
        dbOperation.InsertOneTimeData(int(self.input_two_wheeler.text()),int(self.input_four_wheeler.text()))


        self.close()
        self.login = LoginScreen()
        self.login.showLoginScreen()
        print("Save")



