import csv

# File path for the CSV
file_path = "budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Open and read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        # Extract date and profit/loss
        date = row[0]
        profit = int(row[1])
        
        # Update totals
        total_months += 1
        net_total += profit
        dates.append(date)
        
        # Calculate change from the previous month
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            
            # Check for greatest increase/decrease
            if change > greatest_increase["amount"]:
                greatest_increase = {"date": date, "amount": change}
            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}
        
        # Update previous profit for the next iteration
        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
