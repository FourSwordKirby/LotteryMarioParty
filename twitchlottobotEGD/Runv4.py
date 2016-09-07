import string
import csv
import time
import operator
from Readv3 import getUser, getMessage, getChannelname, getBannedUser, getBannedChannelname
from Readv3 import getslowmode, getr9k, getsubmode, getroomstatechannelname
from Readv3 import getOwner, getTurbo, getSub, getMod
from Socketv2 import openSocket, sendMessage
from Settingsv2 import HOST, PORT, PASS, IDENT
from datetime import datetime

from Tkinter import *
import os
import threading

# Actually joins the rooms
s = openSocket()

#dictionary for user's and the funds they have
userDict = dict()

#dictionary for active tickets
ticketDict1 = dict()
ticketDict2 = dict()
ticketDict3 = dict()
ticketDict4 = dict()
winnings = 30;

#check the ticket stash for winners
def checkTickets():
	threading.Timer(0.2, checkTickets).start()
	global winnings;

	allTickets = open("C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\MarioPartyExerpimentalGameDesign\currentNumbers.txt")
	for ticketIdx, ticket in enumerate(allTickets) :
		ticket = ticket.rstrip()
		if ticketIdx == 0 and ticketDict1.has_key(ticket):
			for user in ticketDict1[ticket]:
				sendMessage(s, "@" + user + " Congratulations! You have gained " + str(winnings) + " tickets", 0);
				userDict[user] += winnings;
			ticketDict1[ticket] = []
		if ticketIdx == 1 and ticketDict2.has_key(ticket):
			for user in ticketDict2[ticket]:
				sendMessage(s, "@" + user + " Congratulations! You have gained " + str(winnings) + " tickets", 0);
			ticketDict2[ticket] = []
		if ticketIdx == 2 and ticketDict3.has_key(ticket):
			for user in ticketDict3[ticket]:
				sendMessage(s, "@" + user + " Congratulations! You have gained " + str(winnings) + " tickets", 0);
			ticketDict3[ticket] = []
		if ticketIdx == 3 and ticketDict4.has_key(ticket):
			for user in ticketDict4[ticket]:
				sendMessage(s, "@" + user + " Congratulations! You have gained " + str(winnings) + " tickets", 0);
			ticketDict4[ticket] = []

	allTickets.close()

checkTickets()


def updateMessage():
	threading.Timer(300, checkTickets).start()
	response = "Welcome to the Mario Party Lottery!! Support your favorite character by purchasing a ticket. Type !help for more info"
	response = "This stream does NOT encourage players to gamble recklessly"
	sendMessage(s, response, 0);

checkTickets()


### joinRoom(s)
readbuffer = ""


id = 0

# Sets how long the scraper will run for (in seconds)
starttime = time.time() + 100000

# Runs until time is up
while time.time() < starttime:
		# Pulls a chunk off the buffer, puts it in "temp"
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()


		# Iterates through the chunk
		for line in temp:
			print line
			id = id + 1
		
			# Parses lines and writes them to the file
			if "PRIVMSG" in line:
				try:

					# Gets user, message, and channel from a line
					user = getUser(line)
					message = getMessage(line)
					channelname = getChannelname(line)
					owner = getOwner(line)
					mod = getMod(line)
					sub = getSub(line)
					turbo = getTurbo(line)
		
					if owner == 1:
						mod = 1
		
					# Writes Message ID, channel, user, date/time, and cleaned message to file
					with open('outputlog.csv', 'ab') as fp:
						ab = csv.writer(fp, delimiter=',')
						data = [id, channelname, user, datetime.now(), message.strip(), owner, mod, sub, turbo];
						ab.writerow(data)
					if(message.startswith("!register")):
						if(not userDict.has_key(user)):
							userDict[user] = 10;
							response = user + " has registered for the Mario Party Lottery!!"
							sendMessage(s, response, 0);

					if(message.startswith("!help")):
						response = "@" + user + " To buy a ticket, type in !ticket followed by the player, followed by the appropriate number of numbers. "
						response += "For example, [!ticket Mario 12 34 56 78 90 69] will give you a ticket for Mario. "
						response += "You get 10 tickets a day. Win drawings to earn more."
						sendMessage(s, response, 0);

					if(message.startswith("!ticket")):
						if(not userDict.has_key(user)):
							sendMessage(s, "@" + user + " Please register before buying tickets", 0);
						else:
							if (len(message.split(" ")) < 3):
								sendMessage(s, "@" + user + " Please format your request properly, type !help", 0);
								continue

							team = message.split(" ")[1];
							ticketNums = message.split(" ")[2:];
							ticket = ""
							for num in ticketNums:
								ticket += num.rstrip() + " "
							ticket = ticket.rstrip();
							
							if(len(filter(lambda x: not x.rstrip().isdigit(), ticketNums)) != 0):
								response = "@" + user + " the numbers you have entered is not valid"
								sendMessage(s, response, 0);
								continue

							if(team == "Mario"):
								if(not ticketDict1.has_key(ticket)):
									ticketDict1[ticket] = []
								ticketDict1[ticket].append(user);
							elif(team == "Peach"):
								if(not ticketDict2.has_key(ticket)):
									ticketDict2[ticket] = []
								ticketDict2[ticket].append(user);
							elif(team == "Boo"):
								if(not ticketDict3.has_key(ticket)):
									ticketDict3[ticket] = []
								ticketDict3[ticket].append(user);
							elif(team == "Yoshi"):
								if(not ticketDict4.has_key(ticket)):
									ticketDict4[ticket] = []
								ticketDict4[ticket].append(user);
							else:
								response = "@" + user + " the team you entered is not playing right now"
								sendMessage(s, response, 0);
								continue
							
							if(userDict[user] <= 0):
								response = "@" + user + " you lack the funds to purchase tickets"
								sendMessage(s, response, 0);
								continue
							userDict[user] -= 1

							print("here")
							response = "@" + user + " You have just purchased ticket [" + ticket + "] for team " + team
							sendMessage(s, response, 0);

				# Survives if there's a message problem
				except Exception as e:
					print "MESSAGE PROBLEM"
					print line
					print e
		
			# Responds to PINGs from twitch so it doesn't get disconnected
			elif "PING" in line:
				try:
					separate = line.split(":", 2)
					s.send("PONG %s\r\n" % separate[1])
					print ("PONG %s\r\n" % separate[1])
					print "I PONGED BACK"
				
				# Survives if there's a ping problem
				except:
					print "PING problem PING problem PING problem"
					print line
		
			# Parses ban messages and writes them to the file
			elif "CLEARCHAT" in line:
				try:
			
					# Gets banned user's name and channel name from a line
					user = getBannedUser(line)
					channelname = getBannedChannelname(line)
				
					# Writes Message ID, channel, user, date/time, and an indicator that it was a ban message.
					#	I use "oghma.ban" because the bot's name is oghma, and I figure it's not a phrase that's
					#	likely to show up in a message so it's easy to search for.
					with open('outputlog.csv', 'ab') as fp:
						ab = csv.writer(fp, delimiter=',');
						data = [id, channelname, user, datetime.now(), "oghma.ban"];
						ab.writerow(data);
			
				# Survives if there's a ban message problem
				except Exception as e:
					print "BAN PROBLEM"
					print line
					print e
				