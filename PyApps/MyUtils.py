from datetime import date, timedelta
from abc import ABCMeta, abstractmethod


def printnl(*args: 'unlimited arguments') -> 'separate each args with "\n"':
    '''print each item in args list per line'''
#     st = '{}\n'*(len(args))
#     print(st.format(*args), end='') #default print() end with '\n', specify end= to overwrite it
    print(*args, sep='\n')


class MyInfo:
    def __init__(self):
        self.name = 'Andy'
        self.status = 'married'

#===============================================================================
# class MySupper(metaclass=ABCMeta):
#     def delegate(self):
#         self.action()
#         
#     @abstractmethod
#     def action(self):
# #         pass
#         raise NotImplementedError('action method NOT implemented in subclass')
#===============================================================================

'''
CPython there are two special type:
_ <slot wrapper> Which (at least) wraps a C-implemented function. Behaves like an <unbound method> in CPython 2
    (at least sometimes) or a <function> in CPython 3
_ <method-wrapper> Which wraps a C-implemented function as an bound method. Instances of this type
    have an __self__ attribute__ which is used as first argument when it is called
datetime.date.__init__: <slot wrapper '__init__' of 'object' objects>. So, this init is unbound of object.__init__
n_date = date.today()
n_date.__init__: <method-wrapper '__init__' of datetime.date object at 0x00B36CC8>. So, it is 
    bound of datetime.date.__init__ and self
Caution @property: assign to n_date.wkday_name works. it creates instance's attr 'wkday_name' and exist parallel
    to @property wkday_name. But call n_date.wkday_name still return value of @property wkday_name. i.e., @property
    isn't shadowed by instance attr. However, assign through class as MyDate.wkday_name = ... will destroy @property
    and the instance attr wkday_name will hide the latest MyDate.wkday_name non_@property value.
    (Read pg 609 - Fluent Python)
'''
class MyDate(date):
    '''
    A custom date class for my personal use. Inherit from datetime.date class
    
    Attributes:
        year = 0: year YYYY
        month = 0: month MM
        day = 0: day DD
        wkday_name: 'Monday', 'Tuesday',...
    
    Defaults: MyDate() create using today date
    '''
    __version__ = '1.0.0'
    _wkday = [
        'Sunday',   #fry_weekday: Sunday = 0
        'Monday',   
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        ]     
      
    '''
    __new__ is staticmethod, so NO require self or cls instance as first arg, so no auto-bound cls on instance. However, it was design to ask for a
        n instance of class(cls) which created by type() in 1st argument . Thus, super() return instance, but call from it still need passing instance 
        such as 'cls'. Other instance method will auto-bound when using super()
    Note: call today_date = super().today() in this __new__causes recursive loop.
    Explanation: super().today() is super(MyDate, cls). cls is object of MyDate(NOT instance of MyDate) create by type()
                super() found today() in datetime.date and call it. This today() calls fromtimestamp()
                and return cls(...) as below snips from datetime.py implementation of date class.
                The issue is the final cls is not date class. We are still in scope of MyDate due to inheritant,
                so the final cls is still MyDate class object. I.e, final cls(...) equivalent MyDate(...).
                Thus, it calls this __new__ again and cause cursive loop.
    Fix: call directly date.today() guarantee the final cls(...) in fromtimestamp is date(...), so it is fine.
    @classmethod
    def fromtimestamp(cls, t):        
        return cls(y, m, d)

    @classmethod
    def today(cls):        
        t = _time.time()
        return cls.fromtimestamp(t)
    '''
    def __new__(cls, year=0, month=0, day=0):
        '''date is immutable, so NO modify after created. Initialization is in __new__, NOT in __init__'''         
#         today_date = super().today()    #WARNING: cause recursive loop
#         print(super(), super().today)
        today_date = date.today()
        ayear = year if year else today_date.year
        amonth = month or today_date.month
        aday = (day, today_date.day)[day == 0]
    
        return super(MyDate, cls).__new__(cls, ayear, amonth, aday) #__new__ is staticmethod, so NO auto-bound cls on instance
    

    '''
    Extreme warning here!!!:
    super().__init__(*args): no need self since super() return super obj. it auto-bound self.
    date.__init__(self, *args): need self since calling through date class __init__ is consider as normal function.
    Both give error: TypeError: object.__init__() takes no parameters because date.__init__ is a slot wrapper of object.__init__. 
        It calls object.__init__ passes in 'self' while object.__init__ doesn't accept any arg.
        date.__init__ is <slot wrapper '__init__' of 'object' objects>
    __init__ is instance method. So, super().__init__() is auto-bound 'self' in it like other instance method
    
    ***Peculiar Note!!!: date.__init__ is actually object.__init__(self) no argurment, so something peculiar here
    1. date.__init__('huh', 'why', 5, 7, 9, 8) or date.__init__(*args) - NO ERROR
    2. as long as 'self' in 1st arg such as date.__init__(self, 'huh', 'why', 5, 7, 9, 8) or date.__init__(self, *args) - always ERROR
    3. super().__init__('huh') or super().__init__(*args): as long as having at least 1 arg - always ERROR
    4. date.__init__(self) - NO ERROR
    5. super().__init__() - NO ERROR
    Explanation: 
    _ 4 and 5 is same: 4 calls from class so need self, 5 calls from instance so NO need self.
    _ 1 no error because without self date.__init__ turn into normal function. So, 'huh' pass to self and args[0] to self. Since object.__init__ does nothing,
        so although value passing to self is not an instant, it doesn't error.
    _ 2 and 3 need explanation
    '''       
    def __init__(self, *args):
        self._wkday_name = self._wkday[self.frys_weekday()]
