# Calculate each of the following values in the data set:
# Import the csv module 
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Initialize variables
count_of_months = 0
total_pl = 0
change_pl = 0
total_change_pl = 0
current_pl = 0
previous_pl = 0
greatest_increase = 0
increase_date = ""
greatest_decrease = 0
decrease_date = ""

# Open the csv and read it into a holder with the module
with open(csvpath, 'r') as csvfile:
    budget = csv.reader(csvfile)   
    #Read the header
    csv_header = next(budget)

# The total number of months included in the dataset
# This could be a count of rows
    
    for row in budget:
        count_of_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        # This is a sum of the P/L column
        
        current_pl = int(row[1])
        total_pl += current_pl    
    
        # The changes in "Profit/Losses" (pl) over the entire period,
        # This should read a line and the line below it into a variable and calculate the difference and output that into a list, then find the average of elements in the list.
        # The change in pl is equal to the current pl minus the previous pl
        
        if count_of_months > 1:
            change_pl = current_pl - previous_pl
            total_change_pl += change_pl

# The greatest increase in profits (date and amount) over the entire period
# Find the max from the variables in the previous step

        if change_pl > greatest_increase:
            greatest_increase = change_pl
            increase_date = row[0]

        # The greatest decrease in profits (date and amount) over the entire period
        # find the min from the variables in the previous step
        
        if change_pl < greatest_decrease:
            greatest_decrease = change_pl
            decrease_date = row[0]
        
        #When the next line runs this makes the previous value the current value
        previous_pl = current_pl


#  and then the average of those changes
average_change_pl = total_change_pl / (count_of_months - 1)


# Make it look like this:

# Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_of_months}")
print(f"Total: {total_pl}")
print(f"Average Change: {average_change_pl:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")


with open("Financial_Analysis.txt", 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months:  {count_of_months}\n")
    file.write(f"Total: {total_pl}\n")
    file.write(f"Average Change: {average_change_pl:.2f}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")
