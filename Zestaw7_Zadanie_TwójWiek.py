from datetime import datetime, date
def AskBD():
    date_now = date.today()
    user_BD = input("Enter your birthdate in a given format: DD-MM-RRRR: ").split("-")

    day, month, year = [int(elem) for elem in user_BD]
    BD = date(year, month, day)

    temp1 = date_now - BD
    tempint = int(temp1.days)
    years = int(tempint / 365)
    months = int((tempint-years*365)/30)
    days = int(tempint-years*365-months*30)
    print("It has been {} year/s, {} month/s and {} day/s since you were born".format(years,months,days))
AskBD()


