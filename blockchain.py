import datetime as dt
import hashlib as hl
from block import Block
from transaction import Transaction

class BlockChain:

	def __init__(self):
		t = Transaction(None, None, None, dt.datetime.now())
		genesis = Block(t, None, 'Satoshi')
		self.items = [genesis]
		
	def mine_block(self, block):
		notHash = True
		while notHash:
			if block.get_hash()[0:4] == '0000':
				notHash = False
			else:
				block.nonce += 1
				block.generate_hash()

		self.items.append(block)

	def get_chain(self):
		return self.items

	def print_chain(self):
		for idx, e in enumerate(self.items):
			print(str(idx) + '. block')
			print(str(e))