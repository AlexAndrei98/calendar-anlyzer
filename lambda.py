from calendarauto import main
from basil_counter import  count
from alex_fitnesspal import food_analysis
from email_sender import sendemail
import datetime
import time

OUTPUT_STRING='Subject: Daily report for Alex\n\n'
todays_tasks,OUTPUT_STRING = main(OUTPUT_STRING)
OUTPUT_STRING = count(todays_tasks,OUTPUT_STRING)
time.sleep(2)
OUTPUT_STRING = food_analysis(OUTPUT_STRING)
print(OUTPUT_STRING)
sendemail(OUTPUT_STRING)



