import os
import csv

#Initialize variables

vote_counter = {} 
total_votes = 0
percent_votes = {}


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    poll = csv.reader(csvfile)

    #Read the header
    csv_header = next(poll)

## The total number of votes cast    
    for row in poll:
        candidate = row[2]
        total_votes += 1
        
## A complete list of candidates who received votes 
## The total number of votes each candidate won           
        if candidate in vote_counter:
            vote_counter[candidate] += 1
        else:
            vote_counter[candidate] = 1

## The percentage of votes each candidate won
    for candidate in vote_counter:
        percent_votes[candidate] = (vote_counter[candidate]/total_votes) * 100

## The winner of the election based on popular vote
    winner = max(vote_counter, key=vote_counter.get)

#Turn the dictionary keys and values into lists that can be called in the print statement
candidates_names = list(vote_counter.keys())
candidates_votes = list(vote_counter.values())
candidates_percents = list(percent_votes.values())

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates_names[0]}: {candidates_percents[0]:.3f}% ({candidates_votes[0]})")
print(f"{candidates_names[1]}: {candidates_percents[1]:.3f}% ({candidates_votes[1]})")
print(f"{candidates_names[2]}: {candidates_percents[2]:.3f}% ({candidates_votes[2]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("Election Results", 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(f"{candidates_names[0]}: {candidates_percents[0]:.3f}% ({candidates_votes[0]})\n")
    file.write(f"{candidates_names[1]}: {candidates_percents[1]:.3f}% ({candidates_votes[1]})\n")
    file.write(f"{candidates_names[2]}: {candidates_percents[2]:.3f}% ({candidates_votes[2]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
    

## Results should look like this:

## Election Results
## -------------------------
##Total Votes: 369711
## -------------------------
## Charles Casper Stockham: 23.049% (85213)
## Diana DeGette: 73.812% (272892)
## Raymon Anthony Doane: 3.139% (11606)
## -------------------------
## Winner: Diana DeGette
## -------------------------