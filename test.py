"""from datetime import datetime
from dateutil import relativedelta

date1 = datetime.strptime(str('2017-01-01'), '%Y-%m-%d')
date2 = datetime.strptime(str('2019-03-19'), '%Y-%m-%d')

difference = relativedelta.relativedelta(date2, date1)
months = difference.months
years = difference.years
# add in the number of months (12) for difference in years
months += 12 * difference.years
months"""
