from datetime import datetime, date, time, timedelta


def date_in_future(integer):
    try:
        current_date = datetime.now()
        future_date = current_date + timedelta(days=integer)
        return (future_date.strftime("%d-%m-%Y %X"))
    except TypeError:
        return (current_date.strftime("%d-%m-%Y %X"))

# TEST
# date_in_future(2)
# date_in_future([])
