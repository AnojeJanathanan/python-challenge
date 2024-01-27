import os
import csv 
import statistics as modulethree

csvpath = os.path.join('Resources','budget_data.csv')

largest_date = ""  #Initialize as empty strings for data to be filled in accordingly
lowest_date = "" 
largest_amount = float("-inf")  #Keeps track of greatest increase   
lowest_amount = float("inf")    #Keeps track of greatest decrease

sum_months = 0 #initialize counters
net = 0
periodic_profit_loss = [] #Data will be appended to this empty list

cwd = os.getcwd() # #Code taken from https://www.tutorialspoint.com/python/os_getcwd.htm

output_file = os.path.join(os.getcwd(), "new.csv") #Output path to export as a textfile to any directory of those who run the code 

prior_value = None  #Initializing this line keeps track of prior values for iteration purposes  #This is similar to initializing a counter as 0
with open(csvpath, encoding='UTF-8') as csvfile: #Opens file and traverses through the csv 
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader) #goes on  to next row 

    for row in csvreader: #For Loop to traverse through the csv file accordingly 
        date = str(row[0]) #represents first row in the csv file, which is date
        column2 = int(row[1]) #represents 2nd row in the csv file, which is Profit/Losses

        sum_months = int(sum_months + 1)  #increases the sum_months variable by 1 and updates the data value per iteration
        net = int(net + column2) #Adds value from Profit Losses to the Net variable per iteration #updates values per iteration

        if prior_value is not None:   #If prior value is not none, store the difference between the Profit Losses/Prior Value as "Result" AKA Change 
            result = column2 - prior_value

            if result > largest_amount: #If the current result/change is larger than the greatest increase amount, update the greatest date/amount with the current results
                largest_date = date
                largest_amount = result

            if result < lowest_amount: #If the current result/change is less than the greatest_decrease_amount, update the values to the current results
                lowest_date = date
                lowest_amount = result

            periodic_profit_loss.append(result) #Append the current result into the list above #Stores the changes in profit/loss 

        prior_value = column2 #Keeps track of previous values  
    
average_change = modulethree.mean(periodic_profit_loss) #using the stats module, calculate the average of the appended values in the "Periodic_Profit_Loss" list

#Print the final results as shown below with formatting
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {sum_months}")
print(f"Total: ${net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {largest_date} (${largest_amount})") #Greatest Increase
print(f"Greatest Decrease in Profits: {lowest_date} (${lowest_amount})")   #Greatest Decrease

with open(output_file, "w", newline='') as finalfile: #Code taken from the "Reading, Writing, and Pyrithmetic" class
    finalfile.write(f"Financial Analysis\n")
    finalfile.write(f"------------------\n")
    finalfile.write(f"Total Months: {sum_months}\n")
    finalfile.write(f"Total: ${net}\n")
    finalfile.write(f"Average Change: ${average_change:.2f}\n")
    finalfile.write(f"Greatest Increase in Profits: {largest_date} (${largest_amount})\n")
    finalfile.write(f"Greatest Decrease in Profits: {lowest_date} (${lowest_amount})\n")
