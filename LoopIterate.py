# Loop Iterate and adding sum from all integers 1-50

# Initialize sum variable
Total_sum = 0

# Iterate through numbers from 1 to 50
for i in range(1, 51):  # range(1, 51) includes numbers from 1 to 50
    Total_sum += i  # Add the current number to the total sum

# Print the result
print(f"The sum of numbers from 1 to 50 is: {Total_sum}")