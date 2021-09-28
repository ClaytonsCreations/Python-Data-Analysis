import os
import csv

#getting csv file
pybank = os.path.join("Resources", "budget_data1.csv")

#lists
months = []
profit_loss = []
change = []

#variables
month = 0
profit_loss = 0


with open(pybank) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
   
    #The total number of months included in the dataset
    for row in csv_reader: 
       months.append(row[0])
       print(months)

  


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