import datetime as dt
import hashlib as hl

class Block:

	blockNo 	= 0
	nofAttempt 	= 0
	timestamp 	= None
	data 		= None
	prev_hash 	= 0
	genr_hash 	= None
	next_block 	= None

	def __init__(self, data):
		self.data = data

	def hashgen(self):		
		h = hl.sha256()
		h.update(
	        str(self.timestamp).encode('utf-8') +
	        str(self.nofAttempt).encode('utf-8') +
	        str(self.data).encode('utf-8')
		)

		return h.hexdigest()

	def __str__(self):
		return(
			str(self.blockNo) + '\n' + 
			str(self.data) + '\n' + 
			str(self.prev_hash) + '\n' +
			str(self.hashgen()) + '\n' +
			str(self.nofAttempt)
		)