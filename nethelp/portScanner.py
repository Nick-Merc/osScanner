import nmap
import sys

sys.path.insert(0, '../helpers')

class PortScanner():
	scanResults = []

	def scan(self, address, ports):
		nm = nmap.PortScanner()

		for port in ports:
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

				self.scanResults.append(result)
			except:
				self.scanResults.append(f"Cannot scan port {port}.")