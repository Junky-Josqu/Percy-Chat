#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

class Server(object):
	def __init__(self, server_name = 'A John Server'):
		self.server_log_location = "~/Documents/Percy-Chat/server/server_log.txt"
		self.server_log = open(self.server_log_location, "r")
		self.is_online = True
		self.server_name = server_name
		self.server_message_amount = 0

	def server_write_message(self, what, which = 'standart'):
		if which == 'standart':
			which = self.server_message_amount + 1
		else:
			pass
		self.server_message_amount = self.server_message_amount + 1
		self.server_log.write(what + '\n')
	def server_give_chat_log(self, which):
		return self.server_log.read()
		'''
	def server_show_log(self):
		print
		'''

	def server_stop(self, stop_message = 'Stop the Server'):
		self.server_log.close()
		self.write_message(stop_message)
