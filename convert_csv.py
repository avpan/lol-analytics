import numpy as np
import os.path
from datetime import date, timedelta
import json

#checks for whether or not the game is a good match to analyze
#it checks to see if the game has 10 players (no afks)
#it checks if the game is a rank game
def checkGame(matchNum):
	x = 0
	hasAdcRed,hasSupRed,hasTopRed,hasMidRed,hasJungRed = 0,0,0,0,0
	hasAdcBlue,hasSupBlue,hasTopBlue,hasMidBlue,hasJungBlue = 0,0,0,0,0	
	teamRed, teamBlue = False,False #blue = teamid 100 and red is 200
	f = open("./data/bigdata/match_%d.json"%matchNum,"r")
	data = json.load(f)
	if data['queueType'] != 'TEAM_BUILDER_DRAFT_RANKED_5x5':
		game = False
	else:
		for item in data["participants"]:
			if item['stats']['winner']:
				x += 1
				if x == 5:
					game = True
				else:
					game = False
			#print item['timeline']['lane'], item['teamId']
			if item['timeline']['lane'] == 'TOP':
				if item['teamId'] == 100:
					hasTopBlue += 1
				elif item['teamId'] == 200:
					hasTopRed += 1
			elif item['timeline']['lane'] == 'MIDDLE':
				if item['teamId'] == 100:
					hasMidBlue += 1
				elif item['teamId'] == 200:
					hasMidRed += 1
			elif item['timeline']['lane'] == 'JUNGLE':
				if item['teamId'] == 100:
					hasJungBlue += 1
				elif item['teamId'] == 200:
					hasJungRed += 1
			elif item['timeline']['lane'] == 'BOTTOM':
				#print item['timeline']['role']
				if item['timeline']['role'] == 'DUO_CARRY':
					if item['teamId'] == 100:
						hasAdcBlue += 1
					elif item['teamId'] == 200:
						hasAdcRed += 1			
				elif item['timeline']['role'] == 'DUO_SUPPORT':
					if item['teamId'] == 100:
						hasSupBlue += 1
					elif item['teamId'] == 200:
						hasSupRed += 1
				
		#checks if the Blue and Red team have respective Top, Jungle, Mid, Adc, Sup meta
		if hasAdcBlue == 1 and hasSupBlue == 1 and hasTopBlue == 1 and hasMidBlue == 1 and hasJungBlue == 1:
			teamBlue = True
		if hasAdcRed == 1 and hasSupRed == 1 and hasTopRed == 1 and hasMidRed == 1 and hasJungRed == 1:
			teamRed = True
			
		#checks if game has 10 players, 5 winners (no afks), and has appropriate roles in meta			
		if len(data['participants']) == 10 and x == 5 and teamBlue and teamRed:
				game = True
				#print 'working'
				for item in data:
					if item == 'timeline':
						game = True
						break
					else:
						game = False
		else:
			game = False
	f.close()	
	return game
	
def sepIntoLanes(stats1,stats2,stats3,stats4,stats5):
	lanes = [stats1[0][3],stats2[0][3],stats3[0][3],stats4[0][3],stats5[0][3]]
	stats = [stats1,stats2,stats3,stats4,stats5]
	top,mid,jungle,adc,sup = [],[],[],[],[] 
	for i in range(0,5):
		if lanes[i] == 'TOP':
			top = stats[i]
		elif lanes[i] == 'MIDDLE':
			mid = stats[i]
		elif lanes[i] == 'JUNGLE':
			jungle = stats[i]
		elif lanes[i] == 'ADCARRY':
			adc = stats[i]
		elif lanes[i] == 'SUPPORT':
			sup = stats[i]
		
	return top,mid,jungle,adc,sup

		
