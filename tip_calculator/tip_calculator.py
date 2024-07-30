print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(
    input("What parcentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

num_percentage = tip / 100 * bill
total_bill = bill + num_percentage
num_split_bill = total_bill / people
print(f'Each person should pay: {round(num_split_bill)}')
