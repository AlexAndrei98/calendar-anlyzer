from calendarauto import main
from basil_counter import  count
from alex_fitnesspal import food_analysis
import datetime
import time
todays_tasks = main()
count(todays_tasks)
time.sleep(2)
food_analysis()

