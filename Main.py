import os
import csv

month_count = []
profit = []
profit_changes= []





csvpath='/Users/Rosa/Desktop/PYTHON MODULE 3/Python-Challenge-3/Resources/budget_data.csv'

print(csvpath)

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')

# print(csvreader)

#read the header row first 
    csv_header=next(csvreader)
    print(f"csv header: {csv_header}")
    

    for row in csvreader:
    # we need to iterate our values that we have 
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_changes.append(profit[i-1]-profit[i])

# we need to see our max and min from our data list for our analysis  
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)


month_profit_increase = profit_changes.index(max(profit_changes))+1
month_profit_decrease = profit_changes.index(min(profit_changes))+1



# print out the results we need for our financial analysis 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change:{round(sum(profit_changes)/len(profit_changes),2)}")
print(f"Greatest Increase in Profits: {month_count[month_profit_increase]} (${(str(greatest_increase))}")
print(f"Greatest Decrease in Profits: {month_count[month_profit_decrease]} (${(str(greatest_decrease))}")


output="output.txt"
output = r'C:\Users\Rosa\Desktop\PYTHON MODULE 3\Python-Challenge-3\Analysis\output.txt'

with open(output, "w") as csvfile:
    new=csv.writer(csvfile)
    new.writelines("Financial Analysis")
    new.writelines("\n")
    new.writelines("---------------------")
    new.writelines("\n")
    new.writelines(f"Total Months:{len(month_count)}")
    new.writelines("\n")
    









