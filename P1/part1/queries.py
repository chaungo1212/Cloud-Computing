from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint
from bson import ObjectId 

collection = connectMongo()

##### FIND ALL ENTRIES IN THE DATABASE #####
# Assuming RQ0 is the query to find all entries in the database
RQ0 = collection.find()
for data in RQ0:
	pprint.pprint(data)
	print('')

######## FIND ENTRIES WITH CONDITION #######
######## collection.find(CONDITION) #######
######## E.g., collection.find({"Name" : "Alice"}) #######

print("WQ2\n")	
######## READ JSON FILE #######
with open('user1001-new.json') as json_data:
    d = json.load(json_data)
print('')
print("Load json file: user1001-new.json, and parse json")
print("uid: " + str(d["uid"]))
print("height: " + d["height"])
print("weight: " + d["weight"])
print("tags: " + d["tags"][0])

print('')
print('New table:')
table = collection.find()
for data in table:
	pprint.pprint(data)
	print('')

if collection.find({"uid":d["uid"]}).count() > 0:
	collection.update({"uid":d["uid"]}, {"$set":{"height":d["height"], "weight":d["weight"], "tags":d["tags"]}})
	print("Update uid:" + str(d["uid"]) + " successfully")
	
print('')

print('New table:')
WQ2 = collection.find().sort("uid", pymongo.ASCENDING)
for data in WQ2:
	pprint.pprint(data)
	print('')
print("RQ1:\n")	
RQ1 = collection.find().count()
print ( str(RQ1)+" employees whose data is in the AggieFit database")

print('')
print("RQ2: \n")
nRQ2 = collection.find({"tags":"active"}).count()
print (str(nRQ2) + " employees are active")
RQ2_table = collection.find({"tags":"active"})
for data in RQ2_table:
	pprint.pprint(data)

print('')
print("RQ3:\n")
RQ3_table = collection.find()
for data in RQ3_table:
	#pprint.pprint(data["goal"]["activityGoal"])
	if data["goal"]["activityGoal"][0:2] != "NA":
		if int((data["goal"]["activityGoal"][0:2])) > 60:
			#print(data["uid"])
			#print(data["goal"]["activityGoal"][0:2])
			pprint.pprint(data)
			

print('')
print("RQ4\n")
RQ4_table = collection.find().sort("uid", pymongo.ASCENDING)
for data in RQ4_table:
	total = 0
	if "activityDuration" in data.keys():	
		for times in data["activityDuration"]:
			total = total + times
	print(str(data["uid"]) + "'s total activityDuration: " + str(total))
#RQ3 = collection.find({"goal.activityGoal":"30"}).count()
#print RQ3
######## UPDATE ENTRIES WITH CONDITION ########
######## collection.update_one(CONDITION, _update_) #######
######## collection.update_many(CONDITION, _update_)
######## E.g., collection.find({"Name" : "Alice"}, {"$inc" : {"age" : 1} })

######## DELETE ENTRIES WITH CONDITION ########
######## collection.delete_one(CONDITION) #######
######## collection.delete_many(CONDITION)
######## E.g., collection.find({"Name" : "Alice"})

######## AGGREGATE ENTRIES WITH PIPELINE ########
######## collection.aggregate(PIPELINE) ########

