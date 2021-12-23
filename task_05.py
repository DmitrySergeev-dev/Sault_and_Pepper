from datetime import datetime, date, time, timedelta


def date_in_future(integer):
    try:
        current_date = datetime.now()
        future_date = current_date + timedelta(days=integer)
        print(future_date.strftime("%d-%m-%Y %B %X"))
    except TypeError:
        print(current_date.strftime("%d-%m-%Y %B %X"))


# TEST
date_in_future(2)
date_in_future([])
