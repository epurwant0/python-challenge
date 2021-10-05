import os
import csv

mainPath = "/Users/ellis/Desktop/Misc/Homework_Submitted/3_Python/python-challenge"
hwPath = "PyPoll/Resources"

csvPath = os.path.join(mainPath, hwPath, "election_data.csv")

totalVotes = 0
candidates = dict()
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
        checkKey(candidates, row[2])
    
    print(f"Total Votes: {totalVotes}")
    tv = f"Total Votes: {totalVotes}"
    
    for key in candidates:
        percent = "{:.0%}".format(candidates[key]/totalVotes)
        totalVArr.append(candidates[key])
        candArr.append(key)
        maxVotes = max(totalVArr)
        print(f"{key}: {percent} ({candidates[key]})")

    print(f"Winner: {candArr[totalVArr.index(max(totalVArr))]} ({maxVotes})")
    wn = f"Winner: {candArr[totalVArr.index(max(totalVArr))]} ({maxVotes})"

    # save the output file path
output_file = os.path.join("/Users/ellis/Desktop/Misc/Homework_Submitted/3_Python/python-challenge/PyPoll/Analysis/output_file.txt")

# open the output file
with open(output_file, 'w') as result:
    result.writelines("Election Results \n")
    result.writelines("-----------------------------\n")
    result.writelines(f"{tv}\n")
    result.writelines("-----------------------------\n")

    for key in candidates:
        percent = "{:.0%}".format(candidates[key]/totalVotes)
        vp = f"{key}: {percent} ({candidates[key]}"
        result.writelines(f"{vp}\n")
    
    result.writelines("-----------------------------\n")
    result.writelines(f"{wn}\n")
    result.writelines("-----------------------------\n")