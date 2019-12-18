import numpy as np 
import datetime as dt 
import hashlib as hl 
from block import Block 
from blockchain import BlockChain 
from transaction import Transaction
import time
from miner import Miner
from timestampserver import TimeStampServer
import queue
import threading

miner_ids = ['M-00','M-01','M-02','M-03','M-04']

blockchain = BlockChain()

transactions = queue.Queue(100)
miners = []

queueLock = threading.Lock()

for idx, e in enumerate(miner_ids):
	miners.append(Miner(e,blockchain,transactions,queueLock))
	miners[idx].start()

transactions.put(Transaction(10,'A','B',dt.datetime.now()))
transactions.put(Transaction(20,'A','D',dt.datetime.now()))
transactions.put(Transaction(30,'C','B',dt.datetime.now()))
transactions.put(Transaction(20,'B','C',dt.datetime.now()))
transactions.put(Transaction(10,'A','B',dt.datetime.now()))
transactions.put(Transaction(40,'D','A',dt.datetime.now()))
transactions.put(Transaction(20,'A','B',dt.datetime.now()))
transactions.put(Transaction(30,'C','D',dt.datetime.now()))

time.sleep(10)

while not transactions.empty():
	pass

Miner.exitflag = 0

time.sleep(10)

for i in blockchain.items:
	print(str(i))

