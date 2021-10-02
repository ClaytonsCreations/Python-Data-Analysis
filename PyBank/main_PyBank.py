import os
import csv

#getting csv file
pybank = os.path.join("Resources", "budget_data 3.csv")

#lists
months = []
profit_loss = []
change = []

#variables
total = 0
increase = 0
decrease = 0
increase_month = ""
decrease_month = ""

#loop
with open(pybank) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
   
    #The total number of months included in the dataset
    for row in csv_reader: 
        months.append(row[0])
    
        #The net total amount of "Profit/Losses" over the entire period
        #row[1] need to add all the negative, add all the positive and subtract negative by positive
          
        total = total + int(row[1])
        #The greatest increase in profits (date and amount) over the entire period
        #row[1] need to find the highest number and pull date from row[0]
        for i in range(len(profit_loss)-1):
            first = profit_loss[i]
            second = profit_loss[i+1]
            row_change = second - first
            change.append(row_change)

    #Finding greatest increase and decrease
        for j in range(len(change)):
            if change[j] > increase:
                increase = change[j]
                increase_month = months[-2]
              
        #The greatest decrease in profits (date and amount) over the over the entire period
        #row[1] need to find the lowest number and pull date from row[0]
            if change[j] < decrease:
                decrease = change[j]
                decrease_month = months[-2]

        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        #take net from above and divide by number of months
        profit_loss.append(int(row[1]))
    change = round((profit_loss[-1] - profit_loss[0]) / (len(months) -1),2) #need to round

#print commands
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: ${change}")
print(f"Greatest Increase in Profits: {increase_month} ${increase}")
print(f"Greatest Decrease in Profit:{decrease_month} ${decrease}")

#create text file of analysis
with open('PyBank_Financial_Analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("_ _ _ _ _ _ _ _ _ _ _\n")
    f.write(f"Total Months: {len(months)}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average Change: ${change}\n")
    f.write(f"Greatest Increase in Profits: {increase_month} ${increase}\n")
    f.write(f"Greatest Decrease in Profit: {decrease_month} ${decrease}\n")
    f.close()