#         print('MyDate init: ', *args)
        
#         super(MyDate, self).__init__(self, *args)  #date.__init__ is object.__init__ so no arg
        date.__init__('huh', 'why', 5, 7, 9, 8) 
            
    def __add__(self, value):
        '''overwrite add() of parent class''' 
        a_value = timedelta(days=value)
        super_add = super().__add__(a_value)
#         return self.__class__(super_add.year, super_add.month, super_add.day) # OR using type()
        return type(self)(super_add.year, super_add.month, super_add.day)
    
    def __radd__(self, value): 
        '''overwrite radd() of parent class'''   
        a_value = timedelta(days=value)
        super_add = super().__radd__(a_value)
#         return self.__class__(super_add.year, super_add.month, super_add.day) # OR using type()
        return type(self)(super_add.year, super_add.month, super_add.day)
    
    def __getitem__(self, ix):
        '''Return value through index
        
        Args:
            ix: index number to access value. Only 2 items.
        Returns:
            string date or weekday name depends on ix.
        Raises:
            IndexError: if ix reach outside of 2 items.
        '''        
        try:
            aItem = (str(self), self.wkday_name)[ix]
        except IndexError as e:
            raise IndexError("Index is out of bound. There is only 2 items")
        else:
            return aItem        
    
    def __len__(self):
        '''return number of items to use with index access'''
        return 2
    
    def __repr__(self):
        '''Overwrite the represent of in instance call'''
        return  '{}({}, {}, {}, {})'.format(self.__class__.__name__,
                                            self.year,
                                            self.month,
                                            self.day, 
                                            self.wkday_name,
                                            )
    
    def __str__(self):
        '''Overwrite print output'''
        return '{}, {}'.format(super().__str__(), self.wkday_name)
        
    def frys_weekday(self):
        '''frys: Sun(0) - Sat(6)'''
        return self.toordinal() % 7
        
    def date_adj(self, adj):
        '''add arbitrary days. Adding negative number equivalent to subtract
        
        Args:
            adj: number of day to add
        Returns:
            date corresponding to added date
        '''
        try:
            if isinstance(self, MyDate):
                a_date = self + adj
            else:
                a_date = self + timedelta(days=adj)
        except Exception as e:
            print(e)
        else:
            return a_date
    
    def find_wkday(self, dayname):
        '''Return date from weekday name. Minimum 2-char name require
        
        Args:
            dayname: name of weekday. At least 2 chars length
        Returns:
            date within the week corresponding to 'self'
        Raises:
            ValueError: if dayname is not valid name of weekday
        '''
        dayname = dayname.title().strip()
        
        if len(dayname) < 2:
            raise ValueError('string is too short. need at least 2 chars')
        
#         if any(item.startswith(dayname) item from _wkday):
        for i, item in enumerate(self._wkday):
            if item.startswith(dayname):
                i = i if i < 6 else -1
                delta = i - self.frys_weekday()                                
                break
        else:
            raise ValueError('It is not valid weekday name')    
                
        return self + timedelta(days=delta) 
        
    ''' 
    3 ways to manipulate class attributes acess: @property, descriptor, modify __getattribute__
    Note: every attribute access calls __getattribute__, ONLY attribute can't find anywhere __getattr__ will called
    '''
    @property
    def wkday_name(self):   #getter
        '''property getter. wk_name is Monday - Sunday'''
        return self._wkday_name
    
    '''or using __setattr__ as a different way to alter attribute write'''
    '''Note: assigning MyDate.__dict__[wkday_name] = ... will allow assignment and destroy property'''
    @wkday_name.setter
    def wkday_name(self, value):
        '''property setter'''
        raise AttributeError('wkday_name is read-only')
#         self._wkday_name = value

    '''
    as say above. This alter attribute _wkday to non_written state. However, this only work on instance access
    Assign from class still work and overwrite _wkday such as MyDate._wkday = 'Oops, you are overwritten'
    Note: DON'T use setattr(self, name, value) in else clause. It'll cause recursive loop because setattr() calls
        self.__setattr__ again. Call as below,  or object.__setattr__, 
        or throuh __dict__ as self.__dict__[name]. (name is str var since [] requre quote-string)
    '''
    def __setattr__(self, name, value):
        '''override setattr to set _wkday read only'''
        if name == '_wkday':
            raise AttributeError('_wkday is read only. Can\'t assign value')
        else:
#             super().__setattr__(name, value)  #Or below. Both works
            self.__dict__[name] = value #handle other attr as reg.
    
    #===========================================================================
    # def _action(self):
    #     print('test delegation inheritant')
    #===========================================================================
class Foo:
    __slots__ = ('_bar',)
    
    def __new__(cls):    
        self = super().__new__(cls)
        self._bar = 'barz'
        return self
        
    @property
    def bar(self):
        return self._bar

        
if __name__ == '__main__':
    adate = MyDate(2019, 3, 3)
    orgdate = date.today()
#     print(adate, adate.wkday_name)
    print(repr(adate))
    print(repr(orgdate))
#     adate_n = adate.date_adj(2)
#     orgdate_n = MyDate.date_adj(orgdate, 2)
#     print(repr(adate_n))
#     print(repr(orgdate_n))
    print(repr(4 + adate))
    print(adate + 4)    
#     print(adate.date_adj(adate, -3)[0])
#     print(adate + 3)
#     print(MyDate.__mro__)
 
#     print(adate.find_wkday('Tue'), adate.find_wkday('su'))
#     adate.delegate()
#     me = MyInfo()
#     printnl(MyInfo.__init__, me.__init__)

    #===========================================================================
    # f = Foo()
    # print(f._bar)
    # printnl(vars(Foo))
    #===========================================================================
    