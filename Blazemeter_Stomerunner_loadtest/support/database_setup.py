import mysql.connector as c
from setup import *
def Establish_connection_A():
    con = c.connect(host = loacldb_hostname,user = localdb_username, passwd = localdb_passwd)
    if con.is_connected():
        print("Successfully connected......")
        return con
    else:
        print("unable to connect to local database, make sure proper crendential is given....")
        
def Establish_connection_B():
    con = c.connect(host = loacldb_hostname,user = localdb_username, passwd = localdb_passwd,database = "testdatahandoff")
    if con.is_connected():
        print("Successfully connected to loacl db......")
        return con
    else:
        print("Unable to connect to local_database, make sure proper crendential is given....\n")

##############################################################-- SET UP THE DATABASE --##############################################################
def Establish_connection_to_creat_db_testDataHandOff():
    con = Establish_connection_A()
    cursor = con.cursor()
    query = "CREATE DATABASE IF NOT EXISTS testdatahandoff"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Database is created with name testdatahandoff......\n")
    
def creat_table_perfDataTableLatestAddtlDebug():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS perfDataTableLatestAddtlDebug (
        TestID TEXT NULL,
    	TestRunID TEXT NULL,
        startTime TEXT NULL,
        endTime TEXT NULL,
        passed TEXT NULL,
        Domain varchar(1000) NULL,
        ApplicationName varchar(1000) NULL,
		BusinessUnit varchar(1000) NULL,
		labelName varchar(1000) NULL,
		is_parent varchar(1000) NULL,
		samples varchar(1000) NULL,
		avgResponseTime varchar(1000) NULL,
		avgThroughput varchar(1000) NULL,
		90line varchar(1000) NULL,
		95line varchar(1000) NULL,
		minResponseTime varchar(1000) NULL,
		maxResponseTime varchar(1000) NULL,
		avgBytes varchar(1000) NULL,
		errorsRate varchar(1000) NULL,
		TestScenario varchar(1000) NULL
    )  ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name perfDataTableLatestAddtlDebug......\n")
    

def creat_table_perfDataTableLatestMatchingRows():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS perfDataTableLatestMatchingRows (
        TestID TEXT NULL,
        TestRunID TEXT NULL,
        startTime TEXT NULL,
        endTime TEXT NULL,
        passed TEXT NULL,
        Domain varchar(1000) NULL,
        ApplicationName varchar(1000) NULL,
        BusinessUnit varchar(1000) NULL,
        labelName varchar(1000) NULL,
        is_parent varchar(1000) NULL,
        samples varchar(1000) NULL,
        avgResponseTime varchar(1000) NULL,
        avgThroughput varchar(1000) NULL,
        90line varchar(1000) NULL,
        95line varchar(1000) NULL,
        minResponseTime varchar(1000) NULL,
        maxResponseTime varchar(1000) NULL,
        avgBytes varchar(1000) NULL,
        errorsRate varchar(1000) NULL,
        TestScenario varchar(1000) NULL
    )  ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name perfDataTableLatestMatchingRows......\n")

def creat_table_perfDataTableLatestJmeterDebug():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS perfDataTableLatestJmeterDebug (
        TestID TEXT NULL,
        TestRunID TEXT NULL,
        startTime TEXT NULL,
        endTime TEXT NULL,
        passed TEXT NULL,
        Domain varchar(1000) NULL,
        ApplicationName varchar(1000) NULL,
        BusinessUnit varchar(1000) NULL,
        labelName varchar(1000) NULL,
        is_parent varchar(1000) NULL,
        samples varchar(1000) NULL,
        avgResponseTime varchar(1000) NULL,
        avgThroughput varchar(1000) NULL,
        90line varchar(1000) NULL,
        95line varchar(1000) NULL,
        minResponseTime varchar(1000) NULL,
        maxResponseTime varchar(1000) NULL,
        avgBytes varchar(1000) NULL,
        errorsRate varchar(1000) NULL
    )  ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name perfDataTableLatestJmeterDebug......\n")

def creat_table_perfDataTableLatestJmeterDebugMatchingRows():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS perfDataTableLatestJmeterDebugMatchingRows (
        TestID TEXT NULL,
        TestRunID TEXT NULL,
        startTime TEXT NULL,
        endTime TEXT NULL,
        passed TEXT NULL,
        Domain varchar(1000) NULL,
        ApplicationName varchar(1000) NULL,
        BusinessUnit varchar(1000) NULL,
        labelName varchar(1000) NULL,
        is_parent varchar(1000) NULL,
        samples varchar(1000) NULL,
        avgResponseTime varchar(1000) NULL,
        avgThroughput varchar(1000) NULL,
        90line varchar(1000) NULL,
        95line varchar(1000) NULL,
        minResponseTime varchar(1000) NULL,
        maxResponseTime varchar(1000) NULL,
        avgBytes varchar(1000) NULL,
        errorsRate varchar(1000) NULL
    )  ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name perfDataTableLatestJmeterDebugMatchingRows......\n")

