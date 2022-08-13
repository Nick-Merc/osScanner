# Author: Nicholas Mercadante
# Project Name: nosScanner
# Project Description:
#     User can input domain or ip address
#     into the program to initiate a scan
#     of dns records as well as a direct
#     scan to reveal more information.
# Date Created: 8/8/2022
# Date Last Modified: 8/11/2022

from PyQt5 import QtCore, QtGui, QtWidgets

import nethelp.netFunctions as nethelp
from nethelp.portScanner import *
import helpers.helperFunctions as windowhelp
import helpers.constants as constant
from targetdata.targetData import *

import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lE_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_ip.setGeometry(QtCore.QRect(30, 60, 113, 22))
        self.lE_ip.setObjectName("lE_ip")
        self.l_ip_prompt = QtWidgets.QLabel(self.centralwidget)
        self.l_ip_prompt.setGeometry(QtCore.QRect(30, 20, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.l_ip_prompt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        self.l_ip_prompt.setFont(font)
        self.l_ip_prompt.setObjectName("l_ip_prompt")


        self.pB_scan1 = QtWidgets.QPushButton(self.centralwidget)
        self.pB_scan1.setGeometry(QtCore.QRect(150, 60, 75, 24))
        self.pB_scan1.setObjectName("pB_scan1")
        self.pB_scan1.clicked.connect(self.scanIP)


        self.l_domain_prompt = QtWidgets.QLabel(self.centralwidget)
        self.l_domain_prompt.setGeometry(QtCore.QRect(30, 140, 271, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l_domain_prompt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        self.l_domain_prompt.setFont(font)
        self.l_domain_prompt.setObjectName("l_domain_prompt")
        self.lE_domain = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_domain.setGeometry(QtCore.QRect(30, 180, 113, 22))
        self.lE_domain.setObjectName("lE_domain")


        self.pB_scan2 = QtWidgets.QPushButton(self.centralwidget)
        self.pB_scan2.setGeometry(QtCore.QRect(150, 180, 75, 24))
        self.pB_scan2.setObjectName("pB_scan2")
        self.pB_scan2.clicked.connect(self.scanDomain)


        self.l_addresses = QtWidgets.QLabel(self.centralwidget)
        self.l_addresses.setGeometry(QtCore.QRect(420, 30, 81, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l_addresses.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_addresses.setFont(font)
        self.l_addresses.setObjectName("l_addresses")
        self.l_nameservers = QtWidgets.QLabel(self.centralwidget)
        self.l_nameservers.setGeometry(QtCore.QRect(600, 30, 101, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l_nameservers.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_nameservers.setFont(font)
        self.l_nameservers.setObjectName("l_nameservers")
        self.l_ports = QtWidgets.QLabel(self.centralwidget)
        self.l_ports.setGeometry(QtCore.QRect(420, 200, 87, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l_ports.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_ports.setFont(font)
        self.l_ports.setObjectName("l_ports")
        self.l_webserver = QtWidgets.QLabel(self.centralwidget)
        self.l_webserver.setGeometry(QtCore.QRect(600, 200, 81, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l_webserver.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_webserver.setFont(font)
        self.l_webserver.setObjectName("l_webserver")
        self.l_whois = QtWidgets.QLabel(self.centralwidget)
        self.l_whois.setGeometry(QtCore.QRect(420, 370, 110, 21))
        self.l_whois.setPalette(palette)
        self.l_whois.setFont(font)
        self.l_whois.setObjectName("l_whois")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(420, 350, 111, 20))
        self.checkBox.setPalette(palette)
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 50, 89, 22))
        self.comboBox.setObjectName("comboBox")

        self.li_addresses = QtWidgets.QListWidget(self.centralwidget)
        self.li_addresses.setGeometry(QtCore.QRect(420, 50, 131, 131))
        self.li_addresses.setObjectName("li_addresses")
        self.li_nameservers = QtWidgets.QListWidget(self.centralwidget)
        self.li_nameservers.setGeometry(QtCore.QRect(600, 50, 131, 131))
        self.li_nameservers.setObjectName("li_nameservers")
        self.li_ports = QtWidgets.QListWidget(self.centralwidget)
        self.li_ports.setGeometry(QtCore.QRect(420, 220, 131, 131))
        self.li_ports.setObjectName("li_ports")
        self.li_webserver = QtWidgets.QListWidget(self.centralwidget)
        self.li_webserver.setGeometry(QtCore.QRect(600, 220, 131, 131))
        self.li_webserver.setObjectName("li_webserver")
        self.li_whois = QtWidgets.QListWidget(self.centralwidget)
        self.li_whois.setGeometry(QtCore.QRect(420, 390, 311, 131))
        self.li_whois.setObjectName("li_whois")
        self.l_background = QtWidgets.QLabel(self.centralwidget)
        self.l_background.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.l_background.setText("")
        self.l_background.setPixmap(QtGui.QPixmap(constant.BACKGROUND_PATH))
        self.l_background.setScaledContents(True)
        self.l_background.setWordWrap(False)
        self.l_background.setIndent(-1)
        self.l_background.setObjectName("l_background")
        self.l_background.raise_()
        self.lE_ip.raise_()
        self.l_ip_prompt.raise_()
        self.pB_scan1.raise_()
        self.l_domain_prompt.raise_()
        self.lE_domain.raise_()
        self.pB_scan2.raise_()
        self.l_addresses.raise_()
        self.l_nameservers.raise_()
        self.l_ports.raise_()
        self.l_webserver.raise_()
        self.l_whois.raise_()
        self.li_addresses.raise_()
        self.li_nameservers.raise_()
        self.li_ports.raise_()
        self.li_webserver.raise_()
        self.li_whois.raise_()
        self.checkBox.raise_()
        self.comboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.actionClear_Data = QtWidgets.QAction(MainWindow)
        self.actionClear_Data.setObjectName("actionClear_Data")
        self.menuActions.addAction(self.actionClear_Data)
        self.menubar.addAction(self.menuActions.menuAction())
        self.actionClear_Data.triggered.connect(lambda: windowhelp.clearData(self))

        self.targets = []
        self.iteration = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "nosScanner v1.0"))
        self.l_ip_prompt.setText(_translate("MainWindow", "Input Target IP Address:"))
        self.pB_scan1.setText(_translate("MainWindow", "Scan"))
        self.l_domain_prompt.setText(_translate("MainWindow", "Input Target Domain Name:"))
        self.pB_scan2.setText(_translate("MainWindow", "Scan"))
        self.l_addresses.setText(_translate("MainWindow", "Addresses:"))
        self.l_nameservers.setText(_translate("MainWindow", "Nameservers:"))
        self.l_ports.setText(_translate("MainWindow", "Open Ports:"))
        self.l_webserver.setText(_translate("MainWindow", "Webserver:"))
        self.l_whois.setText(_translate("MainWindow", "Whois Lookup:"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionClear_Data.setText(_translate("MainWindow", "Clear Data"))
        self.checkBox.setText(_translate("MainWindow", "Enable Port Scan"))


    def loadTargetData(target):
        windowhelp.clearData(self)

        for data in self.targets:
            if (target == data.name):
                selectedData = data
                break

        for address in selectedData.addresses:
            self.li_addresses.addItem(address)

        for nameserver in selectedData.nameservers:
            self.li_nameservers.addItem(nameserver)

        for port in selectedData.ports:
            self.li_ports.addItem(port)

        self.li_webserver.addItem(selectedData.webserver)

        for line in selectedData.whoisData.splitlines():
            self.li_whois.addItem(line)


    def scanIP(self):
        address = self.lE_ip.text()

        #Verification
        validIP = nethelp.verifyIP(address)

        if (validIP):
            #A
            self.li_addresses.addItem(address)
            
            #Port Scan
            if (self.checkBox.isChecked()):
                openPorts = scanner.portScan(address)
                for port in openPorts:
                    self.li_ports.addItem(str(port))

            #Web Server
            webserver = nethelp.getWebServer(address)
            self.li_webserver.addItem(webserver)

            #Whois

            try:
                req = requests.get(f'{constant.WHOIS}{address}')
                parsedData = windowhelp.cleanReq(req.text)
            except:
                parsedData = "Connection Failed"

            for line in parsedData.splitlines():
                self.li_whois.addItem(line)

            nameservers = []
            self.targets.append(TargetData(address, address, nameservers, 999, webserver, parsedData))
            windowhelp.addComboItem(self)

            self.iteration += 1


    def scanDomain(self):
        #Gets domain string from text edit box after pressing scan.
        domain = self.lE_domain.text()

        #Verification: Checks if domain is in proper form and has approved tld.
        validDomain = nethelp.verifyDomain(domain)

        if (validDomain):
            #A
            #Gets A records as list.
            addresses = nethelp.getA(domain)
            #Adds each record to gui list.
            for address in addresses:
                self.li_addresses.addItem(address)

            #NS
            #Gets NS records as list.
            nameservers = nethelp.getNS(domain)
            #Adds each record to gui list.
            for server in nameservers:
                self.li_nameservers.addItem(server)

            #Port Scan
            #Only execute if checkbox is checked:
            if (self.checkBox.isChecked()):
                #Scans first IP address in list; function returns 
                #list of open ports.
                scanner = PortScanner()
                scanner.portScan(addresses[0])
                # openPorts = scanner.portScan(addresses[0])
                #Adds each port to gui list.
                for port in scanner.ports:
                    self.li_ports.addItem(str(port))

            #Web Server
            #Gets webserver by making a head request; function
            #returns clean response.
            webserver = nethelp.getWebServer(domain)
            #Adds webserver to gui list.
            self.li_webserver.addItem(webserver)

            #Whois
            #Makes whois request to website.
            try:
                req = requests.get(f'{constant.WHOIS}{addresses[0]}')
                #Filters response; function returns only whois data.
                parsedData = windowhelp.cleanReq(req.text)

                #Adds each line of whois data to gui list.
                for line in parsedData.splitlines():
                    self.li_whois.addItem(line)
            except:
                self.li_whois.addItem("Connection Failed.")

            #Add all of target data to list; used to save data
            #while switching displayed information.
            self.targets.append(TargetData(domain, addresses, nameservers, 999, webserver, parsedData))

            #Add target to combo list for selection; selecting
            #target will display their scan's data.
            windowhelp.addComboItem(self)

            self.iteration += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())