plotdata = open('./data/FINAL/FINAL.csv','w')
f = open('./data/FINAL/final_data.csv','r')
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
	print time,gold,cs

plotdata.close()
f.close()