import datetime
from datetime import date

from dateutil import relativedelta


class Employee():

    def __init__(self, name, age, tenure):
        self.status = "Temporary"
        self.name = name
        '''self.DOB = datetime.date(DOB)
        self.join_date = datetime.date(join_date)'''
        self.age = age
        self.tenure = tenure
        '''today = date.today()
        months = 0
        self.age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        difference = relativedelta.relativedelta(self.join_date, today)
        months = difference.months
        years = difference.years
        # add in the number of months (12) for difference in years
        months += 12 * difference.years
        self.tenure = months'''

    def display(self):
        print("\n personal Details=", self.name, self.age, self.status)
