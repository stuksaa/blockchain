import threading
from block import Block 
from blockchain import BlockChain 
import random
import copy
import time
import numpy as np

class Miner(threading.Thread):
	
	exitflag = 1
	
	def __init__(self, name, blockchain, transactions, possible_chains, queueLock):
		threading.Thread.__init__(self)
		self.name = name
		self.blockchain = blockchain
		self.transactions = transactions
		self.possible_chains = possible_chains
		self.queueLock = queueLock

	def run(self):
		print('Miner ' + self.name + ' has started working...')
		self.process_data()
		print('Miner ' + self.name + ' has stopped working...')

	def process_data(self):
		while Miner.exitflag:
			self.queueLock.acquire()
			if max([len(x.getChain()) for x in self.possible_chains]) > len(self.blockchain.items):
				index = np.argmax([len(x.getChain()) for x in self.possible_chains])
				self.blockchain = copy.deepcopy(self.possible_chains[index])
			self.queueLock.release()

			if not self.transactions:
				pass
			else:
				self.transactions = [x for x in self.transactions if x.hash_value not in [block.tdata.hash_value for block in self.blockchain.items]]
				
				if self.transactions:
					e = self.transactions.pop()
					self.blockchain.mineblock(Block(e,self.blockchain.items[-1].getHash(),self.name))
					self.queueLock.acquire()
					self.possible_chains.append(copy.deepcopy(self.blockchain))
					self.queueLock.release()
					time.sleep(random.randint(3,10))