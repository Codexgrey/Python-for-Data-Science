from db_functions import *

#- read function; fetching and send to db
def fetchsend_data():
    readFile = open("C:\Users\user\Desktop\DATA - SCIENCE\Python 101\fileInpOut\ecorp data.csv", mode="r", encoding = "utf-8")
    header = readFile.readlines(1)
    wholedata = readFile.readlines()
    refineddata = [data.rstrip("\n") for data in wholedata]

    for entry in refineddata:
        xtracted_entry = entry.split(",")
        split_dt = xtracted_entry[2].split("/")
        sql_date = "-".join([split_dt[2], split_dt[1], split_dt[0]])
        write_data(xtracted_entry[0], int(xtracted_entry[1]), sql_date)


#- calling function
fetchsend_data()
