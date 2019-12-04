import numpy as np 
import datetime as dt 
import hashlib as hl 
from block import Block 
from blockchain import BlockChain 

blockchain = BlockChain()

blockchain.mine(Block('A->B:10'))
blockchain.mine(Block('B->A:5'))
blockchain.mine(Block('B->C:15'))
blockchain.mine(Block('D->A:6'))
blockchain.mine(Block('A->B:10'))
blockchain.mine(Block('C->D:5'))
blockchain.mine(Block('B->D:20'))
blockchain.mine(Block('C->A:7'))

temp = blockchain.head
while temp.next_block is not None:
	print(temp,end='\n\n')
	temp = temp.next_block
