import numpy as np
from datetime import date, timedelta
import json

def main():
	f = open("./data/match.json","r")
	data = f.read().split('\n')
	
	N = len(data)
	for i in range (1,N):
		k = open('./data/bigdata/match_%d.json' % i, 'w')
		k.write(data[i])
		k.close()
	f.close()	
	
if __name__ == "__main__":
	main()