def creat_table_perfDataTableLatestLoadRunnerDebug():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS perfDataTableLatestLoadRunnerDebug (
        TestID TEXT NULL,
        TestRunID TEXT NULL,
        startTime TEXT NULL,
        endTime TEXT NULL,
        passed TEXT NULL,
        Domain varchar(1000) NULL,
        ApplicationName varchar(1000) NULL,
        BusinessUnit varchar(1000) NULL,
        labelName varchar(1000) NULL,
        is_parent varchar(1000) NULL,
        samples varchar(1000) NULL,
        avgResponseTime varchar(1000) NULL,
        avgThroughput varchar(1000) NULL,
        90line varchar(1000) NULL,
        95line varchar(1000) NULL,
        minResponseTime varchar(1000) NULL,
        maxResponseTime varchar(1000) NULL,
        avgBytes varchar(1000) NULL,
        errorsRate varchar(1000) NULL
    )  ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name perfDataTableLatestLoadRunnerDebug......\n")

def creat_table_perfDataTableLatestLoadRunnerDebugMatchingRows():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS perfDataTableLatestLoadRunnerDebugMatchingRows (
        TestID TEXT NULL,
        TestRunID TEXT NULL,
        startTime TEXT NULL,
        endTime TEXT NULL,
        passed TEXT NULL,
        Domain varchar(1000) NULL,
        ApplicationName varchar(1000) NULL,
        BusinessUnit varchar(1000) NULL,
        labelName varchar(1000) NULL,
        is_parent varchar(1000) NULL,
        samples varchar(1000) NULL,
        avgResponseTime varchar(1000) NULL,
        avgThroughput varchar(1000) NULL,
        90line varchar(1000) NULL,
        95line varchar(1000) NULL,
        minResponseTime varchar(1000) NULL,
        maxResponseTime varchar(1000) NULL,
        avgBytes varchar(1000) NULL,
        errorsRate varchar(1000) NULL
    )  ENGINE=INNODB;   
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name perfDataTableLatestLoadRunnerDebugMatchingRows......\n")

def creat_tables_for_jmx_link_blazemeter():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS BlazemeterJMXfileTable (
    name VARCHAR(255),
    link TEXT
    ) ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name BlazemeterJMXileTable......\n")
    
def creat_tabels_to_store_RunIDs_blazemeter():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS BlazemeterTestrunIDS (
    projectId INT,
    testId INT,
    id INT,
    name VARCHAR(255),
    userId INT,
    created INT,
    ended INT,
    maxUsers INT,
    reportStatus VARCHAR(255)
    ) ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name BlazemeterTestrunIDS......\n")

def creat_tabels_to_store_RunIDs_stomerunner():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS StomeRunnerTestrunIDS (
    projectId TEXT NULL,
    testId TEXT NULL,
    id TEXT NULL,
    name VARCHAR(255),
    created TEXT NULL,
    ended TEXT NULL,
    maxUsers TEXT NULL,
    reportStatus VARCHAR(255),
    vusersNum TEXT NULL,
    errorCode VARCHAR(255)
    ) ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name StomeRunnerTestrunIDS......\n")

def creat_stomerunner_template_file():
    con = Establish_connection_B()
    cursor = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS StomeRunnerTemplate (
    LoadTestId TEXT NULL,
    Test_Runs TEXT NULL,
    name VARCHAR(255),
    loadTestScriptId TEXT NULL,
    scriptName TEXT NULL,
    avgTRT TEXT NULL,
    minTRT TEXT NULL,
    maxTRT TEXT NULL,
    percentileTRT TEXT NULL,
    stdDeviation TEXT NULL,
    created TEXT NULL,
    ended TEXT NULL,
    maxUsers TEXT NULL,
    reportStatus VARCHAR(255),
    vusersNum TEXT NULL,
    errorCode VARCHAR(255),
    passed TEXT NULL,
    failed TEXT NULL
    ) ENGINE=INNODB;
    '''
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    print("Table is created with name StomeRunnerTemplate......\n")
    
def basemethod():
    print("Setting the database........")
    Establish_connection_to_creat_db_testDataHandOff()
    
def SetupDataBase():
    basemethod()
    creat_table_perfDataTableLatestAddtlDebug()
    creat_table_perfDataTableLatestMatchingRows()
    creat_table_perfDataTableLatestLoadRunnerDebug()
    creat_table_perfDataTableLatestLoadRunnerDebugMatchingRows()
    creat_tables_for_jmx_link_blazemeter()
    creat_tabels_to_store_RunIDs_blazemeter()
    creat_tabels_to_store_RunIDs_stomerunner()
    # creat_stomerunner_template_file()

def setupblazemetertables():
    basemethod()
    creat_table_perfDataTableLatestAddtlDebug()
    creat_table_perfDataTableLatestMatchingRows()
    creat_tables_for_jmx_link_blazemeter()
    creat_tabels_to_store_RunIDs_blazemeter()

def setupstomerunnertables():
    basemethod()
    creat_table_perfDataTableLatestLoadRunnerDebug()
    creat_table_perfDataTableLatestLoadRunnerDebugMatchingRows()
    creat_tabels_to_store_RunIDs_stomerunner()
    
    


