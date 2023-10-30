import mysql.connector as c
from setup import *

# To establish the connection with the local database

def Establish_connection():
    con = c.connect(host = loacldb_hostname,user = localdb_username, passwd = localdb_passwd,database = "testdatahandoff")
    if con.is_connected():
        print("\nSuccessfully connected to loacl db......")
        return con
    else:
        print("Unable to connect to local_database, make sure proper crendential is given....\n")
        
        
##############################################################################################################################################################################################################################################################################      
############################################################-- BLAZEMETER --##################################################################################################################################################################################################                  
##############################################################################################################################################################################################################################################################################  
        
def store_jmxlink_in_BlazemeterJMXfileTable(dictionary):
    con = Establish_connection()
    cursor = con.cursor()
    for result in dictionary['result']:
        query1 = f"SELECT count(*) FROM BlazemeterJMXfileTable where link='{result['link']}';"
        cursor.execute(query1)
        k = cursor.fetchall() #[(0,)] or [(1,)]
        if (k[0][0]==0):
            query = f"INSERT INTO BlazemeterJMXfileTable (name, link) VALUES ('{result['name']}','{result['link']}');"
            cursor.execute(query)
            con.commit()
            print("Inserting data in the BlazemeterJMXfileTable......\n")
        else:
            print("data already exist in BlazemeterJMXfileTable.....")
    cursor.close()
    con.close()
    
    
def store_testRunID_in_BlazemeterTestrunIDS(dictionary):
    con = Establish_connection()
    cursor = con.cursor()
    for result in dictionary['result']:
        query1 = f"SELECT count(*) FROM BlazemeterTestrunIDS where testId={result['testId']} and id={result['id']};"
        cursor.execute(query1)
        k = cursor.fetchall()
        if (k[0][0]==0):
            query = f'''
            INSERT INTO BlazemeterTestrunIDS (projectId, testId, id, name, userId, created, ended, maxUsers, reportStatus)
            VALUES ({result["projectId"]}, 
                    {result["testId"]}, 
                    {result["id"]}, 
                    '{result["name"]}', 
                    {result["userId"]}, 
                    {result["created"]},
                    {result["ended"]},
                    {result["maxUsers"]},
                    '{result["reportStatus"]}'
                    );
            '''
            cursor.execute(query)
            con.commit()
            print("Inserting data in the BlazemeterTestrunIDS......\n")
        else:
            print("data already exist in the BlazemeterTestrunIDS.......")
    cursor.close()
    con.close()
    
    

def get_runIDs_from_BlazemeterTestrunIDS(Testid):
    con = Establish_connection()
    cursor = con.cursor()
    query = f"SELECT DISTINCT id,created,ended,reportStatus FROM BlazeMeterTestrunIDS WHERE testId={Testid}"
    cursor.execute(query)
    datas = cursor.fetchall()
    return datas 


