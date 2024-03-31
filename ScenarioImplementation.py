import json
import datetime
import graphlib
import time

requestObj = open("request.json", "r")
requestData = json.load(requestObj)
requestDataCopy = requestData

activityObj = open("activity.json", "r")
activityData = json.load(activityObj)
activityDataCopy = activityData

objectObj = open("object.json", "r")
objectData = json.load(objectObj)
objectDataCopy = objectData

operationObj = open("operation.json", "r")
operationData = json.load(operationObj)
operationDataCopy = operationData

activityDependenciesObj = open("activityDependencies.json", "r")
activityDependenciesData = json.load(activityDependenciesObj)
activityDependenciesDataCopy = activityDependenciesData


def getRequests(): #returns requests
    requestList = requestDataCopy["request"]
    print(requestList)
    return requestList
def getObject(activity): #returns objects
    object = objectDataCopy["activity"][activity]["object"]
    return object
def getOperation(activity, object): #returns operations
    operation = operationDataCopy["activity"][activity]["object"][object]["operation"]
    return operation
def getCurrentState(activity, activityDataCopy): #returns current state of an activity
    #activityDataCopy = activityData
    currentState = activityDataCopy["activity"][activity]["current"]["state"]
    return currentState
def preD(preDAList, activityDataCopy): #check if all pre-dependent activities are in their desired states or not
    activityObj = open("activity.json", "r")
    activityData = json.load(activityObj)
    activityDataCopy = activityData
    for da in preDAList:
        dependentActivity = da["activity"]
        daCurrentState = getCurrentState(dependentActivity, activityDataCopy)
        print("######" + daCurrentState)
        daDesiredState = da["desired"]["state"]
        print("######" + daDesiredState)
        if daCurrentState != daDesiredState:
            return False
    return True
def onD(onDAList, activityDataCopy): #check if all ongoing-dependent activities are in their desired states or not
    activityObj = open("activity.json", "r")
    activityData = json.load(activityObj)
    activityDataCopy = activityData
    for da in onDAList:
        dependentActivity = da["activity"]
        daCurrentState = getCurrentState(dependentActivity, activityDataCopy)
        print("######" + daCurrentState)
        daDesiredState = da["desired"]["state"]
        print("######" + daDesiredState)
        if daCurrentState != daDesiredState:
            return False
    return True
def postD(postDAList, activityDataCopy): #check if all post-dependent activities are in their desired states or not
    activityObj = open("activity.json", "r")
    activityData = json.load(activityObj)
    activityDataCopy = activityData
    for da in postDAList:
        dependentActivity = da["activity"]
        daCurrentState = getCurrentState(dependentActivity, activityDataCopy)
        print("######" + daCurrentState)
        daDesiredState = da["desired"]["state"]
        print("######" + daDesiredState)
        if daCurrentState != daDesiredState:
            return False
    return True

def preUpdate(preDAList, activityDataCopy): #update the states of pre-dependent activities
    numberOfDependencies = 0
    for da in preDAList:
        dependentActivity = da["activity"]
        daCurrentState = getCurrentState(dependentActivity, activityDataCopy)
        print("######" + daCurrentState)
        daDesiredState = da["desired"]["state"]
        print("######" + daDesiredState)
        if daCurrentState != daDesiredState and activityDataCopy["activity"][dependentActivity]["immutable"] == "False":
            activityDataCopy["activity"][dependentActivity]["current"]["state"] = daDesiredState
            with open("activity.json", "w") as outfile:
                json.dump(activityDataCopy, outfile, indent=4)
                outfile.close()
            numberOfDependencies = numberOfDependencies + 1
    return numberOfDependencies
def onUpdate(onDAList, activityDataCopy): #update the states of ongoing-dependent activities
    numberOfDependencies = 0
    #activityDataCopy = activityData
    for da in onDAList:
        dependentActivity = da["activity"]
        daCurrentState = getCurrentState(dependentActivity, activityDataCopy)
        print("######" + daCurrentState)
        daDesiredState = da["desired"]["state"]
        print("######" + daDesiredState)
        if daCurrentState != daDesiredState and activityDataCopy["activity"][dependentActivity]["immutable"] == "False":
            activityDataCopy["activity"][dependentActivity]["current"]["state"] = daDesiredState
            with open("activity.json", "w") as outfile:
                json.dump(activityDataCopy, outfile, indent=4)
                outfile.close()
            numberOfDependencies = numberOfDependencies + 1
    return numberOfDependencies
