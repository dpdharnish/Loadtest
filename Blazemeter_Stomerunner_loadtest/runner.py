###########################################################-- COMMAND TO RUN SCRIPT --####################################################
# python3 runner.py --run blazemeter    
# python3 runner.py --run stomerunner
# python3 runner.py --run blazemeter_stomerunner
#########################################################################################################################################

# Import all file and classes
from api.blazemeterapi import BlazemeterApi
from api.stomerunnerapi import StomerunnerApi
from api.replica_api import ReplicaAPI
from support.database_setup import *
from support.csv_reader import *
from support.database_handler import *
from support.args_lib import *
from runner import *
from setup import *

# Runner class where main operation take place
class Runner:
    def __init__(self): 
          
        # Creat DataBase, creat all necessary tables in database and creat csv files
        run = get_run()
        # Run the task
        if run=='blazemeter':
            setupblazemetercsv()
            setupblazemetertables()
            self.Blazemeter()
        elif run=='stomerunner':
            setupstomerunner()
            setupstomerunnertables()
            self.Stomerunner()
        elif run=='blazemeter_stomerunner':
            Setupcsvfiles()
            SetupDataBase()
            self.Blazemeter()
            self.Stomerunner()
        else:
            print("please make sure the --run is blazemeter or stomerunner or blazemeter_stomerunner......")
      
    def Blazemeter(self):
        print('featching data from the blazemeter......')
        API = BlazemeterApi(blaze_meter_api_key,blaze_meter_api_secreat)
        Replica_API = ReplicaAPI(hs_access_token)
        datas = read_blaze_meter_csv_file(blazemeter_path)
        for TestID,Domain,ApplicationName,BusinessUnit in datas:
            try:
                store_jmxlink_in_BlazemeterJMXfileTable(API.getFilesForTestID_Original_TestA(TestID))
                store_testRunID_in_BlazemeterTestrunIDS(API.getTestStaticticsForIDs(TestID))
                datas1 = get_runIDs_from_BlazemeterTestrunIDS(TestID)
                for id,created,ended,reportStatus in datas1:
                    try:
                        store_data_in_database_blazemeter(API.RequestTestStatisticsForTestID(id),TestID,id,created,ended,Domain,ApplicationName,BusinessUnit,reportStatus)
                        print("data stored for: ",id,"\n")
                    except:
                        print("\n")
                        unfound_runids_blazemeter(TestID,id,Domain,ApplicationName,BusinessUnit)
                        print("couldn't fine data for the "+str(id))
            except:
                unfound_test_ids_blazemeter(TestID,Domain,ApplicationName,BusinessUnit)
        # Uncomment the below line only when you what to push the data in replica db
        # Replica_API.store_data_into_replica_db_from_perfDataTableLatestAddtlDebug(fetch_data_from_perfDataTableLatestAddtlDebug())
        
    def Stomerunner(self):
        print('featching data from the stomerunner......')
        API = StomerunnerApi(stomerunner_client_id,stomerunner_client_secret,stomerunner_TENANTID)
        Replica_API = ReplicaAPI(hs_access_token)
        datas = read_stome_runner_csv_file(stomerunner_path)
        for loadtest,Domain,ApplicationName,BusinessUnit,TestScenario in datas:
            try:
                store_testRunID_in_StomeRunnerTestrunIDS(API.getRunIDsforid(loadtest,1),loadtest,1)
                datas1 = get_runIDs_from_StomeRunnerTestrunIDS(loadtest)
                for test_runs,created,ended,reportstatus,maxUsers,vusersNum,errorCode in datas1:
                    try:
                        print(test_runs+"..........")
                        store_data_database_stomerunner(API.GetIds_Details(test_runs,90),loadtest,test_runs,created,ended,reportstatus,maxUsers,vusersNum,errorCode,Domain,ApplicationName,BusinessUnit,TestScenario)
                        print("data stored for: ",test_runs,"\n")    
                    except:
                        print("\n")
                        unfound_runids_stomerunner(loadtest,test_runs,Domain,ApplicationName,BusinessUnit)         
                        print("couldn't fetch data for the "+test_runs)       
            except:
                unfound_test_ids_stomerunner(loadtest,Domain,ApplicationName,BusinessUnit)
                print("unfound for "+str(loadtest))
        # Uncomment the below line only when you what to push the data in replica db
        # Replica_API.store_data_into_replica_db_from_perfDataTableLatestLoadRunnerDebug(fetch_data_from_perfDataTableLatestLoadRunnerDebug())
     
if __name__ == "__main__":
    runner=Runner()