def is_leap_year(year):
    # Your code goes here
    # Implement the leap year check logic
    if year % 4 == 0:
        # If it's a century year (ending in 00)
        if year % 100 == 0:
            # Check if it's also divisible by 400
            return year % 400 == 0
        else:
            # If it's not a century year, it's a leap year
            return True
    else:
        # If not divisible by 4, it's not a leap year
        return False


# Test cases
print(is_leap_year(2020))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(2019))  # Expected output: False
