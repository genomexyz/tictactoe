#!/usr/bin/python3

import numpy as np
import random
import pickle
from flask import Flask
from flask_cors import CORS

#setting
#qtable = {}
lrate = 0.2
wincondition = [[1,2,3], [4,5,6], [7,8,9],
[1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
winreward = 10.
drawreward = 5.
losereward = -10.
#epsilon = 1.0
decay_epsilon = 0.000005
saved_stat = 'qtable.h5'

def montecarlocalc(state, action, reward):
	qold = getQ(state, action)
	qnew = qold + lrate * (reward - qold)
	qtable[(state, action)] = qnew
	return qnew

def domove(hismovestr, possmove):
	global epsilon
	chance = random.uniform(0,1)
	qpossmove = np.zeros((len(possmove)))
	for i in range(len(qpossmove)):
		qpossmove[i] = getQ(hismovestr, possmove[i])
	if chance < epsilon:
		pickmove = random.choice(possmove)
	else:
		pickmove = possmove[np.argmax(qpossmove)]
	epsilon -=  decay_epsilon
	return pickmove

def getQ(state, action): #get Q states
	if(qtable.get((state,action))) is None:
		qtable[(state,action)] = 0.0
	return qtable.get((state,action))


def saveQtable(file_name):  #save table
	with open(file_name, 'wb') as handle:
		pickle.dump([qtable, epsilon], handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadQtable(file_name): #load table
	try:
		bukadata = open(file_name, 'rb')
		qtable_read, epsilon_read = pickle.load(bukadata)
	except IOError:
		qtable_read = {}
		epsilon_read = 1.0
	return qtable_read, epsilon_read
		

def possible_moves(position):
	move = []
	for i in range(1,10):
		if not i in position:
			move.append(i)
	return np.asarray(move)

def checkwinning(bidak):
	win = False
	for i in range(len(wincondition)):
		if set(wincondition[i]).issubset(bidak):
			win = True
			break
	return win

def rewardandpunishment(hismovestr, comhismove, reward):
	movelen = len(comhismove)
	if movelen == 2:
		rewardarray = np.asarray([reward*0.1, reward*0.9,])
	elif movelen == 3:
		rewardarray = np.asarray([reward*0.2, reward*0.3, reward*0.5])
	elif movelen == 4:
		rewardarray = np.asarray([reward*0.2, reward*0.3, reward*0.4, reward*0.1])
	for i in range(len(rewardarray)):
		state = hismovestr[:1+i*2]
		action = comhismove[i]
		montecarlocalc(state, action, rewardarray[i])
	return 1

def checkreq(position):
	validitas = True
	for i in range(len(position)):
		if position[i] == '0':
			validitas = False
			break
	return validitas

#print(getQ('1','2'))
#print(possible_moves(board))

##############
#main program#
##############

qtable, epsilon = loadQtable(saved_stat)

app = Flask(__name__)
CORS(app)

@app.route('/ryan/think/<position>')
def process(position):
	try:
		check = int(position)
	except ValueError:
		return 'INVALID REQUEST'
	if (checkreq(position)):
		hismovestr = position
		playerhismove = []
		comhismove = []
		hismove = []
		for i in range(len(hismovestr)):
			if i % 2:
				comhismove.append(int(hismovestr[i]))
			else:
				playerhismove.append(int(hismovestr[i]))
			hismove.append(int(hismovestr[i]))
		playerhismove = np.asarray(playerhismove)
		comhismove = np.asarray(comhismove)
		hismove = np.asarray(hismove)
	
		#check winning
		comwin = checkwinning(comhismove)
		fixmove = ""
		state = ""
		kembalian = ""
		if not comwin:
			#if player win, we punish the bot
			playerwin = checkwinning(playerhismove)
			if playerwin:
				rewardandpunishment(hismovestr, comhismove, losereward)
				state = 'win'
				fixmove = '0'
				saveQtable(saved_stat)
			if not(playerwin) and len(hismovestr) < 9:
				commitmove = domove(hismovestr, possible_moves(hismove))
				comhismove2nd = []
				for i in range(len(comhismove)):
					comhismove2nd.append(comhismove[i])
				comhismove2nd.append(commitmove)
				comhismove2nd = np.asarray(comhismove2nd)
				comwin = checkwinning(comhismove2nd)
				if comwin:
					rewardandpunishment(hismovestr+str(commitmove), comhismove2nd, winreward)
					state = 'lose'
					fixmove = str(commitmove)
					saveQtable(saved_stat)
				else:
					state = 'ongame'
					fixmove = str(commitmove)
			elif not(playerwin) and len(hismovestr) == 9:
				rewardandpunishment(hismovestr, comhismove, drawreward)
				state = 'draw'
				fimove = '0'
				saveQtable(saved_stat)
				#print(qtable)
			kembalian = fixmove+','+state
		#dont waste my time, me already win!
		else:
			kembalian = "ME ALREADY WIN BROTHER!"
	else:
		kembalian = 'INVALID REQUEST'
	return kembalian
