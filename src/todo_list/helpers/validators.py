def validate_date():
    from datetime import date

    current_year = date.today().year
    current_date = date.today()
    valid = False
    user_date = None

    while not valid:

        while True:
            year = int(input("Enter a year: "))

            if year < current_year:
                print("Enter a valid year\n")
            else:
                break

        while True:
            month = int(input("Enter a month: "))

            if month > 12 or month < 1:
                print("Enter a valid month\n")
            else:
                break

        while True:
            day = int(input("Enter a day: "))
            print()

            if day < 1 or day > 31:
                print("Enter a valid day\n")
            else:
                break

        user_date = date(year, month, day)

        if user_date < current_date:
            print("="* 50)
            print("Please enter a valid date".center(45))
            print("="* 50)
        else:
            valid = True

    return valid, user_date

