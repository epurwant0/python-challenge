import os
import csv

mainPath = "/Users/ellis/Desktop/Misc/Homework_Submitted/3_Python/python-challenge"
hwPath = "PyPoll/Resources"

csvPath = os.path.join(mainPath, hwPath, "election_data.csv")

totalVotes = 0
candids = dict()
totalVArr = []
candArr = []

def checkKey(dict, key):
    if key in dict.keys():
        curVote = dict[key]
        vote = int(curVote) + 1
        dict[key] = vote
    else:
        dict[key] = 1

with open(csvPath, newline = "") as electionCSV:

    electReader = csv.reader(electionCSV, delimiter = ",")

    electHeader = next(electReader)

    for row in electReader:
        totalVotes = totalVotes + 1
        checkKey(candids, row[2])
    
    print(f"Total Votes: {totalVotes}")
    
    for key in candids:
        percent = "{:.0%}".format(candids[key]/totalVotes)
        totalVArr.append(candids[key])
        candArr.append(key)
        maxVotes = max(totalVArr)
        print(f"{key}: {percent} ({candids[key]})")

    print(f"Winner: {candArr[totalVArr.index(max(totalVArr))]} ({maxVotes})")