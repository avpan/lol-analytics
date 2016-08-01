import numpy as np
from datetime import date, timedelta
import json


def checkGame(matchNum):
	f = open("./data/bigdata/match_%d.json"%matchNum,"r")
	data = json.load(f)
	if data['queueType'] != 'TEAM_BUILDER_DRAFT_RANKED_5x5':
		game = False
	else:
		if len(data['participants']) == 10:
			#print len(data['participants'])
			game = True
		else:
			game = False
	f.close()	
	return game

def checkItems(matchNum):
	
	f = open("./data/bigdata/match_%d.json"%matchNum,"r")
	data = json.load(f)
	winners=[]
	for item in data["participants"]:
		kills = item['stats']['kills']
		deaths = item['stats']['deaths']
		assists = item['stats']['assists']
		rank = item['highestAchievedSeasonTier']
		if item['stats']['winner']:
			lane = item['timeline']['lane']
			if lane == 'JUNGLE':
				print data['timeline']['frames']#[str(item['participantId'])]
			if lane == 'BOTTOM':
				role = item['timeline']['role']
				if role == 'DUO_CARRY':
					lane = 'ADCARRY'
				elif role == 'DUO_SUPPORT':
					lane = 'SUPPORT'
			winners.append([item['participantId'],lane,kills,deaths,assists,rank])
		
	
		
def main(matchNum):
	f = open("./data/bigdata/match_%d.json"%matchNum,"r")
	data = json.load(f)
	
	player_info =[] #always 10 players per match to track ids I place their info in corresponding location
	#goes through player basic info
	for item in data['participantIdentities']:
		id = int(item['participantId'])
		name = item['player']['summonerName']
		player_info.append([id, name])
		#print player_info
	
	#remove Losers of match and keep winners	
	winners=[]
	for item in data["participants"]:
		if item['stats']['winner']:
			winners.append(item['participantId'])
		if not item['stats']['winner']:
			for row in player_info:	
				if row[0]==item['participantId']:
					player_info.remove(row)
					
	#print player_info
	time = []
	stats1,stats2,stats3,stats4,stats5=[],[],[],[],[]
	#print len(winners)
	for item in data['timeline']['frames']:
		time.append(item['timestamp']/1000/60) #time in minutes
		x=0
		g1=item['participantFrames'][str(winners[x][0])]['totalGold']
		cs1=item['participantFrames'][str(winners[x][0])]['minionsKilled']
		stats1.append([winners[x[0]],g1,cs1])
		x=1
		g2=item['participantFrames'][str(winners[x][0])]['totalGold']
		cs2=item['participantFrames'][str(winners[x][0])]['minionsKilled']
		stats2.append([winners[x][0],g2,cs2])
		x=2
		g3=item['participantFrames'][str(winners[x][0])]['totalGold']
		cs3=item['participantFrames'][str(winners[x][0])]['minionsKilled']
		stats3.append([winners[x][0],g3,cs3])
		x=3
		g4=item['participantFrames'][str(winners[x][0])]['totalGold']
		cs4=item['participantFrames'][str(winners[x][0])]['minionsKilled']
		stats4.append([winners[x][0],g4,cs4])
		x=4
		g5=item['participantFrames'][str(winners[x][0])]['totalGold']
		cs5=item['participantFrames'][str(winners[x][0])]['minionsKilled']
		stats5.append([winners[x][0],g5,cs5])

	
if __name__ == "__main__":
	n = 1
	checkItems(n)
	#main(n)
	#if checkGame(n):
		#main(n)
		