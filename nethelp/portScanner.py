import nmap
import sys

sys.path.insert(0, '../helpers')
import helpers.constants as constant

class PortScanner():
	ports = []

	def portScan(self, address):
		nm = nmap.PortScanner()

		for port in constant.COMMON_PORTS:
			try:
				print(0)
				nm.scan(address, port)

				print(1)

				result = list(nm[address]['tcp'].keys())[0]

				print(2)

				tmp = nm[address]['tcp'][int(port)]['state']

				print(3)

				result = f"{result} - {tmp}"

				print(4)

				self.ports.append(result)
			except:
				self.ports.append(f"Cannot scan port {port}.")