def store_data_in_database_blazemeter(dictionary,TestID,id,created,ended,Domain,ApplicationName,BusinessUnit,reportStatus):
    con = Establish_connection()
    cursor = con.cursor()
    for result in dictionary['result']:
        query = f"SELECT count(*) FROM perfDataTableLatestAddtlDebug where TestID='{TestID}' and TestRunID='{id}' and labelName='{result['labelName']}';"
        cursor.execute(query)
        k = cursor.fetchall()
        if (k[0][0]==0):
            query = f'''INSERT INTO perfDataTableLatestAddtlDebug (
                    TestID, 
                    TestRunID, 
                    startTime, 
                    endTime, 
                    passed, 
                    Domain, 
                    ApplicationName, 
                    BusinessUnit, 
                    labelName, 
                    is_parent, 
                    samples, 
                    avgResponseTime, 
                    avgThroughput, 
                    90line, 
                    95line, 
                    minResponseTime, 
                    maxResponseTime, 
                    avgBytes, 
                    errorsRate, 
                    TestScenario)
                    VALUES
                    ('{TestID}', 
                    '{id}', 
                    '{created}', 
                    '{ended}', 
                    '{reportStatus}', 
                    '{Domain}', 
                    '{ApplicationName}', 
                    '{BusinessUnit}', 
                    '{result['labelName']}', 
                    'True', 
                    '{result['samples']}', 
                    '{result['avgResponseTime']}', 
                    '{result['avgThroughput']}', 
                    '{result['90line']}', 
                    '{result['95line']}', 
                    '{result['minResponseTime']}', 
                    '{result['maxResponseTime']}', 
                    '{result['avgBytes']}', 
                    '{result['errorsRate']}', 
                    'null');
                    '''
            cursor.execute(query)
            con.commit()
            print("store database in perfDataTableLatestAddtlDebug.....")
        else:
            query = f'''
            INSERT IGNORE INTO perfDataTableLatestMatchingRows (TestID, TestRunID, startTime, endTime, passed, Domain, ApplicationName, BusinessUnit, labelName, is_parent, samples, avgResponseTime, avgThroughput, 90line, 95line, minResponseTime, maxResponseTime, avgBytes, errorsRate, TestScenario)
            SELECT '{TestID}', '{id}', '{created}', '{ended}', '{reportStatus}', '{Domain}', '{ApplicationName}', '{BusinessUnit}', '{result['labelName']}', 'Ture', '{result['samples']}', '{result['avgResponseTime']}', '{result['avgThroughput']}', '{result['90line']}', '{result['95line']}', '{result['minResponseTime']}', '{result['maxResponseTime']}', '{result['avgBytes']}', '{result['errorsRate']}', 'null'
            FROM dual
            WHERE NOT EXISTS (
                SELECT 1
                FROM perfDataTableLatestMatchingRows
                WHERE TestRunID = '{id}'
                AND TestID = '{TestID}'
                AND labelName = '{result['labelName']}'
            );
            '''
            cursor.execute(query)
            con.commit()
            print("Storing data in the perfDataTableLatestMatchingRows.... ")
        print("\n")
    cursor.close()
    con.close()
    print("Inserting data in the Tables......\n")

def fetch_data_from_perfDataTableLatestAddtlDebug():
    con = Establish_connection()
    cursor = con.cursor()
    query = f"SELECT DISTINCT * FROM perfDataTableLatestAddtlDebug;"
    cursor.execute(query)
    return cursor.fetchall()

#######################################################################################################################################    
############################################################-- STOMERUNNER --##########################################################               
#######################################################################################################################################  

def store_testRunID_in_StomeRunnerTestrunIDS(dictionary,id,project_id):
    con = Establish_connection()
    cursor = con.cursor()
    for result in dictionary:
        query1 = f"SELECT count(*) FROM StomeRunnerTestrunIDS where testId='{int(id)}' and id='{int(result['id'])}';"
        cursor.execute(query1)
        k = cursor.fetchall()
        if (k[0][0]==0):
            query = f'''
            INSERT INTO StomeRunnerTestrunIDS (projectId, testId, id, name, created, ended, maxUsers, reportStatus, vusersNum, errorCode)
            VALUES ('{int(project_id)}', 
                    '{int(id)}', 
                    '{int(result["id"])}', 
                    '{result["testName"]}', 
                    '{int(result["startOn"])}',
                    '{int(result["duration"])+int(result["startOn"])}',
                    '{result["totalCount"]}',
                    '{result["status"]}',
                    '{result["vusersNum"]}',
                    '{result["errorCode"]}'
                    );
            '''
            cursor.execute(query)
            con.commit()
            print("Inserting data in the StomeRunnerTestrunIDS......\n")
        else:
            print("data already exist in the StomeRunnerTestrunIDS........")
    cursor.close()
    con.close()
    
    
    
def get_runIDs_from_StomeRunnerTestrunIDS(Testid):
    con = Establish_connection()
    cursor = con.cursor()
    query = f"SELECT DISTINCT id,created,ended,reportStatus,maxUsers,vusersNum,errorCode FROM StomeRunnerTestrunIDS WHERE testId={Testid}"
    cursor.execute(query)
    datas = cursor.fetchall()  # [(id,created,ended,reportStatus,maxUsers,vusersNum,errorCode),()]
    return datas

