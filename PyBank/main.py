# import the package
import csv
import os
# setwd
# os.chdir("/Users/xenialiu/Desktop/SMU_Data_Camp/Homework/Challenage3Python/python-challenge")


###################################################################################################
####################################         PyBank        ########################################
###################################################################################################

# import the first datasets
file1 = os.path.join('Resources','budget_data.csv')

# read the first dataset pybank_data
with open(file1, 'r') as csvfile1:
	pybank_data = csv.reader(csvfile1, delimiter = ',')
	# print header
	pybank_data_header = next(pybank_data)
	# print each row of the data after the header
	#print(f"CSV Header: {pybank_data_header}")
	
	# set a counter  for total number and total amount 
	total_months = 0 
	total = 0
	# set a staring number for changes and greatest increase/decrease
	greatest_increase = -(999999)
	greatest_decrease = 9999999
	previous = 0

	for row in pybank_data:
		# The total number of months included in the dataset
		total_months += 1
		# The net total amount of "Profit/Losses" over the entire period
		total += int(row[1])
		# The changes in "Profit/Losses" over the entire period, and then the average of those changes
		if row[0] == "Jan-10":
			start = int(row[1])
		if row[0] == "Feb-17":
			end = int(row[1])
			average_change = round((end - start)/(total_months-1),2)
		# The greatest increase in profits (date and amount) over the entire period
		if int(row[1])-previous > greatest_increase:
			greatest_increase = int(row[1])-previous
			time_increase = row[0]
		# The greatest decrease in profits (date and amount) over the entire period
		if int(row[1])-previous < greatest_decrease:
			greatest_decrease = int(row[1])-previous
			time_decrease = row[0]
		previous = int(row[1])

# print the results
print(f"Financial Analysis\n-------------------------------------- \n\tTotal Month: {total_months}\n\tTotal: ${total}\n\tAverage Change:  ${average_change}\n\tGreatest Increase in Profits: {time_increase}  (${greatest_increase})\n\tGreatest Decrease in Profits: {time_decrease}  (${greatest_decrease})")

# output the first datasets
file2 = os.path.join('analysis','budget_data_output.txt')


with open(file2, 'w') as txtfile2:
	txtfile2.write(f"Financial Analysis\n-------------------------------------- \n\tTotal Month: {total_months}\n\tTotal: ${total}\n\tAverage Change:  ${average_change}\n\tGreatest Increase in Profits: {time_increase}  (${greatest_increase})\n\tGreatest Decrease in Profits: {time_decrease}  (${greatest_decrease})")
