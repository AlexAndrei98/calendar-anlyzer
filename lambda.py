from calendarauto import main
todays_tasks = main()

TOTAL_COUNT=0

for task in todays_tasks:
    if(task.color == 4):
        TOTAL_COUNT+=1
print('TOTAL COUNT: '+str(TOTAL_COUNT))