def store_data_database_stomerunner(dictionary,loadtest,test_runs,created,ended,reportstatus,maxUsers,vusersNum,errorCode,Domain,ApplicationName,BusinessUnit,TestScenario):
    con = Establish_connection()
    cursor = con.cursor()
    for result in dictionary:
        query = f"SELECT count(*) FROM perfDataTableLatestLoadRunnerDebug  where TestID='{loadtest}' and TestRunID='{test_runs}' and labelName='{result['name']}' and avgResponseTime='{result['avgTRT']}';"
        cursor.execute(query)
        k = cursor.fetchall()
        if (k[0][0]==0):
            query = f'''INSERT INTO perfDataTableLatestLoadRunnerDebug (
                    TestID, 
                    TestRunID, 
                    startTime, 
                    endTime, 
                    passed, 
                    Domain, 
                    ApplicationName, 
                    BusinessUnit, 
                    labelName, 
                    is_parent, 
                    samples, 
                    avgResponseTime, 
                    avgThroughput, 
                    90line, 
                    95line, 
                    minResponseTime, 
                    maxResponseTime, 
                    avgBytes, 
                    errorsRate)
                    VALUES
                    ('{loadtest}', 
                    '{test_runs}', 
                    '{created}', 
                    '{ended}', 
                    '{reportstatus}', 
                    '{Domain}', 
                    '{ApplicationName}', 
                    '{BusinessUnit}', 
                    '{result['name']}', 
                    'True', 
                    'sample_unknow', 
                    '{result['avgTRT']}', 
                    'N/A', 
                    '{result['percentileTRT_90']}', 
                    'N/A', 
                    '{result['minTRT']}', 
                    '{result['maxTRT']}', 
                    'N/A', 
                    'N/A');
                    '''
            cursor.execute(query)
            con.commit()
            print("store database in perfDataTableLatestLoadRunnerDebug.....")
        else:
            query = f'''
            INSERT IGNORE INTO perfDataTableLatestLoadRunnerDebugMatchingRows (TestID, TestRunID, startTime, endTime, passed, Domain, ApplicationName, BusinessUnit, labelName, is_parent, samples, avgResponseTime, avgThroughput, 90line, 95line, minResponseTime, maxResponseTime, avgBytes, errorsRate)
            SELECT '{loadtest}', '{test_runs}', '{created}', '{ended}', '{reportstatus}', '{Domain}', '{ApplicationName}', '{BusinessUnit}', '{result['name']}', 'Ture', 'sample_unknow', '{result['avgTRT']}', 'N/A', '{result['percentileTRT_90']}', 'N/A', '{result['minTRT']}', '{result['maxTRT']}', 'N/A', 'N/A'
            FROM dual
            WHERE NOT EXISTS (
                SELECT 1
                FROM perfDataTableLatestLoadRunnerDebugMatchingRows
                WHERE TestRunID = '{test_runs}'
                AND TestID = '{loadtest}'
                AND labelName = '{result['name']}'
                AND avgResponseTime='{result['avgTRT']}'
            );
            '''
            cursor.execute(query)
            con.commit()
            print("Storing data in the perfDataTableLatestLoadRunnerDebugMatchingRows.... ")
        print("\n")
    cursor.close()
    con.close()
    print("Inserting data in the Tables......\n")

def fetch_data_from_perfDataTableLatestLoadRunnerDebug():
    con = Establish_connection()
    cursor = con.cursor()
    # query = f"SELECT DISTINCT * FROM perfDataTableLatestLoadRunnerDebug;"
    query = "select DISTINCT * from perfDataTableLatestLoadRunnerDebug;"
    cursor.execute(query)
    return cursor.fetchall()
    


#####################################################################################################################################################################################################################################################################################################################################################################################################################        
###################################################################-- SUPPORT METHOD --#######################################################################################################################################################################################################################################################################################################################################                
#####################################################################################################################################################################################################################################################################################################################################################################################################################    
        

def fetch_data_from_perfDataTableLatestMatchingRows():
    con = Establish_connection()
    cursor = con.cursor()
    query = f"SELECT DISTINCT * FROM perfDataTableLatestMatchingRows;"
    cursor.execute(query)
    return cursor.fetchall()