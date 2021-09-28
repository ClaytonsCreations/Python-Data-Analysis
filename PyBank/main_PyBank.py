import os
import csv

#getting csv file
pybank = os.path.join("Resources", "budget_data1.csv")

#lists
months = []
profit_loss = []
change = []

#variables
months = 0
profit_loss = 0


with open('pybank', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
   
    #The total number of months included in the dataset
    for row in csv_reader: 
       temp.append(postag(row))

    for i in range(1, len(profit_loss)):
        change.append((int(profit_loss[i]) - int(profit_loss[i-1])))

    print(f"Financial Analysis")
    print("-" * 26)
    print(f"Total Months: {len(list(months))}")
    print(f"Total: ${sum(profit_loss)}")
    print(f"Average Change: ${round(sum(change) / len(change), 2)}")
    print(f"Greatest Increase in Profits: {months[25]} (${max(change)})")
    print(f"Greatest Decrease in Profits: {months[44]} (${min(change)})")


    #The net total amount of "Profit/Losses" over the entire period
    
        


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes




#The greatest increase in profits (date and amount) over the entire period




#The greatest decrease in profits (date and amount) over the over the entire period


#print commands
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _")
print("Total Months: ")
print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profit: ")





#create text file of analysis