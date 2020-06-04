"""
Program: hello_world.py
Author: Paul Ford
Last date modified: 06/2/2020

The purpose of this program is to say
Hello World.
"""
# Constant variable for months
MONTHS_CONVERSION = 12


def convert_to_months(years):
    """Converts years that is gathered in main
    and returns months"""
    months = years * MONTHS_CONVERSION
    return months
def test():
    print('Test')


if __name__ == '__main__':
    age_in_years = int(input('Please enter the age of the infant (1-5): '))
    months = convert_to_months(age_in_years)
    print("The infant is " + str(months) + " months old!")
    
