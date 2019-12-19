import hashlib as hl

class Transaction():

	def __init__(self, amount, sender_key, receiver_key, timestamp):
		self.amount = amount
		self.sender_key = sender_key
		self.receiver_key = receiver_key
		self.timestamp = timestamp
		h = hl.sha256()
		h.update(
	        str(self.amount).encode('utf-8') +
	        str(self.sender_key).encode('utf-8') +
	        str(self.receiver_key).encode('utf-8') +
	        str(self.timestamp).encode('utf-8')
		)
		self.hash_value = h.hexdigest()

	def __str__(self):
		return( str(self.hash_value) + '\n' +
				'amount: ' + str(self.amount) + '\n' + 
				'sender_key: ' + str(self.sender_key)	+ '\n' +
				'receiver_key: ' + str(self.receiver_key) + '\n' +
				'timestamp: ' + str(self.timestamp) )