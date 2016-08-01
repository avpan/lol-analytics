import numpy as np
import warnings;
with warnings.catch_warnings():
    warnings.simplefilter("ignore");
    import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def main(lane):
	path = './data/FINAL/FINAL_%swinner.csv' % lane
	path2 = './data/FINAL/FINAL_%sloser.csv' % lane
	f = open(path, 'r')
	f2 = open(path2,'r')
	dataList = f.read()
	dataList2 = f2.read()
	data = dataList.split('\n')
	data2 = dataList2.split('\n')
	final_data, final_data2 = [],[]
	for el in data:
		final_data.append(el.split(' '))
	for el in data2:
		final_data2.append(el.split(' '))
	#extract each into their own list
	avgGold, avgCS, time = [],[],[]
	avgGold2, avgCS2,goldDif = [],[],[]
	for i in range(len(final_data)):
		time.append(int(final_data[i][0]))
		avgGold.append(float(final_data[i][1]))
		avgCS.append(float(final_data[i][2]))
	for i in range(len(final_data2)):
		avgGold2.append(float(final_data2[i][1]))
		avgCS2.append(float(final_data2[i][2]))
	
	for i in range(len(time)):
		goldDif.append(np.absolute(avgGold[i]-avgGold2[i]))
	
	goldDif = np.array(goldDif)		
	avgGold = np.array(avgGold)
	avgCS = np.array(avgCS)
	avgGold2 = np.array(avgGold2)
	avgCS2 = np.array(avgCS2)
	time = np.array(time)
	plt.figure(1)
	plt.plot(time, avgGold, 'k-',label='Match Winners')
	plt.plot(time, avgGold2,'r-', label='Match Losers')
	plt.title('Avg Gold Earned for %s' % lane)
	plt.xlabel('Match Time(min)')
	plt.ylabel('Average Gold Earned')
	plt.legend(bbox_to_anchor=(0.4,1),loc=0)
	plt.savefig('./data/Plots/AvgGold_Earned_%s.png' % lane)
	plt.figure(2)
	plt.plot(time,goldDif, 'k-')
	plt.title('Gold Difference between Losers/Winners for %s' % lane)
	plt.xlabel('Game Time(min)')
	plt.ylabel('Average Gold Earned Difference')
	plt.savefig('./data/Plots/AvgGoldEarnedDiff_%s' % lane)
	#plt.plot(time, avgCS, 'ko')
	#plt.show()
	
if __name__ == "__main__":
	lane = raw_input('What lane you wish to plot? (choose: adc, top, mid, jungle, support)')
	main(lane)