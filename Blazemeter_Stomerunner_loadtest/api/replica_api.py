import requests
import json
import os
import csv
import traceback
class ReplicaAPI:
    access_token=None
    headers = None
    cwd = os.getcwd()
    def __init__(self,access_token):
        self.access_token = access_token
        # self.headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        self.headers = {'Authorization': 'Bearer {}'.format(self.access_token),"Content-Type": "application/json"}
        
    def store_data_into_replica_db_from_perfDataTableLatestAddtlDebug(self,datas):
        base_url = "https://api-dev.headspin.io/v0/replica/loadtest"
        request_url = f"{base_url}/upload"
        for TestID, TestRunID, startTime, endTime, passed, Domain, ApplicationName, BusinessUnit, labelName, is_parent, samples, avgResponseTime, avgThroughput, _90line,_95line, minResponseTime, maxResponseTime, avgBytes, errorsRate, TestScenario in datas:
            data_payload = {
                    "data": [
                        {
                            "domain": Domain,
                            "samples": int(samples),
                            "maxResponseTime": float(maxResponseTime),
                            "avgBytes": float(avgBytes),
                            "start_time": int(startTime),
                            "end_time": int(endTime),
                            "avgThroughput": float(avgThroughput),
                            "errorsRate": float(errorsRate),
                            "95line": float(_95line),
                            "business_unit": BusinessUnit,
                            "labelName":labelName,
                            "application_name": ApplicationName,
                            "minResponseTime": float(minResponseTime),
                            "test_id": TestID,
                            "test_run_id": TestRunID,
                            "avgResponseTime": float(avgResponseTime),
                            "90line": float(_90line)
                    }
                ]
            }
            print("\n\n")
            print(data_payload)
            response = requests.post(request_url, headers=self.headers, json=data_payload)
            print(json.dumps(response.json(),indent=3))
    
    def store_data_into_replica_db_from_perfDataTableLatestLoadRunnerDebug(self,datas):
        base_url = "https://api-dev.headspin.io/v0/replica/loadtest"
        request_url = f"{base_url}/upload"
        for TestID, TestRunID, startTime, endTime, passed, Domain, ApplicationName, BusinessUnit, labelName, is_parent, samples, avgResponseTime, avgThroughput, _90line,_95line, minResponseTime, maxResponseTime, avgBytes, errorsRate in datas:
            data_payload = {
                    "data": [
                        {
                            "domain": Domain,
                            "samples": None,
                            "maxResponseTime": float(maxResponseTime),
                            "avgBytes": None,
                            "start_time": int(startTime)//1000,
                            "end_time": int(endTime)//1000,
                            "avgThroughput": None,
                            "errorsRate": None,
                            "95line": None,
                            "business_unit": BusinessUnit,
                            "labelName":labelName,
                            "application_name": ApplicationName,
                            "minResponseTime": float(minResponseTime),
                            "test_id": TestID,
                            "test_run_id": TestRunID,
                            "avgResponseTime": float(avgResponseTime),
                            "90line": float(_90line)
                    }
                ]
            }
            print("\n\n")
            print(data_payload)
            response = requests.post(request_url, headers=self.headers, json=data_payload)
            print(json.dumps(response.json(),indent=3))
                    
       