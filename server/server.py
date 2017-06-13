import time
class Server(object):
	def __init__(self, server_name = 'A John Server'):
		self.server_log_location = '/home/joschi/Dokumente/chat/server/server_log.txt'
		self.server_log = File
		self.is_online = True
		self.server_name = server_name
		self.server_message_amount = 0
		self.server_message = chat_log.messages
	def write_message(self, what, which = 'standart'):
		if which == 'standart':
			which = self.server_message_amount + 1
		else:
			pass
		self.server_message_amount = self.server_message_amount + 1
		self.server_message[which] = what
	def give_message(self, which):
		return self.server_message[which]
	def give_last_message(self):
		return self.server_message
	def server_stop(self, stop_message = 'Stop the Server'):
		self.write_message(stop_message)
