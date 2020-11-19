def calculate_retirement_age(year_of_birth):
    if year_of_birth <= 1937:
        retirement_year = 65
        retirement_month = 0
    elif 1937 < year_of_birth < 1943:
        retirement_year = 65
        retirement_month = abs(1937 - year_of_birth) * 2
    elif 1943 <= year_of_birth <= 1954:
        retirement_year = 66
        retirement_month = 0
    elif 1954 < year_of_birth < 1960:
        retirement_year = 66
        retirement_month = abs(1954 - year_of_birth) * 2
    else:
        retirement_year = 67
        retirement_month = 0

    return retirement_year, retirement_month
