import datetime as dt
import hashlib as hl
from block import Block
from transaction import Transaction

class BlockChain:

	def __init__(self):
		t = Transaction(None, None, None, dt.datetime.now())
		genesis = Block(t, None, 'Satoshi')
		self.items = [genesis]
		
	def mineblock(self, block):
		notHash = True
		while notHash:
			if block.getHash()[0:4] == '0000':
				notHash = False
			else:
				block.nonce += 1
				block.generateHash()

		self.items.append(block)

	def lastBlock(self):
		return self.items[-1]

	def firstBlock(self):
		return self.items[1] #first is not the genesis block

	def getChain(self):
		return self.items

	def printChain(self):
		for idx, e in enumerate(self.items):
			print(idx)
			print(str(e))