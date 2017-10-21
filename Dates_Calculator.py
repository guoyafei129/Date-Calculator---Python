# Yafei Guo
# MF703 HW7

class Date:
    '''a class defintion for a Date.'''
    
    def  __init__(self, new_month, new_day, new_year):
        '''the constructor for Date objects.'''
        self.month = new_month
        self.day = new_day
        self.year = new_year
        
    def __repr__(self):
        ''' return a string representation of this object.'''
        return '%.2d/%.2d/%.4d' %(self.month, self.day, self.year)  
    
    def copy(self):
        ''' returns a newly-constructed object of type Date with the same month, 
           day, and year that the called object has. 
        '''
        return Date(self.month, self.day, self.year)
    
    def __eq__(self, other):
        ''' returns True if the called object (self) and the argument (other) 
        represent the same calendar date (i.e., if the have the same values for 
        their day, month, and year attributes). Otherwise, this method should 
        return False.
        '''        
        return self.month == other.month and self.day == other.day and self.year == other.year
    
    def is_leap_year(self):
        ''' returns True if the called object is in a leap year, and False otherwise. 
        '''
        if self.year % 400 ==0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        else:
            return False
        
    def is_valid_date(self):
        '''returns True if the object is a valid date, and False otherwise.
        '''
        if self.month in range(1,13):
            if self.month in [1, 3, 5, 7, 8, 10, 12] and self.day in range(1,32):
                return True
            elif self.month in [4, 6, 9, 11] and self.day in range(1,31):
                return True
            elif self.month == 2 and self.is_leap_year() == True and self.day in range (1,30):
                return True
            elif self.month == 2 and self.is_leap_year() == False and self.day in range (1,29):
                return True
        return False
                
    def add_one_day(self):
        '''changes the called object so that it represents one calendar day 
           after the date that it originally represented.
        '''
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day < days_in_month[self.month] and self.is_leap_year() == False:
            self.day += 1
        elif self.day == 28 and self.is_leap_year() == True:
            self.day += 1 
        elif self.month < 12 or (self.day > 28 and self.is_leap_year() == True):
            self.day = 1
            self.month += 1
        else:
            self.day = 1
            self.month = 1
            self.year += 1
            
    def rem_one_day(self):
        '''changes the called object so that it represents one calendar day 
           before the date that it originally represented. 
        '''
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True and self.day == 1 and self.month == 3 :
            self.day = 29
            self.month -= 1 
        elif self.day == 1 and self.month != 1:
            self.day = days_in_month[self.month-1]
            self.month -= 1
        elif self.day == 1 and self.month ==1:
            self.day = 31
            self.month = 12
            self.year -= 1
        else:
            self.day -= 1
    
    def add_n_days(self, n):
        ''' changes the calling object so that it represents n calendar days 
            after the date it originally represented.
        '''
        for i in range(n):
            self.add_one_day()
            
    def rem_n_days(self, n):
        ''' changes the calling object so that it represents n calendar days 
            before the date it originally represented.
        '''        
        for i in range(n):
            self.rem_one_day()
    
    def is_before(self, other):
        '''returns True if the called object represents a calendar date that 
           occurs before the calendar date that is represented by other.
        '''
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        return False
    
    def is_after(self, other):
        ''' returns True if the calling object represents a calendar date that 
            occurs after the calendar date that is represented by other.
        '''
        return self != other and not self.is_before(other)
        
    def diff(self, other):
        '''returns an integer that represents the number of days between self and other.
        '''
        n = 0
        self_copy = self.copy()
        while self_copy.is_before(other):
            self_copy.add_one_day()
            n -= 1
        while self_copy.is_after(other):
            self_copy.rem_one_day()
            n += 1
        return n
        
    def day_of_week(self):
        '''returns a string that indicates the day of the week of the Date object that calls it. 
        '''
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        date0 = Date(10,16,2017)  # a known Monday
        if self.is_before(date0):
            return day_of_week_names[-date0.diff(self) % 7]
        else:
            return day_of_week_names[self.diff(date0) % 7]        
    
    def __lt__(self, other):
        ''' returns True if self comes before other, and False otherwise.
        '''
        return self.is_before(other)
    
    def __gt__(self, other):
        ''' returns True if self comes after other, and False otherwise.
        '''        
        return self.is_after(other)
    
    def __add__(self, n):
        '''overload the arithmetic + operator.
        '''
        if type(n) != int:
            print('Operator + is only defined for Date and int.')
            return None
        copy = Date(self.month, self.day, self.year)
        copy.add_n_days(n)
        return copy
    
    def __sub__(self, n):
        '''overload the arithmetic - operator.
        '''        
        if type(n) != int:
            print('Operator - is only defined for Date and int.') 
            return None
        copy = Date(self.month, self.day, self.year)
        copy.rem_n_days(n)
        return copy
    
    def __iadd__(self, n):
        '''overload the arithmetic += operator.
        '''    
        if type(n) != int:
            print('Operator += is only defined for Date and int.')     
            return None
        self.add_n_days(n)
        return self
        
    def __isub__(self, n):
        '''overload the arithmetic -= operator.
        '''    
        if type(n) != int:
            print('Operator -= is only defined for Date and int.')     
            return None
        self.rem_n_days(n)  
        return self
    
