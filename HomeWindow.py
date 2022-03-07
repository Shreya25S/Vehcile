import re

from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit,QMainWindow,QHBoxLayout,QFrame,QGridLayout,QComboBox,QTableWidget,QTableWidgetItem
from DataBaseOperation import DBOperation
from PyQt5.QtWidgets import QHeaderView
import PyQt5.QtGui

class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.dbOperation = DBOperation()
        widget = QWidget()
        widget.setStyleSheet("background:#fff")
        layout_horizontal = QHBoxLayout()
        menu_vertical_layout = QVBoxLayout()

        self.btn_home = QPushButton('Home')
        self.btn_add = QPushButton('Add Vehicle')
        self.btn_manage = QPushButton('Manage Vehicle')
        self.btn_history = QPushButton("History")

        menu_vertical_layout.setContentsMargins(0,0,0,0)
        menu_vertical_layout.setSpacing(0)

        self.btn_home.setStyleSheet("width:200px;height:160px;font-size:20px;background:black;color:white;font-weight:bold;border:1px solid black")
        self.btn_add.setStyleSheet("width:200px;height:160px;font-size:20px;background:black;color:white;font-weight:bold;border:1px solid black")
        self.btn_manage.setStyleSheet("width:200px;height:160px;font-size:20px;background:black;color:white;font-weight:bold;border:1px solid black")
        self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:black;color:white;font-weight:bold;border:1px solid black")


        self.btn_home.clicked.connect(self.showHome)
        self.btn_add.clicked.connect(self.showAdd)
        self.btn_manage.clicked.connect(self.showManage)
        self.btn_history.clicked.connect(self.showHistory)

        menu_frame = QFrame()
        menu_vertical_layout.addWidget(self.btn_home)
        menu_vertical_layout.addWidget(self.btn_add)
        menu_vertical_layout.addWidget(self.btn_manage)
        menu_vertical_layout.addWidget(self.btn_history)

        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        #menu_frame.setMinimumWidth(200)
        #menu_frame.setMaximumHeight(200)

        parent_vertical = QVBoxLayout()
        parent_vertical.setContentsMargins(0,0,0,0)
        self.vertical_1 = QVBoxLayout()
        self.addHomePageData()

        #label_home = QLabel('Home')
        #self.vertical_1.addWidget(label_home)

        self.vertical_2 = QVBoxLayout()
        self.vertical_2.setContentsMargins(0,0,0,0)
        self.addVehiclePage()
        #label_add_vehicle = QLabel('Add vehicle')
        #self.vertical_2.addWidget(label_add_vehicle)

        self.vertical_3 = QVBoxLayout()
        self.vertical_3.setContentsMargins(0,0,0,0)
        self.addManagePage()
        #label_manage = QLabel('Manage')
        #self.vertical_3.addWidget(label_manage)

        self.vertical_4 = QVBoxLayout()
        self.vertical_4.setContentsMargins(0,0,0,0)
        self.addHistoryPage()
        #label_history = QLabel('History')
        #self.vertical_4.addWidget(label_history)


        self.frame_1 = QFrame()
        self.frame_1.setMinimumWidth(self.width())
        self.frame_1.setMaximumWidth(self.width())
        self.frame_1.setMaximumHeight(self.width())
        self.frame_1.setMaximumHeight(self.width())


        self.frame_1.setLayout(self.vertical_1)
        self.frame_2 = QFrame()
        self.frame_2.setLayout(self.vertical_2)
        self.frame_3 = QFrame()
        self.frame_3.setLayout(self.vertical_3)
        self.frame_4 = QFrame()
        self.frame_4.setLayout(self.vertical_4)

        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)

        layout_horizontal.addWidget(menu_frame)
        layout_horizontal.addLayout(parent_vertical)
        layout_horizontal.setContentsMargins(0,0,0,0)
        parent_vertical.setContentsMargins(0,0,0,0)
        parent_vertical.addStretch()
        #menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()
        widget.setLayout(layout_horizontal)
        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.setCentralWidget(widget)

    def showHistory(self):
        # self.btn_history.setStyleSheet("width:200px;height:160px;font-size:20px;background:black;color:white;font-weight:bold;border:1px solid black")

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()

    def showAdd(self):
        self.frame_1.hide()
        self.frame_2.show()
        self.frame_3.hide()
        self.frame_4.hide()

    def showManage(self):
        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.show()
        self.frame_4.hide()

    def showHome(self):
        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()


    def addHomePageData(self):
        try:
            self.vertical_1.setContentsMargins(0,0,0,0)

            vertical_layout = QVBoxLayout()
            vertical_layout.setContentsMargins(0,0,0,0)

            frame = QFrame()

        #frame.setStyleSheet("background-color:#000000")

            horizontal = QHBoxLayout()
            horizontal.setContentsMargins(0,0,0,0)
            label = QLabel("Home")
            label.setStyleSheet("background:white;color:black;font-size:18px;font-weight:bold;width:500px;height:30px;padding:10px;border:1px solid white")
            horizontal.addWidget(label)
            vertical_layout.addLayout(horizontal)


            alldata = self.dbOperation.getSlotSpace()
            print(alldata)
            self.gridLayout = QGridLayout()
            self.gridLayout.setContentsMargins(0,0,0,0)
            self.gridLayout.setHorizontalSpacing(0)
            self.gridLayout.setVerticalSpacing(0)
            vertical_layout.addLayout(self.gridLayout)

            row = 0
            i = 0
            for data in alldata:
                label = QPushButton("Slot "+str(data[0]))
                if data[3] ==1:
                    label.setStyleSheet("background-color:green;color:white;padding:5px;width:100px;height:100px;border:1px solid white;text-align:center;font-weight:bold")
                else:
                    label.setStyleSheet("background-color:red;color:white;padding:5px;width:100px;height:100px;border:1px solid white;text-align:center;font-weight:bold")

                if i%5 == 0:
                    i =0
                    row = row+1

                self.gridLayout.addWidget(label,row,i)
                i = i+1

            frame.setLayout(vertical_layout)
            self.vertical_1.addWidget(frame)
            self.vertical_1.addStretch()

        except:
            print("Error occured please try again")


    def addVehiclePage(self):
        try:
            layout = QVBoxLayout()
            frame = QFrame()

            label = QLabel("Add Vehicle")
            label.setStyleSheet("background:white;color:black;font-size:25px;font-weight:bold;width:500px;height:30px;padding:10px;border:1px solid white")

            name_label = QLabel("Name :")
            name_label.setStyleSheet("color:black;padding:8px 0px;font-size:20px")
            mobile_label = QLabel("Mobile :")
            mobile_label.setStyleSheet("color:black;padding:8px 0px;font-size:20px")
            vehicle_label = QLabel("Vehicle no :")
            vehicle_label.setStyleSheet("color:black;padding:8px 0px;font-size:20px")
            vehicle_type = QLabel("Vehicle type :")
            vehicle_type.setStyleSheet("color:black;padding:8px 0px;font-size:20px")

            error_label = QLabel("")
            error_label.setStyleSheet("color:red")

            name_input = QLineEdit()
            name_input.setStyleSheet("color:black;padding:8px 0px;font-size:20px")
            mobile_input = QLineEdit()
            mobile_input.setStyleSheet("color:black;padding:8px 0px;font-size:20px")
            vehicle_input = QLineEdit()
            vehicle_input.setStyleSheet("color:black;padding:8px 0px;font-size:20px")
            vtype = QComboBox()
            vtype.setStyleSheet("color:black;padding:8px 0px;font-size:14px")
            vtype.addItem("2 wheeler")
            vtype.addItem("4 wheeler")


            button = QPushButton("Add vehicle")
            button.setStyleSheet("color:white;padding:8px 0px;font-size:20px;background-color:black;border:1px solid white")

            layout.addWidget(label)
            layout.addWidget(name_label)
            layout.addWidget(name_input)
            layout.addWidget(mobile_label)
            layout.addWidget(mobile_input)
            layout.addWidget(vehicle_label)
            layout.addWidget(vehicle_input)
            layout.addWidget(vehicle_type)
            layout.addWidget(vtype)
            layout.addWidget(button)
            layout.addWidget(error_label)


            layout.setContentsMargins(0,0,0,0)
            frame.setMinimumHeight(self.height())
            frame.setMinimumWidth(self.width())
            frame.setMaximumHeight(self.width())
            frame.setMaximumWidth(self.width())

            layout.addStretch()
            frame.setLayout(layout)
            button.clicked.connect(lambda : self.addVehicles(name_input.text(),vehicle_input.text(),mobile_input.text(),vtype.currentIndex(),error_label))
            self.vertical_2.addWidget(frame)
        except:
            print("Please try again")

    def addVehicles(self,name,vehicleno,mobile,index,error_label):
        try:
            vtp = 2
            if index == 0:
                vtp = 2
            else:
                vtp = 4

            mob_reg = 0
            #vno_reg = 0
            mob_reg = re.compile("(0|91)?[7-9]?[0-9]{9}$")
            #print(temp.match(mobile))
            #print(re.match('^[a-zA-Z0-9]+$',vehicleno))


            if mob_reg.match(mobile):
                if re.match('^[a-zA-Z0-9]+$',vehicleno):
                    data = self.dbOperation.AddVehicles(name, vehicleno, mobile, str(vtp))
                else:
                    error_label.setText("Incorrect mobile or vehicle no")
            

            if data == True:
                error_label.setText("Added Successfully")
            elif data == False:
                error_label.setText("Failed to Add Vehicle")
            else:
                error_label.setText(str(data))
        except:
            print("Enter the values properly")


    def addManagePage(self):
        data = self.dbOperation.getCurrentVehicle()
        self.table = QTableWidget()
        self.table.setStyleSheet("background:white;color:black;font-weight:bold;border:1px solid black")
        self.table.resize(self.width(),self.height())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)

        button = QPushButton("Refresh")
        button.setStyleSheet("background:black;color:white;font-size:10px")
        button.clicked.connect(self.refreshManage)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Vehicle No"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Mobile"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Vehicle Type"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Entry Time"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Action"))

        loop = 0
        for smalldata in data:
            self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            #self.table.setItem(loop, 6, QTableWidgetItem(''))
            self.button_exit = QPushButton("Exit")
            self.button_exit.setStyleSheet("background:black;color:white")
            self.table.setCellWidget(loop,6,self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)
            loop = loop+1


        frame = QFrame()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.table)
        frame.setLayout(layout)
        layout.addWidget(button)
        frame.setContentsMargins(0,0,0,0)
        frame.setMaximumWidth(self.width())
        frame.setMinimumWidth(self.width())
        frame.setMaximumHeight(self.height())
        frame.setMinimumHeight(self.height())
        self.vertical_3.addWidget(frame)
        self.vertical_3.addStretch()

    #to refresh manage page
    def refreshManage(self):
        data = self.dbOperation.getCurrentVehicle()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(7)
        loop = 0
        for smalldata in data:
            self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            self.button_exit = QPushButton("Exit")
            self.button_exit.setStyleSheet("background:black;color:white;font-size:10px")
            self.table.setCellWidget(loop, 6, self.button_exit)
            self.button_exit.clicked.connect(self.exitCall)
            loop = loop + 1

    def addHistoryPage(self):
        data = self.dbOperation.getAllVehicle()
        self.table1 = QTableWidget()
        self.table1.setStyleSheet("background:white;color:black;font-weight:bold;border:1px solid black")
        self.table1.resize(self.width(),self.height())
        self.table1.setRowCount(len(data))
        self.table1.setColumnCount(7)

        #to refesh page
        button = QPushButton("Refresh")
        button.setStyleSheet("background:black;color:white")
        button.clicked.connect(self.refreshHistory)

        self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table1.setHorizontalHeaderItem(2, QTableWidgetItem("Vehicle No"))
        self.table1.setHorizontalHeaderItem(3, QTableWidgetItem("Mobile"))
        self.table1.setHorizontalHeaderItem(4, QTableWidgetItem("Vehicle Type"))
        self.table1.setHorizontalHeaderItem(5, QTableWidgetItem("Entry Time"))
        self.table1.setHorizontalHeaderItem(6, QTableWidgetItem("Exit Time"))

        loop = 0
        for smalldata in data:
            self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
            loop = loop+1


        self.frame1 = QFrame()
        self.layout1 = QVBoxLayout()
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.setSpacing(0)
        self.layout1.addWidget(self.table1)
        self.frame1.setLayout(self.layout1)
        self.layout1.addWidget(button)
        self.frame1.setContentsMargins(0, 0, 0, 0)
        self.frame1.setMaximumWidth(self.width())
        self.frame1.setMinimumWidth(self.width())
        self.frame1.setMaximumHeight(self.height())
        self.frame1.setMinimumHeight(self.height())
        self.vertical_4.addWidget(self.frame1)
        self.vertical_4.addStretch()

    def refreshHistory(self):
        self.table1.clearContents()
        data = self.dbOperation.getAllVehicle()
        loop = 0
        self.table1.setRowCount(len(data))
        self.table1.setColumnCount(7)
        for smalldata in data:
            self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
            self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
            self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
            self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
            self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
            self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
            self.table1.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
            loop = loop + 1



    def exitCall(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            id = str(self.table.item(row,0).text())
            self.dbOperation.exitVehicle(id)
            self.table.removeRow(row)






