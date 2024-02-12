# Plinko odds Calculator

# This function finds the factorial of input 'x'
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

# function for getting the number of rows from the user, and ensuring the input is an integer.
def get_rows_input():
    while True:
        try:
            return int(input("How many rows: "))
        
        except ValueError:
            print("Your input must be a number, try again.")
    
# Start

print("--==-- Plinko Odds Calculator --==--\n")

# Get num of rows as input
rows = get_rows_input()

# State the number of buckets (same as rows)
print(f"\nThere are {rows} buckets.")

# List the bucket numbers
for i in range(rows):
    if i < rows-1:
        print(i, end=", ")
    else:
        print(i)

print("") ## just for new line

# Table Headers
seperator="-----------------------------------------"
print(seperator)
print("| Bucket |  Probability\t|  Fraction\t|")
print(seperator)

# Populate Table with data
for k in range(rows):
    n = rows-1

    # calculates probability of a ball landing in bucket 'k'
    p = factorial(n) / (factorial(k) * factorial(n - k) * (2**n))

    # convert probability to a percent with 4 decimal places
    percent = round(p * 100, 4)

    # print row
    #print("|  " + str(k) + "\t |  " + str(percent) + "%\t|  1/" + str(round(1/p, 4)) + "\t|")
    print(f"|  {k}\t |  {percent}%\t|  1/{round(1/p, 4)}\t|")

    print(seperator)


# This is so the cmd window doesn't close automatically
input("\npress Enter to close")
