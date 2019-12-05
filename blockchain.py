import datetime as dt
import hashlib as hl
from block import Block

class BlockChain:

	block 	= Block("Genesis")
	head = block

	def add(self, block):
		block.prev_hash = self.block.hashgen()
		block.genr_hash = block.hashgen()
		bno = self.block.blockNo
		self.block.next_block = block
		self.block = self.block.next_block
		self.block.blockNo = bno + 1
		
	def mine(self, block):
		h = hl.sha256()
		notHash = True
		while notHash:
			block.timestamp = dt.datetime.now()
			hashgen = block.hashgen()
			if hashgen[0:4] == '0000':
				notHash = False
			else:
				block.nofAttempt += 1

		self.add(block)
