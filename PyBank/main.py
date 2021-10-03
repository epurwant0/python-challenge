import os
import csv

mainPath = "/Users/ellis/Desktop/Misc/Homework_Submitted/3_Python/python-challenge"
hwPath = "PyBank/Resources"

csvPath = os.path.join(mainPath, hwPath, "budget_data.csv")

totalMonths = 0
netTotal = 0
prePL = 0
avgTot = 0
counter = 0
avgPLArr = []
datesArr = []

#print(open(csvPath).readlines())

with open(csvPath, newline = "") as budgetCSV:
    
    budgetReader = csv.reader(budgetCSV, delimiter = ",")
    #print(list(budgetReader)[1][1]) // 867884

    budgetHeader = next(budgetReader)

    for row in budgetReader:

        datesArr.append(row[0])
        totalMonths = totalMonths + 1
        netTotal = netTotal + int(row[1])

        if counter != 0:
            curPL = int(row[1])
            avgPLArr.append(curPL - prePL)
        
        prePL = int(row[1])
        counter = counter + 1

    avgChange = sum(avgPLArr) / len(avgPLArr)
    avgChange = round(avgChange, 2)

    print (f"Total Months: {totalMonths}")
    print (f"Total Net: ${netTotal}")
    print(f"Average Change: ${avgChange}")
    print (f"Greatest Increase: {datesArr[avgPLArr.index(max(avgPLArr)) + 1]} ${max(avgPLArr)}")
    print (f"Greatest Decrease: {datesArr[avgPLArr.index(min(avgPLArr)) + 1]} ${min(avgPLArr)}")
    

