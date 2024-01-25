import os #Code2 by Anoje Janathanan #Import Modules
import csv 

csvpath = os.path.join("election_data.csv") #import csv for analysis

sum_votes = 0 #initialize total vote counter
candidates = [] #Candidate names who recieved votes will be appended to this empty list
vote_results = []  #Vote Result data is appended to this empty list

cwd = os.getcwd()  #Code taken from https://www.tutorialspoint.com/python/os_getcwd.htm

output_file = os.path.join(os.getcwd(), "newtwo.csv") #Outputs text file of results to directory of user 
    
    
with open(csvpath, encoding='UTF-8') as csvfile: #open csv file/traverses through the csv accordingly 
    csvreader = csv.reader(csvfile, delimiter=",") 

    # Proceed to next row
    next(csvreader)

 
    for row in csvreader: #This for loop keeps note of the total number of votes with the candidate name 
        sum_votes = int(sum_votes + 1) #increments the total vote count 1 per iteration and updates the vote value #integer
        name = str(row[2]) #according to the csv file, row index 2 equates to the Candidate column #string

        if name not in candidates:  #Checks to see if the candidate who recieved votes is already appended to the list above, if not, it will add the name to the list 
            candidates.append(name)
            vote_results.append(1)
        else:
      
            index = candidates.index(name)#traverses to find the index of the candidate name in the list above
            vote_results[index] = vote_results[index] + 1 #increases by 1 accordingly 
            
winner_calculation = vote_results.index(max(vote_results))  #According to this, the winner is the one with the maximum amount of votes as shown in this code
winner = candidates[winner_calculation]  #Assign the winner as the candidate with the maximum amount of votes

#Outputs the final results in terminal #structured in order of the output 
print("Election Results") #Header 
print("-------------------------")
print("Total Votes:", sum_votes)
print("-------------------------")

for candidate, votes_results in zip(candidates, vote_results):   #calculates the percentage of votes based on the total votes that each candidate won
        percentage = (votes_results / sum_votes) * 100  
        print("{}: {:.3f}% ({})".format(candidate, percentage, votes_results))


print(f"-------------------------\n")
print("Winner:", winner) 
print(f"-------------------------\n")


#For the textfile content #Will Showcase these results in the file 
with open(output_file, "w", newline='') as pollfile:
    pollfile.write(f"Election Results\n")
    pollfile.write(f"------------------\n")
    pollfile.write(f"Total Votes: {sum_votes}\n")

    for candidate, vote_results in zip(candidates, vote_results):
        percentage = (vote_results / sum_votes) * 100
        pollfile.write("{}: {:.3f}% ({})\n".format(candidate, percentage, vote_results))

    pollfile.write(f"-----------------\n")
    pollfile.write("Winner: {}\n".format(winner))
    pollfile.write(f"-----------------\n")







