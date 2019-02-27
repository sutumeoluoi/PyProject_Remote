from datetime import date, timedelta


class MyDate(date):
    '''
    A custom date class for my personal use. Inherit from datetime.date class
    '''
    
    def __new__(cls, year=0, month=0, day=0):
        '''date is immutable, so NO modify after created. Initialization is in __new__, NOT in __init__'''
        if (year, month, day) == (0, 0, 0):
            adate = date.today()
        else:
            adate = date(year, month, day)
        return super().__new__(cls, adate.year, adate.month, adate.day)
       
#     def __init__(self, year=0, month=0, day=0):
#         if (year, month, date) == (0, 0, 0):
#             adate = date.today()
#         else:
#             adate = date(year, month, day)
#         super().__init__(adate.year, adate.month, adate.day)
            
    def date_incr(self, startdate, incr):
        try:
            incr_date = startdate + timedelta(days=incr)
        except Exception as e:
            print(e)
        else:
            return incr_date
    
if __name__ == '__main__':
    adate = MyDate()
    print(adate.today())
    incr_7 = adate.date_incr(adate.today(), 7)
       
    print(incr_7)
