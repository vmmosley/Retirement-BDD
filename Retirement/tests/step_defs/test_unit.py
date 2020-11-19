from pytest_bdd import scenarios, parsers, given, when, then
from Retirement.BirthYearValidation import birth_year_validation
from Retirement.BirthMonthValidation import birth_month_validation
from Retirement.CalculateRetirementAge import calculate_retirement_age
from Retirement.CalculateRetirementDate import calculate_retirement_date

EXTRA_TYPES = {
    'Number': int,
    'String': str,
}
CONVERTERS = {
    'year': str,
    "r_month": int,
    "r_age": int,
    "month": str,
    "r_date": str,
}
scenarios('../features/unit.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('the user enters "{year:String}" for the birth year', extra_types=EXTRA_TYPES))
@given('the user enters "<year>" for the birth year')
def year_input(year):
    return birth_year_validation(year)


@when(parsers.cfparse('the "{year:String}" is tested for validity', extra_types=EXTRA_TYPES))
@when('the "<year>" is tested for validity')
def year_check(year):
    if year_input(year):
        return True
    else:
        return False


@then(parsers.cfparse('the program will continue to run is the "{year:String}" is valid', extra_types=EXTRA_TYPES))
@then('the program will continue to run is the "<year>" is valid')
def year_valid(year):
    response = True
    assert response == year_check(year)


@then(parsers.cfparse('the program finds the input invalid and should return an error message for '
                      'that "{year:String}"', extra_types=EXTRA_TYPES))
@then('the program finds the input invalid and should return an error message for that "<year>"')
def year_invalid(year):
    response = False
    assert response == year_check(year)


@given(parsers.cfparse('the user puts "{month:String}" for the birth month', extra_types=EXTRA_TYPES))
@given('the user puts "<month>" for the birth month')
def month_input(month):
    return birth_month_validation(month)


@when(parsers.cfparse('the "{month:String}" is checked if it is a valid input', extra_types=EXTRA_TYPES))
@when('the "<month>" is checked if it is a valid input')
def month_check(month):
    if month_input(month):
        return True
    else:
        return False


@then(parsers.cfparse('the program should continue to run if "{month:String} is valid', extra_types=EXTRA_TYPES))
@then('the program should continue to run if "<month>" is valid')
def month_valid(month):
    response = True
    assert response == month_check(month)


@then(parsers.cfparse('the program should return an error message if "{month:String}" is '
                      'invalid', extra_types=EXTRA_TYPES))
@then('the program should return an error message if "<month>" is invalid')
def month_invalid(month):
    response = False
    assert response == month_check(month)


@then(parsers.cfparse('the program should get the retirement age "{r_age:Number}" and retirement '
                      'month of "{r_month:Number}" for the year "{year:String}"', extra_types=EXTRA_TYPES))
@then('the program should get the retirement age "<r_age>" and retirement '
      'month of "<r_month>" for the year "<year>"')
def year_calc(r_age, r_month, year):
    age = -1
    month = -1
    if year_check(year):
        age, month = calculate_retirement_age(int(year))
    assert (age, month) == (r_age, r_month)


@given(parsers.cfparse('the user inputs both "{year:String}" and "{month:String}"', extra_types=EXTRA_TYPES))
@given('the user inputs both "<year>" and "<month>"')
def user_input(year, month):
    if year_check(year):
        if month_check(month):
            return True
        else:
            return False
    else:
        return False


@when(parsers.cfparse('both "{year:String}" and "{month:String}" return as valid', extra_types=EXTRA_TYPES))
@when('both "<year>" and "<month>" return as valid')
def user_validation(year, month):
    if user_input(year, month):
        return True
    else:
        return False


@then(parsers.cfparse('the program will use the add {year:String} to retiring age and {month:String} to retiring month '
                      'to find the "{r_date:String}"', extra_types=EXTRA_TYPES))
@then('the program will add "<year>" to retiring age and "<month>" to retiring month to find the "<r_date>"')
def date_calc(year, month, r_date):
    age_year, age_month = calculate_retirement_age(int(year))
    retiring_date = calculate_retirement_date(int(year), int(month), age_year, age_month).strftime("%B of %Y")
    assert retiring_date == r_date

