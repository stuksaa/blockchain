from block import Block

class BlockChain:

	sofRed	= 10
	maxiter = 2**32
	maxnum 	= 2**(256-sofRed)

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
		for i in range(self.maxiter):
			if int(block.hashgen(), 16)<=self.maxnum:
				self.add(block)
				break
			else:
				block.nofAttempt += 1
