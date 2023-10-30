import csv
import os
cwd = os.getcwd()
def Setupcsvfiles():
    if (not os.path.exists(cwd+"/csv_files/unfound_ids_blazemeter.csv")):
        with open(cwd+"/csv_files/unfound_ids_blazemeter.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Domain","ApplicationName","BusinessUnit"])
            
    if (not os.path.exists(cwd+"/csv_files/unfound_runids_blazemeter.csv")):
        with open(cwd+"/csv_files/unfound_runids_blazemeter.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Runids","Domain","ApplicationName","BusinessUnit"])
            
    if (not os.path.exists(cwd+"/csv_files/unfound_ids_stomerunner.csv")):
        with open(cwd+"/csv_files/unfound_ids_stomerunner.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Domain","ApplicationName","BusinessUnit"])
    
    if (not os.path.exists(cwd+"/csv_files/unfound_runids_stomerunner.csv")):
        with open(cwd+"/csv_files/unfound_runids_stomerunner.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Runids","Domain","ApplicationName","BusinessUnit"])

def setupblazemetercsv():
    if (not os.path.exists(cwd+"/csv_files/unfound_ids_blazemeter.csv")):
        with open(cwd+"/csv_files/unfound_ids_blazemeter.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Domain","ApplicationName","BusinessUnit"])
            
    if (not os.path.exists(cwd+"/csv_files/unfound_runids_blazemeter.csv")):
        with open(cwd+"/csv_files/unfound_runids_blazemeter.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Runids","Domain","ApplicationName","BusinessUnit"])

def setupstomerunner():
    if (not os.path.exists(cwd+"/csv_files/unfound_ids_stomerunner.csv")):
        with open(cwd+"/csv_files/unfound_ids_stomerunner.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Domain","ApplicationName","BusinessUnit"])
    
    if (not os.path.exists(cwd+"/csv_files/unfound_runids_stomerunner.csv")):
        with open(cwd+"/csv_files/unfound_runids_stomerunner.csv","w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["TestID","Runids","Domain","ApplicationName","BusinessUnit"])
    
        
        
def unfound_test_ids_blazemeter(TestID,Domain,ApplicationName,BusinessUnit):
    with open(cwd+"/csv_files/unfound_ids_blazemeter.csv","a",newline="") as file:
        csv_writer = csv.writer(file)
        l1=[TestID,Domain,ApplicationName,BusinessUnit]
        csv_writer.writerow(l1)
        del(l1)

def unfound_runids_blazemeter(TestID,id,Domain,ApplicationName,BusinessUnit):
    with open(cwd+"/csv_files/unfound_runids_blazemeter.csv","a",newline="") as file:
        csv_writer = csv.writer(file)
        l1=[TestID,id,Domain,ApplicationName,BusinessUnit]
        csv_writer.writerow(l1)
        del(l1)

def unfound_test_ids_stomerunner(TestID,Domain,ApplicationName,BusinessUnit):
    with open(cwd+"/csv_files/unfound_ids_stomerunner.csv","a",newline="") as file:
        csv_writer = csv.writer(file)
        l1=[TestID,Domain,ApplicationName,BusinessUnit]
        csv_writer.writerow(l1)
        del(l1)

def unfound_runids_stomerunner(TestID,id,Domain,ApplicationName,BusinessUnit):
    with open(cwd+"/csv_files/unfound_runids_stomerunner.csv","a",newline="") as file:
        csv_writer = csv.writer(file)
        l1=[TestID,id,Domain,ApplicationName,BusinessUnit]
        csv_writer.writerow(l1)
        del(l1)
        
def read_blaze_meter_csv_file(path):
    try:
        with open(path, 'r') as file:
            print("\nCollecting data from the blazemeter csv file......\n")
            csv_reader = csv.DictReader(file)
            datas = []
            for data in csv_reader:
                # '\ufeffDomain'
                datas.append((data['TestID1'],data['\ufeffDomain'],data['ApplicationName'],data['BusinessUnit']))
            if len(datas)>0:
                for i in datas:
                    print(i)
                return datas 
            else:
                print("There is no data in the csv file.....")
    except:
        print("Error occurred while reading the csv file, make sure the path and colume name is correct...")
        print("excepted colume for blazemeter name Domain, ApplicationName, BusinessUnit, TestID1.....")

def read_stome_runner_csv_file(path):
    try:
        with open(path, 'r') as file:
            print("\nCollecting data from the stomerunner csv file......\n")
            csv_reader = csv.DictReader(file)
            datas = []
            for data in csv_reader:
                datas.append((data['TestID1'],data['\ufeffDomain'],data['ApplicationName'],data['BusinessUnit'],data['TestScenario']))
            if len(datas)>0:
                for i in datas:
                    print(i)
                return datas
            else:
                print("There is no data in the csv file.....")
    except:
        print("Error occurred while reading the csv file, make sure the path and colume name is correct...")
        print("excepted colume for blazemeter name Domain, ApplicationName, BusinessUnit, TestID1.....")
    

def read_jmeter_csv_file():
    pass
        
            
# read_stome_runner_csv_file("/Users/dharnishdp/awf/project_M/Loadtest/csv_files/samplefile.csv")