def postUpdate(postDAList, activityDataCopy): #update the states of post-dependent activities
    numberOfDependencies = 0
    #activityDataCopy = activityData
    for da in postDAList:
        dependentActivity = da["activity"]
        daCurrentState = getCurrentState(dependentActivity, activityDataCopy)
        print("######" + daCurrentState)
        daDesiredState = da["desired"]["state"]
        print("######" + daDesiredState)
        if daCurrentState != daDesiredState and activityDataCopy["activity"][dependentActivity]["immutable"] == "False":
            activityDataCopy["activity"][dependentActivity]["current"]["state"] = daDesiredState
            with open("activity.json", "w") as outfile:
                json.dump(activityDataCopy, outfile, indent=4)
                outfile.close()
            numberOfDependencies = numberOfDependencies + 1
    return numberOfDependencies
def initialRequestProcess(requestList, numberOfRequests, activityDataCopy): #process the requests for initial phase
    numberOfDependencies = 0
    dependencyCheck = 0
    for request in range((int)(numberOfRequests)):
        currentRequest = requestList[request]
        requestedActivity = currentRequest["activity"]
        currentStateofRequestedActivity = getCurrentState(requestedActivity, activityDataCopy)
        object = getObject(requestedActivity)
        operation = getOperation(requestedActivity, object)

        ##calculate time from here

        activityDependenciesDataCopy = activityDependenciesData
        if "preDA" in activityDependenciesDataCopy["dependency"]["activity"][requestedActivity]:
            preDAList = activityDependenciesDataCopy["dependency"]["activity"][requestedActivity]["preDA"]
            dependencyCheck = dependencyCheck + len(preDAList)
            preD_result = preD(preDAList, activityDataCopy)
            #print("1:" , preD_result)
            if not preD_result:
                #output = preUpdate(preDAList, activityDataCopy)
                #activityDataCopy = output[0]
                numberOfDependencies = numberOfDependencies + preUpdate(preDAList, activityDataCopy)
                #print(activityDataCopy)
        activityDataCopy["activity"][requestedActivity]["current"]["state"] = "running"
        with open("activity.json", "w") as outfile:
            json.dump(activityDataCopy, outfile, indent=4)
            outfile.close()
        preD_result = preD(preDAList, activityDataCopy)
            #print("2:" , preD_result)
    #print(numberOfDependencies)
    print("dependency check: ", dependencyCheck*10)
    return numberOfDependencies
def ongoingDependencyProcess(requestList, numberOfRequests, activityDataCopy): #process the requests for ongoing phase
    numberOfDependencies = 0
    dependencyCheck = 0
    for request in range((int)(numberOfRequests)):
        currentRequest = requestList[request]
        requestedActivity = currentRequest["activity"]
        currentStateofRequestedActivity = getCurrentState(requestedActivity, activityDataCopy)
        object = getObject(requestedActivity)
        operation = getOperation(requestedActivity, object)

        ##calculate time from here

        activityDependenciesDataCopy = activityDependenciesData
        if "onDA" in activityDependenciesDataCopy["dependency"]["activity"][requestedActivity]:
            onDAList = activityDependenciesDataCopy["dependency"]["activity"][requestedActivity]["onDA"]
            dependencyCheck = dependencyCheck + len(onDAList)
            onD_result = onD(onDAList, activityDataCopy)
            #print("1 ",onD_result)
            if (not onD_result):
                numberOfDependencies = numberOfDependencies + onUpdate(onDAList, activityDataCopy)
            onD_result = onD(onDAList, activityDataCopy)
            #print("2 ",onD_result)
        activityDataCopy["activity"][requestedActivity]["current"]["state"] = "inactive"
        with open("activity.json", "w") as outfile:
            json.dump(activityDataCopy, outfile, indent=4)
            outfile.close()
    #print(numberOfDependencies)
    print("dependency check: ", dependencyCheck*10)
    return numberOfDependencies

