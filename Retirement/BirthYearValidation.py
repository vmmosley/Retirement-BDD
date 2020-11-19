def birth_year_validation(year):
    try:
        year = int(year)
        if year < 1900 or year > 2020:
            print("Please try again. Year should be between 1900 and 2020")
            return False
        else:
            return True
    except ValueError:
        print("Value should be a number, Please try again")
        return False
