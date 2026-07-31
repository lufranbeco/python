# Get the total number of people splitting the bill (converted to an integer)
people=int(input("Indicate the number of people who will pay: "))

# Get the total bill amount before tip (converted to a floating-point number)
check=float(input("Indicate the amount to be paid: "))

# Get the tip percentage from the user (converted to a floating-point number)
tip=float(input("Indicate the tip percentage: "))

# Calculate tip amount ((check * tip) / 100), add it to the bill (+ check), 
# and divide the grand total evenly among all people (/ people)
total=(((check*tip)/100)+check)/people

# Output the final amount each person owes, formatted to two decimal places ({total:.2f})
print(f"The total amount per person is {total:.2f}")