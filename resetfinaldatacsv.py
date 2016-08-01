#reset final_data.csv

finalpath1 = './data/FINAL/final_data_allwinners.csv'
finalpath2 = './data/FINAL/final_data_alllosers.csv'

fpadc1 = './data/FINAL/final_data_adcwinners.csv'
fptop1 = './data/FINAL/final_data_topwinners.csv'
fpmid1 = './data/FINAL/final_data_midwinners.csv'
fpjung1 = './data/FINAL/final_data_junglewinners.csv'
fpsup1 = './data/FINAL/final_data_supportwinners.csv'

fpadc2 = './data/FINAL/final_data_adclosers.csv'
fptop2 = './data/FINAL/final_data_toplosers.csv'
fpmid2 = './data/FINAL/final_data_midlosers.csv'
fpjung2 = './data/FINAL/final_data_junglelosers.csv'
fpsup2 = './data/FINAL/final_data_supportlosers.csv'

final1 = open(finalpath1,'w')
final2 = open(finalpath2,'w')

ftop1 = open(fptop1,'w')
fmid1 = open(fpmid1,'w')
fadc1 = open(fpadc1,'w')
fjng1 = open(fpjung1,'w')
fsup1 = open(fpsup1,'w')

ftop2 = open(fptop2,'w')
fmid2 = open(fpmid2,'w')
fadc2 = open(fpadc2,'w')
fjng2 = open(fpjung2,'w')
fsup2 = open(fpsup2,'w')

final1.write('%d %f %f %d' %(0,0,0,0))
final2.write('%d %f %f %d' %(0,0,0,0))

fadc1.write('%d %f %f %d' %(0,0,0,0))
ftop1.write('%d %f %f %d' %(0,0,0,0))
fmid1.write('%d %f %f %d' %(0,0,0,0))
fjng1.write('%d %f %f %d' %(0,0,0,0))
fsup1.write('%d %f %f %d' %(0,0,0,0))

fadc2.write('%d %f %f %d' %(0,0,0,0))
ftop2.write('%d %f %f %d' %(0,0,0,0))
fmid2.write('%d %f %f %d' %(0,0,0,0))
fjng2.write('%d %f %f %d' %(0,0,0,0))
fsup2.write('%d %f %f %d' %(0,0,0,0))

final1.close()
final2.close()

fadc1.close()
ftop1.close()
fmid1.close()
fjng1.close()
fsup1.close()

fadc2.close()
ftop2.close()
fmid2.close()
fjng2.close()
fsup2.close()