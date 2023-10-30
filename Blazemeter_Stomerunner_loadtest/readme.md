# Blazemeter and stomerunner DataHandler
- BlazeMeter is a popular performance testing and load testing platform. It allows you to simulate traffic to your website or application, providing insights into how it performs under different levels of load. It's often used for stress testing, scalability testing, and measuring the performance of web applications.
- StormRunner Load is a cloud-based performance testing tool offered by Micro Focus. It's designed to test the performance and scalability of web and mobile applications. It allows you to create and execute performance tests in the cloud, making it easier to simulate large user loads from different geographic locations.

## Description: The primary objective of this script is to retrieve test run data from Blazemeter and Stomerunner through their respective APIs, save this data in a local database, and then filter out any duplicate entries before storing the unique data in a replica database.

## initial setup
### step1: install python version 3.10.7 (https://www.python.org/) and also set the directory in the .zshrc file
### step2: install database mysql (https://www.mysql.com/)
### step3: install following library, 'requests' and 'mysql-connector'
### step4: command to install above library (pip3 install mysql-connector-python) and (pip3 install requests)
### step5: Make sure to specify all credentials details in the setpu.py file

## command to run script
### command to run blazemeter: python3 runner.py --run blazemeter
### command to run stomerunner: python3 runner.py --run stomerunner
### command to run both: python3 runner.py --run blazemeter_stomerunner

- Note1: if you need to push the data into replica database for blazemeter, uncomment line 62 in runner.py file
- Note1: if you need to push the data into replica database for stomerunner, uncomment line 86 in runner.py file

## file details
### ./api/blazemeterapi.py: This script manages interactions with the BlazeMeter API.
### ./api/stomerunnerapi.py: This script handles communications with the Stomerunner API.
### ./api/replica_api.py: This script is responsible for transferring data from the local database to the replica database using an API.
### ./csv_files: Within this folder, you'll find files containing essential details, including Test IDs, Application Names, Domains, and Business Units. It also houses records of unfound test IDs and test runs.
### ./response: This directory stores all responses obtained from the BlazeMeter API and Stomerunner API.
### ./support/args_libs.py: This file is designed to parse command-line arguments effectively.
### ./support/csv_reader.py: This script plays a key role in reading data from CSV files, such as information about Domains, Business Units, Application Names, Test Scenarios, and Test ID records. It also handles the storage of unfound test IDs in CSV format.
### ./support/database_handler.py: This script is responsible for interacting with the local database and includes functionality to filter data stored in the local database.
### ./support/database_setup.py: This file's purpose is to create the necessary database structure and tables.
### runner.py: This serves as the main runner script, acting as the central component that connects all the .py files and orchestrates the workflow.
### setup.py: Here, you'll find details related to credentials and setup information.