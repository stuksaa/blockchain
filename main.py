import copy
import threading
from miner import Miner
from timestampserver import TimeStampServer
from blockchain import BlockChain 

blockchain 		= BlockChain()
queue_lock 		= threading.Lock()

miner_names		= ['M-00','M-01','M-02','M-03','M-04']
transactions 	= []
possible_chains = []
miners 			= []

timestampserver = TimeStampServer(transactions, queue_lock)

possible_chains.append(blockchain)

for idx, e in enumerate(miner_names):
	miners.append(Miner(e, copy.deepcopy(blockchain), transactions, possible_chains, queue_lock))
	miners[idx].start()

timestampserver.start()

for miner in miners:
	miner.join()

print()
print('The following blockchain has been constructed:')
miners[0].blockchain.print_chain()