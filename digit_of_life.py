date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Your Digit of Life is: " + date)


# Lab 2.5.9 - The Digit of Life
#
# Purpose:
# Calculate the Digit of Life using the digits of a birthday.
#
# Assumptions:
# 1. The user enters a birthday containing exactly 8 digits.
# 2. The date can be entered as YYYYMMDD, YYYYDDMM, or MMDDYYYY.
# 3. The order of the digits does not affect the result.
# 4. The program adds all the digits of the date.
# 5. If the sum contains more than one digit, the process repeats.
# 6. The final result must be a single digit.
# 7. The program checks the input format, not whether
#    the date is a real calendar date.
#
# Tracing:
# 1. Ask the user to enter their birthday.
# 2. Check whether the input contains exactly 8 digits.
# 3. Display an error message if the format is invalid.
# 4. Otherwise, repeat while the date has more than one digit.
# 5. Initialize the_sum to zero.
# 6. Iterate through every digit in the date.
# 7. Convert each digit to an integer and add it to the_sum.
# 8. Print the current date or intermediate sum.
# 9. Convert the sum back into a string.
# 10. Repeat until only one digit remains.
# 11. Print the final Digit of Life.