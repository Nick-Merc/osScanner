from PyQt5 import QtCore, QtGui, QtWidgets

def clearData(window):
    window.lE_ip.setText("")
    window.lE_domain.setText("")
    window.li_addresses.clear()
    window.li_nameservers.clear()
    window.li_ports.clear()
    window.li_webserver.clear()
    window.li_whois.clear()

def cleanReq(request):
    validLine = False
    firstChar = True
    invalidChars = {'#'}

    request = request.splitlines()

    returnVal = ""

    for i in request:
        tmp = i.split()

        if (len(tmp) > 0):
            if (tmp[0] == "NetRange:"):
                validLine = True

            if (validLine):
                returnVal += i
                returnVal += '\n'

            if (validLine):
                if (tmp[0] == "OrgAbuseRef:"):
                    validLine = False

    if (len(returnVal) <= 0):
        returnVal = "No Whois data detected."

    return(returnVal)

def addComboItem(window):
    window.comboBox.addItem(window.targets[window.iteration].name)
    window.comboBox.setItemText(window.iteration, window.targets[window.iteration].name)