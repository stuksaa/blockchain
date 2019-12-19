import datetime as dt
import hashlib as hl
from transaction import Transaction

class Block:

	nonce				= 0
	block_hash 			= None
	previous_hash 		= None
	tdata 				= None
	
	def __init__(self, tdata, previous_hash, miner_name):
		self.tdata = tdata
		self.previous_hash = previous_hash
		self.block_hash = self.generateHash()
		self.miner_name = miner_name

	def getHash(self):
		return self.generateHash()

	def getPreviousHash(self):
		return self.previous_hash

	def getIndex(self):
		return self.index

	def generateHash(self):		
		h = hl.sha256()
		h.update(
	        str(self.nonce).encode('utf-8') +
	        str(self.tdata.amount).encode('utf-8') +
	        str(self.tdata.senderKey).encode('utf-8') +
	        str(self.tdata.receiverKey).encode('utf-8') +
	        str(self.tdata.timestamp).encode('utf-8')
		)

		return h.hexdigest()

	def isvalidHash(self):
		return self.generateHash() == self.getHash()

	def __str__(self):
		return(
			str('****************************************************************') + '\n' +
			str(self.tdata) + '\n' + 
			str(self.previous_hash) + '\n' +
			str(self.getHash()) + '\n' +
			str(self.miner_name) + '\n' +
			str(self.nonce) + '\n'
		)