import datetime as dt
import hashlib as hl
from transaction import Transaction

class Block:
	
	def __init__(self, tdata, previous_hash, miner_name):
		self.nonce = 0
		self.tdata = tdata
		self.previous_hash = previous_hash
		self.block_hash = self.generate_hash()
		self.miner_name = miner_name

	def get_hash(self):
		return self.generate_hash()

	def generate_hash(self):		
		h = hl.sha256()
		h.update(
	        str(self.nonce).encode('utf-8') +
	        str(self.tdata.amount).encode('utf-8') +
	        str(self.tdata.sender_key).encode('utf-8') +
	        str(self.tdata.receiver_key).encode('utf-8') +
	        str(self.tdata.timestamp).encode('utf-8')
		)
		return h.hexdigest()

	def __str__(self):
		return(
			str('****************************************************************') + '\n' +
			str(self.tdata) + '\n' + 
			str(self.previous_hash) + '\n' +
			str(self.get_hash()) + '\n' +
			str(self.miner_name) + '\n' +
			str(self.nonce) + '\n'
		)