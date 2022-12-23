# Dependencies 
import os
import csv

# Specify the file to read
budget_file = os.path.join("Resources", "budget_data.csv")

# Open the file to read
with open(budget_file) as csv_file:
    # Initialize csv.reader 
    csv_reader = csv.reader(csv_file, delimiter = ",")
    # Skip the header
    csv_header = next(csv_reader) 
    # Create variables for total, greatest increase and decrease, two empty lists for dollars amount and months
    total = 0
    increase = 0
    decrease = 0
    profit_list = []
    date_list = []
    # Iterate thru each row in the file
    for row in csv_reader:
        # Add the dollars to total
        total += int(row[1])
        # Add each dollors amount as an item to the list
        profit_list.append(int(row[1]))
        # Add each month as an item to the list
        date_list.append(row[0])
    # Number of the months = len(list)
    months = len(date_list)
    # Grab the dollar amount from first month
    first = profit_list[0]
    # Grab the dollar amount from last month
    last = profit_list[months - 1]
    # Create a empty list for changes over the entire period
    change_list = []
    # Iterate thru a range of number (0 to 85)
    for i in range(months - 1):    
        # Calculate the changess over the entire period
        change = int(profit_list[i + 1]) - int(profit_list[i])
        # Add the changes to list
        change_list.append(change)
        # Assign new values to increase and decrease varibale based on conditions met
        if change > increase:
            increase = change
            increase_date = date_list[i + 1]
        elif change < decrease:
            decrease = change
            decrease_date = date_list[i + 1]

# Output values
output = ("Financial Analysis" + "\n"
    "----------------------------" + "\n"
    f"Total Month: {months}" + "\n"
    f"Total: ${total}" + "\n"
    f"Average Change: ${((last - first)/(months - 1)):.2f}" + "\n"
    f"Greatest Increase in Profits: {increase_date} (${increase})" + "\n"
    f"Greatest Decrease in Profits: {decrease_date} (${decrease})"
    )

# Specify the file to write
financial_analysis = os.path.join("financial_analysis.txt")

# Open the file to write
with open(financial_analysis, "w") as text_file:
    # Write the file 
    text_file.write(output)