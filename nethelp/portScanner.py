import nmap
import sys

sys.path.insert(0, '../helpers')
import helpers.constants as constant

def portScan(address):
	nm = nmap.PortScanner()
	openPorts = []

	for port in constant.COMMON_PORTS:
		try:
			ports = f'{port}-{port}'
			nm.scan(address, ports)

			print(1)

			result = list(nm[address]['tcp'].keys())[0]

			print(2)

			tmp = nm[address]['tcp'][int(port)]['state']

			print(3)

			result = f"{result} - {tmp}"

			print(4)

			openPorts.append(result)
		except:
			print(f"Cannot scan port {port}.")

	return(openPorts)