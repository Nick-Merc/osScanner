import os
import requests

def verifyIP(ipAddress):
    validity = False
    dotCount = 0

    for char in ipAddress:
        if (char == '.'):
            dotCount += 1

    if (dotCount == 3):
        validity = True
        tmp = ipAddress.split('.')
        for num in tmp:
            if (len(num) > 0):
                if (int(num) > 255 or int(num) < 0):
                    validity = False
            else:
                validity = False
                break

    return(validity)

def verifyDomain(domain):
    validity = False
    validTLDs = { 'com', 'net', 'org', 'gov', 'io'}

    count = 0
    for letter in domain:
        if (letter == '.'):
            count += 1

    if (count == 1):
        tmp = domain.split('.')
        tld = tmp[1]

        for suffix in validTLDs:
            if (tld == suffix):
                validity = True
                break

    return(validity)

def getA(domain):
    tmp = os.popen(f"nslookup -q=A {domain}").read()
    tmp = tmp.split()
    returnAddress = ""

    count = 0
    for word in tmp:
        if (count >= 2):
            returnAddress += word
            returnAddress += ' '

        if (word == "Address:") or (word == "Addresses:"):
            count += 1

    return(returnAddress)

def getNS(address):
    tmp = os.popen(f"nslookup -q=NS {address}").read()
    tmp = tmp.split()
    returnAddresses = ""
    timer = -1;

    startRead = False
    for word in tmp:
        if (word == "nameserver"):
            timer = 2;

        if (timer == 0):
            returnAddresses += word
            returnAddresses += ' '

        timer -= 1

    return(returnAddresses)

def getWebServer(domain):

    try:
        req = requests.head(f"https://{domain}").headers
        returnVal = ""
        returnVal = req["server"]

        if (len(returnVal) <= 0):
            returnVal = "No server detected."
    except:
        returnVal = "Connection Failed."

    return(returnVal)