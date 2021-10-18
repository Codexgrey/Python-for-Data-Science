from datetime import datetime as dt
import csv


read_file = open("fileInpOut\Rawfile.txt", mode = "r", encoding= "utf-8")
whole_data = read_file.readlines()
# print(len(whole_data))

overview = whole_data[:5]
# print(overview);
# print("\n")


## strip out '\n' at the end of every string
refined_data = [entry.rstrip("\n") for entry in whole_data]
refined_data[0] = refined_data[0].lstrip("\ufeff")
# print(refined_data[:5])


## sorting data with respect to date
sorted_refData = sorted(refined_data, key = lambda c: dt.strptime(c.split(" on ")[1], "%d-%m-%Y"))
# print(sorted_refData[:5])
# print("\n")
# print(sorted_refData[-5:])


##extracting name, sales and date into seperate lists
nameList = []
salesList = []
dateList = []

for entry in sorted_refData:
    xtract_name = entry.split(":")[0]
    nameList.append(xtract_name);

    xtract_sales = int(entry.split(" on ")[0].split(" : ")[1].lstrip("₦"))
    salesList.append(xtract_sales);

    xtract_dates = entry.split(" on ")[1]
    dateList.append(xtract_dates);

dateList = list(map(lambda c: c.replace("-", "/"), dateList))

# print(nameList[:3])
# print(salesList[:3])
# print(dateList[:3])
    

# Excel part    
# writing into a csv file
new_file = open("fileInpOut\ecorp data.csv", mode = "w", encoding="utf-8", newline="")

#create a csc writer object
handleWriting = csv.writer(new_file)

#writing a row: first row/header
handleWriting.writerow(["name", "sales", "date"])

#an example of writerows: to write multiple rows
# handleWriting.writerows([["John", 12, "Today"], ["Dave", 15, "Tomorrow"]])

#writing the rest of the data
for num in range(len(sorted_refData)):
    handleWriting.writerow([nameList[num], salesList[num], dateList[num]])

new_file.close()


#Excel 2
agentsList = sorted(set(nameList))
# print(agentsList)


# First Method
agents_sales = []
for agent in agentsList:
    agentSum = 0
    for index, name in enumerate(nameList):
        if agent == name:
            sales = salesList[index]
            agentSum += sales
        else:
            pass
    agents_sales.append(agentSum);


# Second Method
smart_salesDict = {}
for name, sales in zip(nameList, salesList):
    smart_salesDict[name] = smart_salesDict.get(name, 0) + sales
# print(smart_salesDict)



## Week 4...
sorted_namesDict = dict(sorted(smart_salesDict.items(), key = lambda a: a[0]))
# print(sorted_namesDict)

unique_agents = sorted_namesDict.keys()
unique_agentSales = sorted_namesDict.values()
unique_agentCommission = list(map(lambda c: c * 0.045, unique_agentSales))
total_Sales = sum(unique_agentSales)
unique_agentImpact = list(map(lambda c: str((c/total_Sales) * 100) + "%", unique_agentSales))


# agentImpact = {}
# for agent, sales in zip(unique_agents, unique_agentSales):
#     agentImpact[agent] = agentImpact.get(agent, "") + (str(round((sales * 100)/total_Sales, 3)) + "%")
# print(agentImpact.get('Shae Buggs '))


### Data For Second Excel Sheet
import xlwt
from tempfile import TemporaryFile as TF

total_Sales = sum(unique_agentSales)
total_commissions = sum(unique_agentCommission)
net_revenue = total_Sales - total_commissions

# getting empty book
book = xlwt.Workbook()

# adding desired number of sheets
firstSheet = book.add_sheet("agents' records")
secondSheet = book.add_sheet("revenue records")

# writing into sheets
# first sheet
firstSheet.write(0, 0, "agent name")
firstSheet.write(0, 1, "agent sales")
firstSheet.write(0, 2, "agent commission")
firstSheet.write(0, 3, "agent impact")

for index, entry in enumerate(unique_agents):
    firstSheet.write(index + 1, 0, entry) # cos index at 0, 0 is already "Agent Name"

for index, entry in enumerate(unique_agentSales):
    firstSheet.write(index + 1, 1, entry)

for index, entry in enumerate(unique_agentCommission):
    firstSheet.write(index + 1, 2, entry)

for index, entry in enumerate(unique_agentImpact):
    firstSheet.write(index + 1, 3, entry)

# second sheet
secondSheet.write(0, 0, "total revenue")
secondSheet.write(0, 1, "total commission")
secondSheet.write(0, 2, "net revenue")

secondSheet.write(1, 0, total_Sales)
secondSheet.write(1, 1, total_commissions)
secondSheet.write(1, 2, net_revenue)

# saving
book.save("fileInpOut\Ecorp Data.xls")
book.save(TF())





#--- Task A
sorted_salesDict = dict(sorted(smart_salesDict.items(), key = lambda c: c[1], reverse=True))
top10_agents = list(sorted_salesDict)[:10]
print(top10_agents)



#--- Task B
# creating months list
monthsList = []
for num in range(1, 13):
    monthsList.append(dt(2020, num, 1).strftime("%B"))

# creating list for months in which sales where made
salesMonths = list(map(lambda c: c.split("/")[1], dateList)) 

# finding total sales per month
monthlySales = {}
for month, sales in zip(salesMonths, salesList):
    monthlySales[month] = monthlySales.get(month, 0) + sales

# zipping spelt out months to total sales figures
zipped_monthlySales = list(zip(monthsList, monthlySales.values()))
# print(zipped_monthlySales)



#--- Task C
monthlySales_Desc = sorted(zipped_monthlySales, key = lambda c: c[1], reverse=True)
salesMonth_Highest = monthlySales_Desc[0][0]
salesMonth_Lowest = monthlySales_Desc[-1][0]
# print(salesMonth_Highest)
# print(salesMonth_Lowest)



#--- Task D
agentCommissions = {}
for name, sales in zip(nameList, salesList):
    agentCommissions[name] = agentCommissions.get(name, 0) + round(sales * 0.045)
# print(agentCommissions)
# print(len(agentCommissions))
