# PyBank & PyPoll

  The `PyBank` directory contains a Python script named `main.py` that analyzes the records in financial dataset called `budget_data.csv` and calculate each of the following values:

  1. The total number of months included in the dataset

  2. The net total amount of "Profit/Losses" over the entire period

  3. The changes in "Profit/Losses" over the entire period, and then the average of those changes

  4. The greatest increase in profits (date and amount) over the entire period

  5. The greatest decrease in profits (date and amount) over the entire period
  
  The script also print the analysis to the terminal and export a text file called `budget_analysis.txt` with the results.
  
    Financial Analysis
    ----------------------------
    Total Month: 86
    Total: $22564198
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)
  

  
  The `PyPoll` directory contains a Python script named `main.py` that analyzes the votes in a set of poll data called `election_data.csv` and calculates each of the following values:

  1. The total number of votes cast

  2. A complete list of candidates who received votes

  3. The percentage of votes each candidate won

  4. The total number of votes each candidate won

  5. The winner of the election based on popular vote
  
  The script also print the analysis to the terminal and export a text file called `election_final.txt` with the results.
  
   
    Election Results
    -------------------------
    Total votes: 369711
    -------------------------
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    -------------------------
    Winner: Diana DeGette
    -------------------------
    
