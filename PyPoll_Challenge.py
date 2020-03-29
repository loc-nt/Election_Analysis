# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources\election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Declare variables:
# Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Declare a list of counties
county_list = []
# Declare an empty dictionary for counties:
county_votes = {}

# 2. Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Exlucle the header row from the count.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        ## CHALLENGE code:
        # Get the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county...
        if county_name not in county_list:
            # Add it to the list of counties.
            county_list.append(county_name)
            # 2. Begin tracking that candidate's vote count. 
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1
        ## End CHALLENGE code.


# 3. Save the results to our text file.
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

    # Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # County with largest turnout and Voters Count Tracker
    county_max = ""
    county_max_count = 0
    county_max_perc = 0

    ## CHALLENGE code:
    # Print headline first:
    county_results = (f"County Votes:\n")
    print(county_results)
    txt_file.write(county_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # 1. Iterate through the county list.
    for county in county_votes:
        # 2. Retrieve vote count of a county.
        c_votes = county_votes[county]
        # 3. Calculate the percentage of votes.
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        # To do: print out each county's name, vote count, and percentage of votes to the terminal.
        county_results = (f"{county}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        # Print each county, its voter count, and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)

        # Determine county_max
        # Determine if the votes is greater than the county_max_count.
        if (c_votes > county_max_count) and (c_vote_percentage > county_max_perc):
            # If true then set county_max_count = c_votes and c_vote_percentage = county_max_perc.
            county_max_count = c_votes
            county_max_perc = c_vote_percentage
            # And, set the county with highest turnout equal to the county's name.
            county_max = county

    # 4. The county with the highest turnout
    highest_turnout_summary = (
        f"-------------------------\n"
        f"Lardest Turnout County: {county_max}\n"
        f"-------------------------\n")
    print(highest_turnout_summary)
    # 5. Save the highest turnout county name to the text file.
    txt_file.write(highest_turnout_summary)
    ## End CHALLENGE code.


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    # 4. The winner of the election based on popular vote
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # 5. Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

