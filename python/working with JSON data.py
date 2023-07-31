
import urllib.request
import json

def printResults(data):
    #use the JSON module to load the string data into a dictionary
    theJSON = json.loads(data)

#now we cabaccess the contents of the Json like any other python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"]) 

   #output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(count, "events recorded")

#for each event, print the place where it occurred 
    for i in theJSON['features']:
        print(i["properties"]["place"])
    print("-----------------\n")

    #print events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if ["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"])
    print("-----------------\n")


    #print only the events where at least 1 person reported feeling something
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
             print(i['properties']["place"],feltReports, "times")

def main():
    '''define a variable to hold the source URL
    in the case we 'll use the free data feed from the usgs
    this feed lists all the earthquakes for the last day larger than mag 2.5 '''
    urlData = "http://earthquake.usds.gov/earthquake/feed/v1.0/summary/2.5_day.geojson "
    #open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode()== 200):
        data = webUrl.read()
        printResults(data)

    else:
        print("sorry")


if __name__ == "__main__":
    main()
