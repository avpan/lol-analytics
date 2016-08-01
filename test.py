import numpy as np
from datetime import date, timedelta
import json

def main():
	f = open("./data/match.json","r")
	data = json.load(f)
	f.close()	
	
if __name__ == "__main__":
	main()