def main(matchNum):
	f = open("./data/bigdata/match_%d.json"%matchNum,"r")
	data = json.load(f)
	
	player_info =[] #always 10 players per match to track ids I place their info in corresponding location
	#goes through player basic info
	for item in data['participantIdentities']:
		id = int(item['participantId'])
		name = item['player']['summonerName']
		player_info.append([id, name])
	

	#remove Losers of match and keep winners	
	winners=[]
	for item in data["participants"]:
		kills = item['stats']['kills']
		deaths = item['stats']['deaths']
		assists = item['stats']['assists']
		rank = item['highestAchievedSeasonTier']
		gold = item['stats']['goldEarned']
		cs = item['stats']['minionsKilled']
		if item['stats']['winner']:
			lane = item['timeline']['lane']
			if lane == 'BOTTOM':
				role = item['timeline']['role']
				if role == 'DUO_CARRY':
					lane = 'ADCARRY'
				elif role == 'DUO_SUPPORT':
					lane = 'SUPPORT'
			winners.append([item['participantId'],lane,kills,deaths,assists,rank,gold,cs])
		if not item['stats']['winner']:
			for row in player_info:	
				if row[0]==item['participantId']:
					player_info.remove(row)
					
	time = []
	stats1,stats2,stats3,stats4,stats5=[],[],[],[],[]
	for item in data['timeline']['frames']:
		time.append(item['timestamp']/1000/60) #time in minutes
		x=0
		ID = str(winners[x][0])
		lane = winners[x][1]
		gold=item['participantFrames'][ID]['totalGold']
		cs=item['participantFrames'][ID]['minionsKilled']
		jngcs = item['participantFrames'][ID]['jungleMinionsKilled']
		CS = cs + jngcs
		stats1.append([ID,gold,CS,lane])
		x=1
		ID = str(winners[x][0])
		lane = winners[x][1]
		gold=item['participantFrames'][ID]['totalGold']
		cs=item['participantFrames'][ID]['minionsKilled']
		jngcs = item['participantFrames'][ID]['jungleMinionsKilled']
		CS = cs + jngcs
		stats2.append([ID,gold,CS,lane])
		x=2
		ID = str(winners[x][0])
		lane = winners[x][1]
		gold=item['participantFrames'][ID]['totalGold']
		cs=item['participantFrames'][ID]['minionsKilled']
		jngcs = item['participantFrames'][ID]['jungleMinionsKilled']
		CS = cs + jngcs
		stats3.append([ID,gold,CS,lane])
		x=3
		ID = str(winners[x][0])
		lane = winners[x][1]
		gold=item['participantFrames'][ID]['totalGold']
		cs=item['participantFrames'][ID]['minionsKilled']
		jngcs = item['participantFrames'][ID]['jungleMinionsKilled']
		CS = cs + jngcs
		stats4.append([ID,gold,CS,lane])
		x=4
		ID = str(winners[x][0])
		lane = winners[x][1]
		gold=item['participantFrames'][ID]['totalGold']
		cs=item['participantFrames'][ID]['minionsKilled']
		jngcs = item['participantFrames'][ID]['jungleMinionsKilled']
		CS = cs + jngcs
		stats5.append([ID,gold,CS,lane])
			
	#for total winners regardless of lane
	#write to files for csv in format 'time' ''avgtotalGold' 'avgminionskilled'
	T = len(time)
	final_data = []
	for i in range(0,	T):
		avgGold = (stats1[i][1] + stats2[i][1] + stats3[i][1] + stats4[i][1] + stats5[i][1]) / float(5)
		avgCS =  (stats1[i][2] + stats2[i][2] + stats3[i][2] + stats4[i][2] + stats5[i][2]) / float(5)
		final_data.append([time[i],avgGold,avgCS,])
	
	#write to .csv file for winner/losers
	datafile = open('./data/csv_winner/data_match%d.csv'%matchNum,'w')
	for i in range(0,T):
		datafile.write('%d %f %f\n' % (final_data[i][0],final_data[i][1],final_data[i][2]))
	datafile.close()
		
	#splitting data into their separate lanes
	top, mid, jungle, adcarry, support = [],[],[],[],[] 
	top, mid, jungle, adcarry, support = sepIntoLanes(stats1,stats2,stats3,stats4,stats5)
			
	#write to .csv file for winner/losers for the different 5 lanes
	T = len(time)
	print len(time), len(jungle)
	#print len(top),len(mid),len(jungle),len(adcarry),len(support)
	df_top = open('./data/timeline_winner/top/data_match%d.csv'%matchNum,'w')
	df_mid = open('./data/timeline_winner/mid/data_match%d.csv'%matchNum,'w')
	df_jung = open('./data/timeline_winner/jungle/data_match%d.csv'%matchNum,'w')
	df_adc = open('./data/timeline_winner/adc/data_match%d.csv'%matchNum,'w')
	df_sup = open('./data/timeline_winner/support/data_match%d.csv'%matchNum,'w')
	
#write into .csv file in form time, gold, cs, 
	for i in range(0,T):
		df_top.write('%d %d %d\n' % (time[i],top[i][1],top[i][2]))
		df_mid.write('%d %d %d\n' % (time[i],mid[i][1],mid[i][2]))
		df_jung.write('%d %d %d\n' % (time[i],jungle[i][1],jungle[i][2]))
		df_adc.write('%d %d %d\n' % (time[i],adcarry[i][1],adcarry[i][2]))
		df_sup.write('%d %d %d\n' % (time[i],support[i][1],support[i][2]))
	
	df_top.close()
	df_mid.close()
	df_jung.close()
	df_adc.close()
	df_sup.close()
	
	#write end game stats such as rank, lane, kills, deaths, and assists
	endstats_df = open('./data/endstats_winner/data_match%d.csv'%matchNum,'w')
	
	for i in range(0,5):
		lane = str(winners[i][1])
		kills = winners[i][2]
		deaths = winners[i][3]
		assists = winners[i][4]
		rank = str(winners[i][5])
		gold = winners[i][6]
		cs = winners[i][7]
		endstats_df.write('%s %s %d %d %d %d %d\n' % (rank,lane,kills,deaths,assists,cs,gold))
	
	endstats_df.close()
	f.close()	
	
if __name__ == "__main__":
	N_matches = int(raw_input('How many matches you want converted?'))
	
	for n in range(5014,N_matches+1):
		filepath = "./data/bigdata/match_%d.json" % n
		if os.path.isfile(filepath):
			if checkGame(n):
				main(n)
		else:
			continue
