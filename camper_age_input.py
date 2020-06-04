MONTHS_CONVERSION = 12


def convert_to_months(years):
    months = years * MONTHS_CONVERSION
    return months


if __name__ == '__main__':
    age_in_years = int(input('Please enter the age of the infant (1-5): '))
    convert_to_months(age_in_years)
