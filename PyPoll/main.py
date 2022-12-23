# Dependencies
import os 
import csv

# Specify the file to read
election_file = os.path.join("Resources", "election_data.csv")

# Open the file to read
with open(election_file) as file:
    # Initialize csv.reader 
    csv_reader = csv.reader(file, delimiter = ",")
    # Skip the header
    csv_header = next(csv_reader)
    # Create variables for total votes, votes for each candidate and a empty dictionary
    votes = 0
    c_vote = 0
    d_vote = 0
    r_vote = 0
    candidates_dict = {}
    # Iterate thru each row in the file
    for row in csv_reader:
        # Add 1 vote to total votes with each iteration
        votes += 1
        # Count the votes each candidate receives
        if row[2] == "Charles Casper Stockham":
            c_vote += 1
        elif row[2] == "Diana DeGette":
            d_vote += 1
        elif row[2] == "Raymon Anthony Doane":
            r_vote += 1
        # Assign votes as value to each candidate name as key in a dictionary
        candidates_dict["Charles Casper Stockham"] = c_vote
        candidates_dict["Diana DeGette"] = d_vote
        candidates_dict["Raymon Anthony Doane"] = r_vote
    # Find the greatest amount of votes 
    max_vote = max(candidates_dict.values())
    # Access the dictionary and find the candidate with the greatest amount of votes 
    for name in candidates_dict:
        if max_vote == candidates_dict[name]:
            winner = name

# Output values
output = ("Election Results" + "\n"
    "-------------------------" + "\n"  
    f"Total votes: {votes}" + "\n"
    "-------------------------" + "\n"  
    f"Charles Casper Stockham: {100 * c_vote / votes:.3f}% ({c_vote})" + "\n"
    f"Diana DeGette: {100 * d_vote / votes:.3f}% ({d_vote})" + "\n"
    f"Raymon Anthony Doane: {100 * r_vote / votes:.3f}% ({r_vote})" + "\n"
    "-------------------------" + "\n"
    f"Winner: {winner}" + "\n"
    "-------------------------"
    )
    
# Specify the file to write
election_final = os.path.join("election_final.txt")

# Open the file to write
with open(election_final, "w") as text_file:
    text_file.write(output)
