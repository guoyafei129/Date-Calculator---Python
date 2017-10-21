# Yafei Guo
# MF703 HW7

from a7task1 import Date

def options_expiration_days(year):
    '''returns a list of all of the Dates on which options expire during a calendar year.
    '''
    days=[]
    months=[]
    for month in range(1,13):
        for day in range(15,22):  # the third week
            if Date(month,day,year).day_of_week() == 'Friday':
                days+=[day]
        months+=[month]
    return [Date(months[i], days[i], year) for i in range(0,12)]

print(options_expiration_days(2017))
print(options_expiration_days(2018))

def market_holidays(year):
    if Date(1,1,year).day_of_week() == 'Sunday':
        nyd = Date(1,2,year)      
    else:
        nyd = Date(1,1,year)
    print("New Year's Day is observed on", nyd.day_of_week(), nyd)
    
    for day in range(15,22): # the third week
        if Date(1,day,year).day_of_week() == 'Monday':
            mlkd = Date(1,day,year)   
        if Date(2,day,year).day_of_week() == 'Monday':
            pd = Date(2,day,year) 
    print("Martin Luther King Day is observed on", mlkd.day_of_week(), mlkd)
    print("President's Day is observed on", pd.day_of_week(), pd)
    
    for day in range(1,32):  # in May
        if Date(5,day,year).day_of_week() == 'Monday':
            md = Date(5,day,year)  # update till the last Monday in May
    print("Memorial Day is observed on", md.day_of_week(), md) 
    
    if Date(7,4,year).day_of_week() == 'Sunday':
        ind = Date(7,5,year)      
    else:
        ind = Date(7,4,year)
    print("Independence Day is observed on", ind.day_of_week(), ind)
    
    for day in range(1,8):  # the first week:
        if Date(9,day,year).day_of_week() == 'Monday':
            lbd = Date(9,day,year)
    print("Labor Day is observed on", lbd.day_of_week(), lbd) 
    
    for day in range(22, 29):  # the forth week:
        if Date(11,day,year).day_of_week() == 'Thursday':
            tgd = Date(11,day,year)
    print("Thanksgiving Day is observed on", tgd.day_of_week(), tgd) 
    
    if Date(12,25,year).day_of_week() == 'Sunday':
        cmd = Date(12,26,year)      
    else:
        cmd = Date(12,25,year)
    print("Christmas Day is observed on", cmd.day_of_week(), cmd)    
            
    
    return [nyd, mlkd, pd, md, ind, lbd, tgd, cmd]
        
print(market_holidays(2017))
print(market_holidays(2018))

