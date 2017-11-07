from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint
import signal
import sys
from bson import ObjectId 

def printdict(dict):
	print("{"),
	i = 0
	for key, value in dict.iteritems():
		i = i + 1
		if(str(key) != "_id"):
			if i < len(dict):
				print("'"+str(key)+"':'"+str(value)+", "),
			else:
				print("'"+str(key)+"':'"+str(value)),
	print("}")

db = connectMongo()
#db.create_collection("health_quotes")
#db.create_collection("fit_chat")
allcollectionNames = db.collection_names()
#db["health_quotes"].remove()
#db["fit_chat"].remove()
#for collectionName in allcollectionNames:
#	print(collectionName)
selectCollection = False
listenStart = False
previndex = 0
while True:
	try:
		if listenStart == True:
			while True:
				if previndex != msgboard.count():
					msglist = msgboard.find()
					for i in range(previndex, msgboard.count()):
						print(msglist[i])
					previndex = msgboard.count()

		print("Enter command:"),
		command = raw_input()

		if command.find('select') != -1:
			index_space = command.find(' ')
			if index_space != -1:
				msgboardName = command[index_space+1:len(command)]
				if msgboardName in allcollectionNames:
					print(command.split())
					msgboard = db[msgboardName] # Switch collection to msgboard
					selectCollection = True
				else:
					print(msgboardName + " is not in this database")
			else:
				print(" No board is selected\n")
					
		elif command.find('read') != -1:
			if selectCollection == False:
				print("Has not select the message board")
			else:
				print(command.split())
				if msgboard.count() == 0:
					print("None")
				else:
					for msg in msgboard.find():
						#msglist = dictTolist(msg)
						#print(msglist)
						printdict(msg)
		elif command.find('write') != -1:
			if selectCollection == False:
				print("Has not select the message board")
			else:
				index_space = command.find(' ')
				if index_space != -1:
					msg = command[index_space+1:len(command)]
					print(command.split())
					msgboard.insert({'pattern':None, 'type':'message', 'channel':msgboardName, 'data':msg})
				else:
					print("No message to write into the board")
					
		elif command.find('listen') != -1:
			if selectCollection == False:
				print("Has not select the message board")
			else:
				listenStart = True
				print(command.split())
				previndex = msgboard.count()
				print("Sub")
				print("{'pattern':None, 'type':'subscribe', 'channel':'" + msgboardName + "', 'data':1L}")
				
		elif command.find('stop') !=-1:
			print(command.split())
			sys.exit(1);
		else:
			print("Command invalid")
			print("Example: select health_quotes, or read, or write I'm here, or listen, or stop")
	except KeyboardInterrupt:
		listenStart = False
	