from datetime import date, timedelta
from abc import ABCMeta, abstractmethod

class MySupper(metaclass=ABCMeta):
    def delegate(self):
        self.action()
        
    @abstractmethod
    def action(self):
#         pass
        raise NotImplementedError('action method NOT implemented in subclass')

class MyDate(date):
    '''
    A custom date class for my personal use. Inherit from datetime.date class
    '''
    _wkday = [
        'Monday',   #date.weekday(): 0 is Monday 
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
        ]        
    
    def __new__(cls, year=0, month=0, day=0, name='andy'):
        '''date is immutable, so NO modify after created. Initialization is in __new__, NOT in __init__'''         
#         today_date = super().today()    #WARNING: cause recursive loop
        today_date = date.today()
        ayear = year if year else today_date.year
        amonth = month or today_date.month
        aday = (day, today_date.day)[day == 0]
#         if (year, month, day) == (0, 0, 0):
#             adate = date.today()
#         else:
#             adate = date(year, month, day)         
        return super().__new__(cls, ayear, amonth, aday)
    
    def __add__(self, value):
        super_add = super().__add__(value)
#         return self.__class__(super_add.year, super_add.month, super_add.day) # OR using type()
        return type(self)(super_add.year, super_add.month, super_add.day)

    '''
    Extreme warning here
    '''       
    def __init__(self, *args):
        self.wkday_name = self._wkday[self.weekday()]
        sp = super()
        print(sp.__thisclass__, sp.__self__, sp.__self_class__)
        super().__init__(*args)
            
    def date_incr(self, startdate, incr):
        try:
            incr_date = startdate + timedelta(days=incr)
        except Exception as e:
            print(e)
        else:
            return incr_date
    
    def _action(self):
        print('test delegation inheritant')
        
if __name__ == '__main__':
    adate = MyDate(1999, 9, 9)
    print(adate, adate.wkday_name)
#     incr_7 = adate.date_incr(adate, 1)
    print(MyDate.__mro__)
       
#     print(incr_7, incr_7.wkday_name)
#     adate.delegate()
