class Transaction():

	def __init__(self, amount, senderKey, receiverKey, timestamp):
		self.amount = amount
		self.senderKey = senderKey
		self.receiverKey = receiverKey
		self.timestamp = timestamp
		
	def __str__(self):
		return( 'Amount: ' + str(self.amount) + '\n' +
				'senderKey: ' + str(self.senderKey) + '\n' +
				'receiverKey: ' + str(self.receiverKey) + '\n' +
				'timestamp: ' + str(self.timestamp) ) 
		