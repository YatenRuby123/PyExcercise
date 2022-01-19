#1. Create a python method that takes arguments int X and int Y,
#and updates DEPART and RETURN fields
#in test_payload1.xml:
#- DEPART gets set to X days in the future from the current date
#(whatever the current date is at the moment of executing the code)
#- RETURN gets set to Y days in the future from the current date
#Please write the modified XML to a new file.

#Solution 1
import xml.etree.ElementTree
from datetime import date
from datetime import timedelta

def update_payload1(X: int, Y: int):
    new_parsed_file = xml.etree.ElementTree.parse("test_payload1.xml")
    file_root = new_parsed_file.getroot()

    for DEPART in file_root.iter("DEPART"):
        DEPART.text = (date.today() + timedelta(days=X)).strftime("%Y%m%d")

    for RETURN in file_root.iter("RETURN"):
        RETURN.text = (date.today() + timedelta(days=Y)).strftime("%Y%m%d")

    new_parsed_file.write("updated_payload1.xml")

update_payload1(2, 8)
#-----------------------------------------------------------------------------------------------

# 2. Create a python method that takes a json element
# as an argument, and removes that element from test_payload.json.
# Please verify that the method can remove either nested or non-nested elements
# (try removing "outParams" and "appdate").
# Please write the modified json to a new file.

#Solution 2
import json

def remove_elem_from_json(a):
    with open('test_payload.json', 'r') as file:
        result = json.load(file)
    if a in result:
        result.pop(a,None)
    with open('updated_payload.json', 'w') as file:
        results  = json.dump(result, file)

remove_elem_from_json("outParams")

#-----------------------------------------------------------------------------------------------

# 3. Create a python script that parses jmeter log files in CSV format,
# and in the case if there are any non-successful endpoint responses recorded in the log,
# prints out the label, response code, response message, failure message,
# and the time of non-200 response in human-readable format in PST timezone
# (e.g. 2021-02-09 06:02:55 PST).

#Solution 3
import csv
from datetime import datetime
import pandas as pd
from pytz import timezone

def jmeter_log_parser(filename):
    input_file =  pd.read_csv(filename, delimiter=','  , engine='python')
    responseCode = None
    responseMessage = None
    failureMessage = None
    timeStamp = None
    Label = None
    for i in range(len(input_file)):
        if input_file.values[i][3] != 200:
            responseCode = input_file.values[i][3]
            Label = input_file.values[i][2]
            responseMessage = input_file.values[i][4]
            failureMessage = input_file.values[i][8]
            timeStamp = input_file.values[i][0]
            print ("Label is : " + Label)
            print("Response Code is: " +  str(responseCode))
            print("Response Message is: "  + responseMessage)
            if str(failureMessage) == "nan":
                print("Failure Message is: ")
            fmt = "%Y-%m-%d %H:%M:%S %Z%z"
            now_utc = timeStamp
            now_pacific = datetime.fromtimestamp(now_utc / 1000, tz=timezone('UTC')).astimezone(timezone('US/Pacific'))
            print(now_pacific.strftime(fmt))
            print('--------------')

jmeter_log_parser("Jmeter_log1.jtl")