def postDependencyProcess(requestList, numberOfRequests, activityDataCopy): #process the requests for post phase
    numberOfDependencies = 0
    dependencyCheck = 0
    for request in range((int)(numberOfRequests)):
        currentRequest = requestList[request]
        requestedActivity = currentRequest["activity"]
        currentStateofRequestedActivity = getCurrentState(requestedActivity, activityDataCopy)
        object = getObject(requestedActivity)
        operation = getOperation(requestedActivity, object)

        ##calculate time from here

        activityDependenciesDataCopy = activityDependenciesData
        if "postDA" in activityDependenciesDataCopy["dependency"]["activity"][requestedActivity]:
            postDAList = activityDependenciesDataCopy["dependency"]["activity"][requestedActivity]["postDA"]
            dependencyCheck = dependencyCheck + len(postDAList)
            postD_result = postD(postDAList, activityDataCopy)
            #print("1 ",postD_result)
            if (not postD_result):
                numberOfDependencies = numberOfDependencies + postUpdate(postDAList, activityDataCopy)
            postD_result = postD(postDAList, activityDataCopy)
            #print("2 ",postD_result)
    #print(numberOfDependencies)
    print("dependency check: ", dependencyCheck*10)
    return numberOfDependencies
def engine():
    # this function is called at the beginning.
    # It takes input for the number of requests the user want to process
    # (give 1,2,3,or 4 as we have maximum 4 requests. each sent for 10 times).
    # It checks whether the request is for initial, ongoing or post phase.
    requestList = getRequests()
    numberOfRequests = input('How may requests do you want to process ?')
    phase = input('when are you calculating dependencies? ')
    if(phase == "initial"):
        numberOfDependencies = 0
        start_time_initial = time.time()
        #total_time = 0
        for i in range(10):
            activityObj = open("activity.json", "r")
            activityData = json.load(activityObj)
            activityDataCopy = activityData
            numberOfDependencies = numberOfDependencies + initialRequestProcess(requestList, numberOfRequests, activityDataCopy)
        end_time_initial = time.time()
        time_diff = (end_time_initial - start_time_initial)
        execution_time = time_diff*1000
        #avg_time = total_time
        print(f"Processing time for {numberOfRequests} in initial request is  {execution_time}")
        print("number of dependencies solved initially: ", numberOfDependencies)
        # # Open the source file containing JSON data
        with open('activity_old.json', 'r') as source_file:
            # Load JSON data from the source file
            data1 = json.load(source_file)

        # Open the destination file where you want to write the JSON data
        with open('activity.json', 'w') as destination_file:
            # Write JSON data to the destination file
            json.dump(data1, destination_file, indent=4)
            destination_file.close()

    elif (phase == "ongoing"):
        numberOfDependencies = 0
        start_time_ongoing = time.time()
        for i in range(10):
            activityObj = open("activity.json", "r")
            activityData = json.load(activityObj)
            activityDataCopy = activityData
            activityDataCopyCopy = activityDataCopy
            #print(activityDataCopyCopy)
            numberOfDependencies = numberOfDependencies + ongoingDependencyProcess(requestList, numberOfRequests,
                                                                                   activityDataCopy)
        end_time_ongoing = time.time()
        time_diff = (end_time_ongoing - start_time_ongoing)
        execution_time = time_diff*1000
        print(f"Processing time for {numberOfRequests} in ongoing processing is  {execution_time}")
        print("number of dependencies solved in ongoing: ", numberOfDependencies)
        with open('activity_old.json', 'r') as source_file:
            # Load JSON data from the source file
            data1 = json.load(source_file)

        # Open the destination file where you want to write the JSON data
        with open('activity.json', 'w') as destination_file:
            # Write JSON data to the destination file
            json.dump(data1, destination_file, indent=4)
            destination_file.close()

    elif (phase == "post"):
        numberOfDependencies = 0
        start_time_post = time.time()
        for i in range(10):
            activityObj = open("activity.json", "r")
            activityData = json.load(activityObj)
            activityDataCopy = activityData
            activityDataCopyCopy = activityDataCopy
            activityDataCopyCopyCopy = activityDataCopyCopy
            #print(activityDataCopyCopyCopy)
            numberOfDependencies = numberOfDependencies + postDependencyProcess(requestList, numberOfRequests,
                                                                                   activityDataCopy)
        end_time_post = time.time()
        time_diff = (end_time_post - start_time_post)
        execution_time = time_diff*1000
        print(f"Processing time for {numberOfRequests} is in post processing  {execution_time}")
        print("number of dependencies solved in post: ", numberOfDependencies)
        with open('activity_old.json', 'r') as source_file:
            # Load JSON data from the source file
            data1 = json.load(source_file)

        # Open the destination file where you want to write the JSON data
        with open('activity.json', 'w') as destination_file:
            # Write JSON data to the destination file
            json.dump(data1, destination_file, indent=4)
            destination_file.close()


engine() #this engine() function is called after running the program
