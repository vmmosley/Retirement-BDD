import datetime


def calculate_retirement_date(birth_year, birth_month, retirement_age_year, retirement_age_month):
    delta = datetime.timedelta(days=((retirement_age_year * 365) + ((retirement_age_month + 1) * 30.417)))
    retirement_date = datetime.date(birth_year, birth_month, 1) + delta
    return retirement_date
