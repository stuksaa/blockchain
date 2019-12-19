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
import copy
import random

miner_ids = ['M-00','M-01','M-02','M-03','M-04']

blockchain = BlockChain()

transactions = []
transactions.append(Transaction(10,'A','B',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(20,'A','D',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(30,'C','B',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(20,'B','C',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(10,'A','B',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(40,'D','A',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(20,'A','B',dt.datetime.now()))
time.sleep(random.random())
transactions.append(Transaction(30,'C','D',dt.datetime.now()))
transactions.reverse()

possible_chains = []
possible_chains.append(blockchain)

miners = []

queueLock = threading.Lock()

for idx, e in enumerate(miner_ids):
	miners.append(Miner(e,copy.deepcopy(blockchain),copy.deepcopy(transactions),possible_chains,queueLock))
	miners[idx].start()


time.sleep(100)

Miner.exitflag = 0

time.sleep(3)

print(miners[0].blockchain.printChain())