if __name__ == '__main__':    
    ## Task 1
        
    # 1.    
    d1=Date(10,17,2017)
    print(d1)
    
    d1 = Date(1, 1, 2017)
    d2 = d1
    d3 = d1.copy()
    print(id(d1))
    print(id(d2))
    print(id(d3))
    print(d1==d2)
    print(d1==d3)
    
    # 2.
    d1 = Date(1, 1, 2000)
    print(d1.is_leap_year())
    d2 = Date(1, 1, 1900)
    print(d2.is_leap_year())
    
    # 3.
    print('# 3.')
    d1 = Date(10,7,2017)
    print(d1.is_valid_date())
    d2 = Date(14,2,2017)
    print(d2.is_valid_date())
    d3 = Date(2,30,2017)
    print(d3.is_valid_date())
    d4 = Date(2,29,2016)
    print(d4.is_valid_date())
    d5 = Date(2,29,2017)
    print(d5.is_valid_date())
    d6 = Date(-4,-4, -5)
    print(d6.is_valid_date())
    d7 = Date(2,29,1900)
    print(d7.is_valid_date())
    
    # 4.
    d = Date(12, 31, 2017)
    print(d)
    d.add_one_day()
    print(d)
    d = Date(2, 28, 1900)
    d.add_one_day()
    print(d)
    d.add_one_day()
    print(d)
    
    # 5.
    print('# 5.')
    d = Date(1,1, 2017)
    print(d)
    d.rem_one_day()
    print(d)
    d = Date(3,1, 1900)
    d.rem_one_day()
    print(d)
    d = Date(3,1, 2016)
    d.rem_one_day()
    print(d)
    d.rem_one_day()
    print(d)
    d = Date(10,19,2017)
    d.rem_one_day()
    print(d)
    
    # 6.
    print('# 6.')
    d = Date(10, 17, 2017)
    d.add_n_days(3)
    print(d)
    d = Date(10, 17, 2017)
    d.add_n_days(0)
    print(d)
    
    # 7.
    print('# 7.')
    d = Date(10, 17, 2017)
    d.rem_n_days(500)
    print(d)
    d = Date(10, 17, 2017)
    d.rem_n_days(0)
    print(d)
    
    # 8.
    print('# 8.')
    d1 = Date(1, 1, 2018)
    d2 = d1
    d3 = d1.copy()
    print(id(d1))
    print(id(d2))
    print(id(d3))
    print(d1==d2)
    print(d1==d3)
    
    # 9.
    print('# 9.')
    ny = Date(1, 1, 2018)
    d = Date(10, 17, 2017)
    print(ny.is_before(d))
    print(d.is_before(ny))
    print(d.is_before(d))
    d3 = Date(12,31,2017)
    print(d3.is_before(ny))
    d4 = Date(12,31,2018)
    print(d4.is_before(ny))
    
    # 10.
    print('# 10.')
    ny = Date(1, 1, 2018)
    d = Date(10, 17, 2017)
    print(ny.is_after(d))
    print(d.is_after(ny))
    print(d.is_after(d))
    d3 = Date(12,31,2017)
    print(d3.is_after(ny))
    d4 = Date(12,31,2018)
    print(d4.is_after(ny))
    
    # 11.
    print('# 11.')
    d1 = Date(10, 17, 2017)
    d2 = Date(4, 16, 2018)
    print(d2.diff(d1))
    print(d1.diff(d2))
    print(d1)
    print(d2)
    d3 = Date(12, 1, 2015)
    d4 = Date(3, 15, 2016)
    print(d4.diff(d3))
    #print(Date(7, 4, 1776).diff(Date(1, 1, 2100)))   #-118154
    
    
    # 12.
    d = Date(4, 16, 2017)
    print(d.day_of_week())   # Sunday
    print(Date(1, 1, 2100).day_of_week())  # Friday
    print(Date(7, 4, 1776).day_of_week())  # Thursday
        
    ## Task 2        
    # 1.
    d1 = Date(4, 16, 2018)
    d2 = Date(10, 17, 2017)
    print(d1 < d2)
    print(d2 < d1)
    print(d1 > d2)
    print(d2 > d1)
    
    # 2.
    d1 = Date(10, 17, 2017)
    d2 = d1 + 181
    print(d1)
    print(d2)
    d3 = d2 - 181
    print(d3)
    
    # 3.
    d1 = Date(10, 17, 2017)
    d1 += 181
    d1
    d1 -= 181
    d1
    d = Date(1,1,2017)
    d += 1
    print(d)
    d += 1.2
## end of unit test code