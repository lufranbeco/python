people=int(input("Indicate the number of people who will pay: "))

check=float(input("Indicate the amount to be paid: "))

tip=float(input("Indicate the tip percentage: "))

total=(((check*tip)/100)+check)/people

print(f"The total amount per person is {total}")