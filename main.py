import numpy as np 
import datetime as dt 
import hashlib as hl 

class Block:

	blockNo = 0
	data = None
	prev_hash = None
	next_hash = None
	genr_hash = None
	timestamp = None

	def __init__(self, data):
		self.data = data
		timestamp = dt.datetime.now()

	def hashgen(self):		
		h = hl.sha224()
		h.update(
			str(self.timestamp).encode('utf-8')
		)

		return h.hexdigest()

	def __str__(self):
		return(
			str(self.blockNo) + '\n' + 
			str(self.data) + '\n' + 
			str(self.hashgen())
		)


class BlockChain:
	block = Block("Genesis")

	def add():
		

blockchain = BlockChain()

print(blockchain.block)



