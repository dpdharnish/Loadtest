import requests
import json
import os
class StomerunnerApi:
    def __init__(self,client_id,client_secret,TENANTID):
        self.cwd = os.getcwd()
        self.client_id = client_id
        self.client_secret=client_secret
        self.TENANTID = TENANTID
        url = "https://loadrunner-cloud.saas.microfocus.com/v1/auth-client?TENANTID="+self.TENANTID
        self.payload =  {
            "client_id": client_id,
            "client_secret": client_secret
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=json.dumps(self.payload), headers=headers)
        if response.status_code == 200:
            self.access_token = response.json().get("token")
            print('Access token is generated....')
            print(self.access_token)
        else:
            print("Failed to get the Bearer token. Status Code:", response.status_code)
            print("Response:", response.text)
    
    def getRunIDsforid(self,loadtest_id,project_id):
        url = 'https://loadrunner-cloud.saas.microfocus.com/v1/projects/'+str(project_id)+'/load-tests/'+loadtest_id+f'/runs?TENANTID={self.TENANTID}'
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            with open(self.cwd+"/responces/blaze_ids_"+str(loadtest_id)+".txt","w") as f:
                f.write(json.dumps(user_data,indent=3))
            print("getFilesForTestID_Original_TestA is executed for "+str(loadtest_id),"\n")
            return user_data
        else:
            print(f"Error: {response.status_code} - Unable to fetch user data\n")
            print("Response:", response.text)
    
    def GetIds_Details(self,id,percentile):
        url = 'https://loadrunner-cloud.saas.microfocus.com/v1/test-runs/'+str(id)+f'/transactions?TENANTID={self.TENANTID}&percentile={percentile}'
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            with open(self.cwd+"/responces/GetIds_Details_of_test_"+str(id)+".txt","w") as f:
                f.write(json.dumps(user_data,indent=3))
            print("getIds_Details is executed for "+str(id),"\n")
            return user_data
        else:
            print(f"Error: {response.status_code} - Unable to fetch user data\n")
            print("Response:", response.text)