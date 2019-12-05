import hashlib as hl 
import datetime as dt 
import time

h = hl.sha256()

for i in range(10):
	notHash = True
	while notHash:
		tstamp = dt.datetime.now()
		h.update(str(tstamp).encode('utf-8'))
		hashgen = h.hexdigest()
		if hashgen[0:5] == '00000':
			notHash = False 
	
	print(hashgen)