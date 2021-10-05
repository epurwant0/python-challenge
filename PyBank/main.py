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

    tm = f"Total Months: {totalMonths}"
    tn = f"Total Net: ${netTotal}"
    ac = f"Average Change: ${avgChange}"
    gi = f"Greatest Increase: {datesArr[avgPLArr.index(max(avgPLArr)) + 1]} ${max(avgPLArr)}"
    gd = f"Greatest Decrease: {datesArr[avgPLArr.index(min(avgPLArr)) + 1]} ${min(avgPLArr)}"

    print (tm)
    print (tn)
    print (ac)
    print (gi)
    print (gd)

    # save the output file path
output_file = os.path.join("/Users/ellis/Desktop/Misc/Homework_Submitted/3_Python/python-challenge/PyBank/Analysis/output_file.txt")

    # open the output file
with open(output_file, 'w') as result:
    result.writelines("Financial Analysis\n")
    result.writelines("-----------------------------\n")
    result.writelines(f"{tm}\n")
    result.writelines(f"{tn}\n")
    result.writelines(f"{ac}\n")
    result.writelines(f"{gi}\n")
    result.writelines(f"{gd}\n")

