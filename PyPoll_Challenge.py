# import csv and OS modules 
import csv
import os
#Assign a variable for the file to load and the path
file_to_load=os.path.join('Resources','election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Total vote counter set to 0 to accumulate
total_votes=0

#Candidate options list
candidate_options=[]
#county options list
county_options=[]

#empty dictionary for compiling candidate votes
candidate_votes={}
#county votes dictionary
county_votes={}

#String that holds county name that had the largest turnout
largest_turnout=" "
largest_county_votes=0
largest_county_percentage=0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function.
   file_reader = csv.reader(election_data)
#Prints the header row 
   headers=next(file_reader)
 
 # Print each row in the CSV file.
   for row in file_reader:
      #Add to the total vote count
      total_votes += 1
#Print the candidate name from each row
      candidate_name=row[2]
      county_name=row[1]
# Add the candidate name to the list
      if candidate_name not in candidate_options:
         #Add it to the list of candidates.
         candidate_options.append(candidate_name)
         #begin tracking that candidate's vote count
         candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] +=1

      if county_name not in county_options:
         #Adding to the list of counties
            county_options.append(county_name)
            #tracking each county's vote count
            county_votes[county_name] = 0
      county_votes[county_name] += 1

#Printing total votes
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
   election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n")
   print(election_results, end="")
    # Save the final vote count to the text file.
   txt_file.write(election_results)

#For loop to obtain votes for each candidate and get the percentage of votes
   for candidate in candidate_votes:
      votes=candidate_votes[candidate]
      #calculating percentage of votes for each candidate
      vote_percentage=(votes/total_votes)*100
      #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
      candidate_vote_summary=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
      #Print to the terminal
      print(candidate_vote_summary)
      txt_file.write(candidate_vote_summary)

# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
      if (votes > winning_count) and (vote_percentage > winning_percentage):
# 2. If true then set winning_count = votes and winning_percent =
# vote_percentage.
         winning_count = votes
         winning_percentage=vote_percentage
# 3. Set the winning_candidate equal to the candidate's name.
         winning_candidate= candidate  

#Candidate winning summary
   winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
   print(winning_candidate_summary)
   txt_file.write(winning_candidate_summary)

#for loop for identifying county names and counting votes per county, also calculating percentages
   for county in county_votes:
      votes_c=county_votes[county]
      percentage_bycounty=(votes_c/total_votes)*100
# To do: print out each county's name, vote count, and percentage of
# votes to the terminal.
      print(f"{county}: {percentage_bycounty:.1f}% ({votes_c:,})\n") 
      county_results=(f"{county}: {percentage_bycounty:.1f}% ({votes_c:,})\n")
         #  Save the results to our text file.
      txt_file.write(county_results)

# 2. If statement where if true then set largest_county_votes = votes_c and largest_county_percentage =
# percentage_bycounty.
      if (votes_c > largest_county_votes) and (percentage_bycounty > largest_county_percentage):
         largest_county_votes = votes_c
         largest_county_percentage=percentage_bycounty
# 3. Set the largest turnout string equal to the county's name.
         largest_turnout= county

#Largest turnout by county summary variable:
   largest_turnout_summary = (
      f"-------------------------\n"
      f"County with largest voter turnout: {largest_turnout}\n"
      f"-------------------------\n")
   print(largest_turnout_summary)
   txt_file.write(largest_turnout_summary)





