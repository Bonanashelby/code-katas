"""Remove the time.

best practice jking06 & others 

def shorten_to_date(long_date):
    return long_date.split(',')[0]
"""


def shorten_to_date(long_date):
    shorten_date = long_date.split(',')
    return shorten_date[0]
