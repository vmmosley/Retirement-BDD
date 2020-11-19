def birth_month_validation(month):
    try:
        month = int(month)
        if month < 1 or month > 12:
            print("Please try again. month should be between 1 and 12")
            return False
        else:
            return True
    except ValueError:
        print("Value should be a number, Please try again")
        return False
