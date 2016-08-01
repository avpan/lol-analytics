import os.path
FILENUM = 10

def findAvg():
		plotdata = open('./data/FINAL/FINAL_allwinner.csv','w')
		f = open('./data/FINAL/final_data_allwinners.csv','r')
		data= f.read()
		finaldata = data.split('\n')
		finaldata.pop()
		final_data =[]
		for row in finaldata:
			final_data.append(row.split(' '))
		for i in range(len(final_data)):
			time = int(final_data[i][0])
			gold = float(final_data[i][1])
			cs = float(final_data[i][2])
			N = int(final_data[i][3])
			avg_Gold = gold/N
			avg_CS = cs/N
			if i == len(finaldata)-1:
				plotdata.write('%d %f %f' % (time,avg_Gold,avg_CS))
			else:
				plotdata.write('%d %f %f\n' % (time,avg_Gold,avg_CS))
		plotdata.close()
		
def main(num,cur_time):
		filepath = './data/csv_winner/data_match%d.csv' % num
		finalpath = './data/FINAL/final_data_allwinners.csv' #path for winners
		f=open(filepath,'r')
		final = open(finalpath,'r')
		data = f.read()		
		datafinal = final.read()
		datarows = data.split('\n')
		final_data = datafinal.split('\n')
		datarows.pop()
		final_data.pop()
		datalist = []
		finallist = []
		for row in datarows:
			datalist.append(row.split(' '))
		for row in final_data:
			finallist.append(row.split(' '))
		final.close()
		final = open(finalpath,'w')
		max_time = len(datalist)
		if max_time > cur_time:
			cur_time = max_time
			for i in range(0,cur_time):
				time = int(datalist[i][0])
				gold = float(datalist[i][1])
				cs = float(datalist[i][2])
				if i >= len(finallist):
					final.write('%d %f %f %d\n' % (time,gold,cs, 1))
				else:
					goldsum = float(finallist[i][1]) + gold #sumgold
					cssum = float(finallist[i][2]) + cs#sumcs
					finallist[i][3] = int(finallist[i][3]) + 1
					final.write('%d %f %f %d\n' % (time,goldsum,cssum,finallist[i][3]))
		else:
			for i in range(0,max_time):
				time = int(datalist[i][0])
				gold = float(datalist[i][1])
				cs = float(datalist[i][2])
				goldsum = float(finallist[i][1]) + gold
				cssum = float(finallist[i][2]) + cs
				finallist[i][3] = int(finallist[i][3]) + 1
				final.write('%d %f %f %d\n' % (time,goldsum,cssum,finallist[i][3]))
			for i in range(max_time,cur_time):
				time = int(finallist[i][0])
				gold = float(finallist[i][1])
				cs = float(finallist[i][2])
				final.write('%d %f %f %d\n' % (time,gold,cs,int(finallist[i][3])))
		final.close()	
		
		if num == FILENUM-1:
			findAvg()	
		f.close()
		return cur_time
	
if __name__ == "__main__":
	cur_time = 0
	for i in range(1,FILENUM):
		filepath = './data/csv_winner/data_match%d.csv' % i
		if os.path.isfile(filepath):
			cur_time = main(i,cur_time)
		else:
			continue