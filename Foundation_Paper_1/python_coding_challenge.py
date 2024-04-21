from datetime import datetime, date, timedelta
import math


def main():
    while True:
        dob = input("Please enter your birth date in DD/MM/YYYY format: ")
        try:
            dob_date_object = datetime.strptime(dob, '%d/%m/%Y')
            if dob_date_object:
                break
            else:
                print("Please enter a valid date in DD/MM/YYYY format.")
        except ValueError:
            print("Please enter a valid date in DD/MM/YYYY format")

    while True:
        theory = input("Have you passed your theory test? Yes/No: ")
        if theory.lower() == 'yes' or theory.lower() == 'no':
            break
        else:
            print("Please enter Yes or No: ")

    while True:
        drive_test = input("Have you passed your driving test? Yes/No: ")
        if theory.lower() == 'yes' or theory.lower() == 'no':
            break
        else:
            print("Please enter Yes or No: ")

    dob_as_datetime_object = datetime.strptime(dob, '%d/%m/%Y').date()
    age_in_days = age_calc(dob_as_datetime_object)
    age_in_years = age_in_days/365.25
    #print(age_in_years, type(age_in_years))
    #print(f"age_in_years is {age_in_years, type(age_in_years)}\n")
    seventeenth_birthday = dob_date_object + timedelta(days=(math.ceil(365.25*17)))
    seventeenth_birthday_as_str = datetime.strftime(seventeenth_birthday, '%d/%m/%Y')
    #print(f"seventeenth birthday is {seventeenth_birthday}")

    date_difference = datetime.today() - seventeenth_birthday
    # print(f"The date difference is {date_difference.days}")

    if age_in_years < 17:
        return f"Your request has been rejected as you are under the minimum age. You can reapply on "\
               f"{seventeenth_birthday_as_str} ({abs(date_difference.days)} days).\nThank you for using our service."

    if theory.lower() == 'no':
        return ("Your request has been rejected as you have not passed your theory. "
                "Thank you for using our service.")

    if drive_test.lower() == 'no':
        return "Your request has been rejected as you have not passed your driving test."

    return "Your licence is on its way!"

    #print(dob, theory, drive_test)


def age_calc(dob_as_datetime):
    age = date.today() - dob_as_datetime
    # print("Your age is: ", age.days, type(age.days))
    return age.days



if __name__ == '__main__':
    main()
