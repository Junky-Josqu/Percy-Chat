import server
def create_client():
    print 'Welcome to to Server-Client.'
    print 'Servername:'
    name = raw_input()
    if name == 'default':
        print 'Create Server with default Name'
        server_client = Server_client()
    else:
        print 'Create Server with %s name' % (name)
        server_client = Server_client(name)
        
class Server_client(object):
	def __init__(self, server_name = 'A John Server'):
		self.server_name = server_name
		self.server_online = False
		self.server_client_show_interface()
	def server_on(self):
		self.server = server.Server(self.server_name)
		self.server_online = True
		print "Server is started"
	def server_off(self, stop_message = 'Stop Server'):
		print 'stop the Server'
		self.server.server_stop(stop_message)
		self.server = None
	def server_client_search_command(self, wanted_command):
		if wanted_command == 'stop':
			self.server_off()
		elif wanted_command == 'start':
			self.server_on()
		elif wanted_command != "":
			pass
		else:
			print 'Wrong Command'
		'''
	def server_client_interface(self, wanted_command):t
		print 'SERVER CLIENT: %s' % (self.server_name)
		#print self.server.give_last_message()
		self.server_client_search_command(wanted_command)
		'''
	def server_client_show_interface(self):
		i = 0
		print 'SERVER CLIENT: %s' % (self.server_name)

		while i == 0:
			new_command = raw_input()
			old_command = None
			if old_command != new_command:
				#print 'do command ' + new_command
				self.server_client_search_command(new_command)
				new_command = None
			else:
				print 'no command'
create_client()
