from datetime import date, timedelta


class MyDate(date):
    '''
    A custom date class for my personal use. Inherit from date class
    '''
#     pass
    
    def __new__(cls, curdate = date.today()):
#         pass
        return super().__new__(cls, curdate.year, curdate.month, curdate.day)
        print(curdate)
        
    def __init__(self, curdate = date.today()):
        super().__init__()
        self.curdate = curdate
        
    def date_incr(self, startdate, incr):
        try:
            incr_date = startdate + timedelta(days=incr)
        except Exception as e:
            print(e)
        else:
            return incr_date
    
if __name__ == '__main__':
    adate = MyDate()
#     cur_date = date.today()
    print(adate.curdate)
    incr_7 = adate.date_incr(adate.curdate, 7)
       
    print(incr_7)
