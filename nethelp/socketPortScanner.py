import socket

class PortScanner():
	portStates = []

	def scan(self, addr, ports):
		self.portStates.clear()
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)

		for port in ports:
			result = client.connect_ex((addr, port))
			if (result == 0):
				self.portStates.append(f"Port {port} is open.")
			else:
				self.portStates.append(f"Port {port} is closed.")