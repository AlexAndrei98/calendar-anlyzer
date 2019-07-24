#GET THE DAY WITH THE INFO 
import myfitnesspal
import datetime
def food_analysis(OUTPUT_STRING):
    client = myfitnesspal.Client('alexandrei1998@hotmail.it')
    day = client.get_date(datetime.datetime.now().year, datetime.datetime.now().month,datetime.datetime.now().day)
    #---------------------------
    #Get meals data 
    BREAKFAST = day.meals[0]
    LUNCH =  day.meals[1]
    DINNER = day.meals[2]
    SNACKS = day.meals[3]
    OUTPUT_STRING +="\n\nToday you ate the following:"

    if (len(BREAKFAST)>0):
        OUTPUT_STRING +="\nYou had a good BREAKFAST for calories: "+str(BREAKFAST.totals['calories'])
    else:
        OUTPUT_STRING +="\nBro you gotta eat some BREAKFAST"

    if (len(LUNCH)>0):
        OUTPUT_STRING +="\nYou had a good LUNCH for calories: "+str(LUNCH.totals['calories'])
    else:
        OUTPUT_STRING +="\nBro you gotta eat some LUNCH"

    if (len(DINNER)>0):
        OUTPUT_STRING +="\nYou had a good DINNER for calories: "+str(DINNER.totals['calories'])
    else:
        OUTPUT_STRING +="\nBro you gotta eat some DINNER"
    if (len(SNACKS)>0):
        OUTPUT_STRING +="\nYou had a good SNACKS for calories: "+str(SNACKS.totals['calories'])
    else:
        OUTPUT_STRING +="\nBro you gotta eat some SNACKS"
    """
    [<Breakfast {}>, 
    <Lunch {
        'calories': 455, 
        'carbohydrates': 26, 
        'fat': 1, 
        'protein': 5, 
        'sodium': 20, 
        'sugar': 3}>, 
    <Dinner {
        'calories': 949, 
        'carbohydrates': 34, 
        'fat': 35, 
        'protein': 46, 
        'sodium': 362, 
        'sugar': 6}>, 
    <Snacks {}>]
    """
    #Print Cardiovascular exercise 

    OUTPUT_STRING +="\n\nToday you did the following exercises: \n"
    if(len(day.exercises[0].get_as_list())>0):
        for ex in day.exercises[0].get_as_list():
            OUTPUT_STRING += ex['name'] + " for "+str(ex['nutrition_information']['minutes']) + ' minutes\n'
    """
    [
        {'name': 'Kickboxing (including Turbo Jam)', 
        'nutrition_information': 
            {'minutes': 53, 
            'calories burned': 231
            }
        }, 
        {'name': 'Apple Health App Workout', 
        'nutrition_information': 
            {'minutes': 10, 
            'calories burned': 155
            }
        }
    ]
    """
    #Print Strength exercise 
    if(len(day.exercises[1].get_as_list())>0):
        for ex in day.exercises[0].get_as_list():
            OUTPUT_STRING += ex['name'] + " for "+str(ex['nutrition_information']['minutes']) + ' minutes\n'



    return OUTPUT_STRING

