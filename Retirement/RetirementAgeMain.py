from Retirement import CalculateRetirementDate, CalculateRetirementAge, BirthYearValidation, BirthMonthValidation


def main():
    print("Social Security Full Retirement Age Calculator\n")
    year = input("Enter year of birth or press Enter to exit: ")
    while True:
        if year == '':
            break
        while not BirthYearValidation.birth_year_validation(year):
            year = input("\nEnter year of birth or press Enter to exit: ")
        if year == '':
            break
        month = input("Enter month of birth: ")
        while not BirthMonthValidation.birth_month_validation(month):
            month = input("\nEnter month of birth: ")
        retirement_age_year, retirement_age_month = CalculateRetirementAge.calculate_retirement_age(int(year))
        retirement_date = CalculateRetirementDate.calculate_retirement_date(int(year), int(month),
                                                                            retirement_age_year, retirement_age_month)
        print("Your full retirement age is " + str(retirement_age_year) + " and " + str(retirement_age_month)
              + " months.")
        print("This will be in", retirement_date.strftime("%B of %Y."))
        year = input("\nEnter year of birth or press Enter to exit: ")


main()
