import requests
import json
import os
class BlazemeterApi:
    api_key = None
    secreat_key = None
    auth = None
    cwd = os.getcwd()
    def __init__(self,api_key,secreat_key):
        self.api_key = api_key
        self.secreat_key = secreat_key
        self.auth = (self.api_key,self.secreat_key)
        
    def getFilesForTestID_Original_TestA(self,testIDvalue):
        url ="https://a.blazemeter.com/api/v4/tests/" + testIDvalue + "/files" 
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            user_data = response.json()
            with open(self.cwd+"/responces/getFilesForTestID_Original_TestA"+testIDvalue+".txt","w") as f:
                f.write(json.dumps(user_data,indent=3))
            print("getFilesForTestID_Original_TestA is executed for "+testIDvalue,"\n")
            return user_data
        else:
            print(f"Error: {response.status_code} - Unable to fetch user data\n")
    
    def getTestStaticticsForIDs(self,testIDvalue):
        url ="https://a.blazemeter.com/api/v4/masters?testId="+testIDvalue
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            user_data = response.json()
            with open(self.cwd+"/responces/getTestStaticticsForIDs"+testIDvalue+".txt","w") as f:
                f.write(json.dumps(user_data,indent=3))
            print("getTestStaticticsForIDs is executed for "+testIDvalue)
            return user_data
        else:
            print(f"Error: {response.status_code} - Unable to fetch user data {testIDvalue}")
    
    def RequestTestStatisticsForTestID(self,masters):
        url ="https://a.blazemeter.com/api/v4/masters/"+str(masters)+"/reports/aggregatereport/data"
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            user_data = response.json()
            with open(self.cwd+"/responces/RequestTestStatisticsForTest"+str(masters)+".txt","w") as f:
                f.write(json.dumps(user_data,indent=3))
            print("RequestTestStatisticsForTestID is executed for "+str(masters))
            return user_data
        else:
            print(f"Error: {response.status_code} - Unable to fetch user data {masters}")
    
                
        