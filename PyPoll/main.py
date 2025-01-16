import csv

# File path for the CSV
file_path = "election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        # Extract candidate name from each row
        candidate = row[2]
        
        # Increment total vote count
        total_votes += 1
        
        # Increment the candidate's vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and determine the winner
winner = ""
max_votes = 0
results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    
    # Check for the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Sort results by votes (optional)
results.sort(key=lambda x: x[1], reverse=True)

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
