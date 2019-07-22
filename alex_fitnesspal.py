#GET THE DAY WITH THE INFO 
import myfitnesspal
client = myfitnesspal.Client('alexandrei1998@hotmail.it')
day = client.get_date(datetime.datetime.utcnow().year, datetime.datetime.utcnow().month,datetime.datetime.utcnow().day)

#---------------------------
#Get meals data 
print(day.meals)

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
print(day.exercises[0].get_as_list())

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

toda
print(day.exercises[1].get_as_list())

