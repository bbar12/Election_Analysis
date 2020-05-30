# import csv and OS modules 
import csv
import os
#Assign a variable for the file to load and the path
file_to_load=os.path.join('election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function.
   file_reader = csv.reader(election_data)
#Prints the header row 
   headers=next(file_reader)
   print(headers)
 # Print each row in the CSV file.
 #   for row in file_reader:
 #       print(row)

# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
#Writing some data to the file
#    txt_file.write("Counties in the Election")
#    txt_file.write("\n___________________________")
#writing each of these in separate lines
#    txt_file.write("\nArapahoe\nDenver\nJefferson")


# Total number of votes cast

# A complete list of candidates who received votes

# Total number of votes each candidate received

# Percentage of votes each candidate won

# The winner of the election based on popular vote