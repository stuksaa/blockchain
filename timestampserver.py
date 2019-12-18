import threading
from transaction import Transaction
import random
import datetime as dt

class TimeStampServer(threading.Thread):

	exitflag = 1
	client_ids = ['A','B','C','D','E','F','G']
	trans_vals = [10, 20, 15, 30, 40]

	def __init__(self, transactions, queueLock):
		threading.Thread.__init__(self)
		print('Timestamp Server is starting...')
		self.transactions = transactions
		self.queueLock = queueLock

	def run(self):
		while TimeStampServer.exitflag:
			amount = random.choice(TimeStampServer.trans_vals)
			sender = random.choice(TimeStampServer.client_ids)
			receiver = random.choice(TimeStampServer.client_ids)
			transaction = Transaction(amount,sender,receiver,dt.datetime.now())
			self.queueLock.acquire()
			self.transactions.put(transaction)
			self.queueLock.release()

