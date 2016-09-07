import socket
import string
import time
from Settingsv2 import HOST, PORT, PASS, IDENT, CHANNELLIST
#from getchannellist import getchannellist


# The open socket function, which actually does the connecting
def openSocket():

	#CHANNELLIST = getchannellist()
	
	# Connects to host and port established in the settings file
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + IDENT + "\r\n")
	
	# Sends request to see meta-messages including bans
	s.send("CAP REQ :twitch.tv/commands" + "\r\n")
	s.send("CAP REQ :twitch.tv/tags" + "\r\n")
	
	# Joins all the channels in the list
	for c in CHANNELLIST:
		s.send("JOIN #" + c + "\r\n")
		print("JOIN #" + c + "\r\n")
		time.sleep(0.01)
	return s

# Defines the message sending function; not currently used in this script	
def sendMessage(s, message, channelNumber):
	messageTemp = "PRIVMSG #" + CHANNELLIST[channelNumber] + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)