"""
@author Vishal Dhiman
"""
import datetime 
from datetime import date
import  calendar

class Thurday:

    def isLastThursday(self,input_date):
        #convert string to date
        date_user=date.fromisoformat(input_date)
        
        #first check if day of date is thursday or not 
        if date_user.isoweekday() == 4:
            #using getLastThurday get date of last thursday of the month for given date
            date_last_Thursday=self.getLastThursday(date_user.month,date_user.year)
            if date_user.day==date_last_Thursday.day:
                return True
            
        return False

    def getLastThursday(self,input_month,year):
        
        #getting number of days in input month
        week_day,days_in_month=calendar.monthrange(year,input_month)

        #getting date of last day of month
        last_day_month = date(year,input_month,days_in_month)

        # From current last day of month finding most recent Thursday

        step_to_go_back = 4 - last_day_month.isoweekday()
        #if gap is of one week between last Thurday and last day of month

        if step_to_go_back > 0: 
            step_to_go_back -= 7                                 
        
        date_last_Thursday =last_day_month+datetime.timedelta(step_to_go_back)
        return date_last_Thursday  


def programMenu():
    obj_thu=Thurday()
    while(True):
        
        print("\n\n[OUT]: What you want to do? Choose Options")
        print("    (1) If you want to check if given date is last Thursday of a month,Then Enter 1")
        print("    (2) If you want to get last Thursday of given a month,Then Enter 2")
        n=int(input("\n[IN]: Enter option: "))

        if n==1:
            g_date=input("\n[IN]: Enter date: ([**]Date Format: 'YYYY-MM-'DD'): ")
            stat=obj_thu.isLastThursday(g_date)
            if stat:
                print("\n[OUT]: Status: {} \n\tThe given date {}  is of last Thursday of the month.".format(stat,g_date))
            else:
                print("\n[OUT]: Status: {} \n\tThe given date {}  is not of last Thursday of the month.".format(stat,g_date))          
        elif n==2:
            year=2019
            print("\n[INFO]: Default Year is 2019 if want to change year then after month, with space enter year also.")
            user_in=input("\n[IN]: Enter Month: ")           
            if len(list(user_in.split()))>1:
                month,year=map(int,user_in.split())
            else:
                month=int(user_in)
            print("\n\n[OUT]: The date of last Thursday of the month {} is: {}".format(month,obj_thu.getLastThursday(month,year)))
        else:
            print("\n[OUT]: OOPS!! Wrong Choice.")


        opt=input("\n\n[IN]: Want to go again? (yes/no): ")

        if not opt.lower()=="yes":
            break 

if __name__=="__main__":
    programMenu()
    
