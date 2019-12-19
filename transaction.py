import hashlib as hl

class Transaction():

	def __init__(self, amount, senderKey, receiverKey, timestamp):
		self.amount = amount
		self.senderKey = senderKey
		self.receiverKey = receiverKey
		self.timestamp = timestamp
		h = hl.sha256()
		h.update(
	        str(self.amount).encode('utf-8') +
	        str(self.senderKey).encode('utf-8') +
	        str(self.receiverKey).encode('utf-8') +
	        str(self.timestamp).encode('utf-8')
		)
		self.hash_value = h.hexdigest()

	def __str__(self):
		return( 'Amount: ' + str(self.amount) + '\n' +
				'senderKey: ' + str(self.senderKey) + '\n' +
				'receiverKey: ' + str(self.receiverKey) + '\n' +
				'timestamp: ' + str(self.timestamp) )