import threading
from block import Block 
from blockchain import BlockChain 
import random
import copy
import time
import numpy as np

class Miner(threading.Thread):
	
	process_flag = 1
	
	def __init__(self, name, blockchain, transactions, possible_chains, queue_lock):
		threading.Thread.__init__(self)
		self.name = name
		self.blockchain = blockchain
		self.transactions = transactions
		self.possible_chains = possible_chains
		self.queue_lock = queue_lock
		self.no_load = 0

	def run(self):
		print('Miner ' + self.name + ' has started working...')
		self.process_data()
		print('Miner ' + self.name + ' has stopped working...')

	def process_data(self):
		while Miner.process_flag:
			self.queue_lock.acquire()
			self.replace_longest_blockchain()
			self.queue_lock.release()

			self.queue_lock.acquire()
			leftover_transactions = self.calc_leftover_transactions()
			self.queue_lock.release()

			if leftover_transactions:
				self.no_load = 0
				next_transaction = leftover_transactions.pop()
				self.blockchain.mine_block(Block(next_transaction, self.blockchain.items[-1].get_hash(), self.name))
				self.queue_lock.acquire()
				self.possible_chains.append(copy.deepcopy(self.blockchain))
				self.queue_lock.release()
				time.sleep(random.randint(1,5))
			else:
				self.no_load += 1
				time.sleep(1)

			if self.no_load==10:
				Miner.process_flag = 0

	def calc_leftover_transactions(self):
		mined_transactions_hashvalue = [block.tdata.hash_value for block in self.blockchain.items]
		return([transaction for transaction in self.transactions if transaction.hash_value not in mined_transactions_hashvalue])

	def replace_longest_blockchain(self):
		longest_blockchain_length = max([len(x.get_chain()) for x in self.possible_chains])
		actual_blockchain_length = len(self.blockchain.items)
		if longest_blockchain_length > actual_blockchain_length:
			index = np.argmax([len(x.get_chain()) for x in self.possible_chains])
			self.blockchain = copy.deepcopy(self.possible_chains[index])