import os
import csv

#getting csv file
pypoll = os.path.join("Resources", "PyPoll_Resources_election_data.csv")

#lists
candidate = []
vote_count = []

#variables
votes = 0
names = ""

#loop
with open(pypoll) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
   
    #The total number of votes cast
    for row in csv_reader: 
        votes = votes + 1

        #A complete list of candidates who received votes
        names = row[2]
        if names in candidate:
            index = candidate.index(names)
            vote_count[index] = vote_count[index] + 1
        else:
            candidate.append(names)
            vote_count.append(1)
            
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.      
percentages = []
max_votes = vote_count[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidate)):
    vote_percentage = round((vote_count[count]/votes*100))
    percentages.append(vote_percentage)
    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        print(max_votes)
        max_index = count
winner = candidate[max_index]

#print commands
print("Election Results")
print("---------------------")
print(f"Total Votes: {votes}")
print("---------------------")
for count in range(len(candidate)):
    print(f"{candidate[count]}: {percentages[count]}% ({vote_count[count]})")
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")

#create text file of analysis
with open('Election_Results.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("---------------------\n")
    f.write(f"Total Votes: {votes}\n")
    f.write("---------------------\n")
    for count in range(len(candidate)):
        f.write(f"{candidate[count]}: {percentages[count]}% ({vote_count[count]})\n")
    f.write("---------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("---------------------\n")
    f.close() 