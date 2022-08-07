# import the package
import csv
import os
# setwd
# os.chdir("/Users/xenialiu/Desktop/SMU_Data_Camp/Homework/Challenage3Python/python-challenge")

###################################################################################################
####################################         PyPoll        ########################################
###################################################################################################

file2 = os.path.join('Resources','election_data.csv')


# read the second dataset pyroll_data
with open(file2, 'r') as csvfile2:
	pypoll_data = csv.reader(csvfile2, delimiter = ',')
	# print header
	pypoll_data_header = next(pypoll_data)
	#print(f"CSV Header: {pypoll_data_header}")
	# print each row of the data after the header
	
	# create the function for calculate percentage
	def perc_func(x,y):
		result = round((x/y)*100,3)
		return result

	# set a count as scalar
	total = 0
	CCS = 0
	DD = 0
	RAD = 0

	# create a empty list to save the name of candidates 
	candidates = []

	for row in pypoll_data:
		# The total number of votes cast
		total += 1
		# A complete list of candidates who received votes
		if row[2] not in candidates:
			name = row[2]
			candidates.append(name) 
        # The total number of votes each candidate won
		if row[2] == candidates[0]:
			CCS += 1
		elif row[2] == candidates[1]:
			DD += 1
		else:
			RAD += 1
		# The percentage of votes each candidate won
		CCS_perc = perc_func(CCS,total)
		DD_perc = perc_func(DD,total)
		RAD_perc = perc_func(RAD,total)
		# The winner of the election based on popular vote.
		if CCS_perc > DD_perc:
			winner = candidates[0]
			winner_perc = CCS_perc
		else:
			winner = candidates[1]
			winner_perc = DD_perc
		if winner_perc > RAD_perc:
			winner = winner
		else: 
			winner = candidates[2]



# print the results
print(f"Election Results\n------------------------------ \nTotal Votes: {total}\n------------------------------ \n{candidates[0]}: {CCS_perc}% ({CCS})\n{candidates[1]}: {DD_perc}% ({DD})\n{candidates[2]}: {RAD_perc}% ({RAD})\n------------------------------ \nWinner: {winner}\n------------------------------\n" )


# output the second datasets
file2 = os.path.join('analysis','election_data_output.txt')


with open(file2, 'w') as txtfile2:
	txtfile2.write(f"Election Results\n------------------------------ \nTotal Votes: {total}\n------------------------------ \n{candidates[0]}: {CCS_perc}% ({CCS})\n{candidates[1]}: {DD_perc}% ({DD})\n{candidates[2]}: {RAD_perc}% ({RAD})\n------------------------------ \nWinner: {winner}\n------------------------------\n")











