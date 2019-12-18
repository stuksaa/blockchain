import threading
from block import Block 
from blockchain import BlockChain 

class Miner(threading.Thread):
	
	exitflag = 1
	
	def __init__(self, name, blockchain, transactions, queueLock):
		threading.Thread.__init__(self)
		self.name = name
		self.blockchain = blockchain
		self.transactions = transactions
		self.queueLock = queueLock

	def run(self):
		print('Miner ' + self.name + ' has started working...')
		self.process_data()
		print('Miner ' + self.name + ' has stopped working...')

	def process_data(self):
		while Miner.exitflag:
			self.queueLock.acquire()
			if self.transactions.empty():
				self.queueLock.release()
			else:
				e = self.transactions.get()
				self.blockchain.mineblock(Block(e,self.blockchain.items[-1].getHash()))
				self.queueLock.release()
				print('This block has been mined by: ' + self.name)