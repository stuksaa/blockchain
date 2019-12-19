import threading
from transaction import Transaction
import random
import datetime as dt
import time

class TimeStampServer(threading.Thread):

	exitflag = 1
	time_factor = 3
	future_transactions =  [[10,'A','B'],
							[20,'A','D'],
							[30,'C','B'],
							[20,'B','C'],
							[10,'A','B'],
							[40,'D','A'],
							[20,'A','B'],
							[30,'C','D']]

	def __init__(self, transactions, queue_lock):
		threading.Thread.__init__(self)
		print()
		print('Timestamp Server is starting...')
		print()
		self.transactions = transactions
		self.queue_lock = queue_lock

	def run(self):
		for t in self.future_transactions:
			transaction = Transaction(t[0],t[1],t[2],dt.datetime.now())
			self.queue_lock.acquire()
			self.transactions.insert(0,transaction)
			self.queue_lock.release()
			self.send_message(transaction)
			time.sleep(random.random()*TimeStampServer.time_factor)

	def send_message(self, transaction):
		print()
		print('Dear Miners! The following transaction has been sent:')
		print(str(transaction))
		print()