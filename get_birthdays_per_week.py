from datetime import datetime, timedelta
from random import randint


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
birthdays = {weekday: [] for weekday in weekdays}

def get_birthdays_per_week(users):

    today = datetime.now().date()
    end_week = today + timedelta(weeks=1)
    str = ''
    str_weekend = ''

    for user in users:
        birthday = user['birthday'].date().replace(year=2023)
        if today <= birthday < end_week:
            weekday = weekdays[birthday.weekday()]
            birthdays[weekday].append(user['name'])

    # Print name for week
    while today < end_week:
        num_week = today.weekday()
        str_week = weekdays[num_week]
        today += timedelta(days=1)
        
        if len(birthdays[str_week]) == 0:
            continue
        elif num_week == 5 or num_week == 6:
            str_weekend += ', '.join(birthdays[str_week])
            continue
        elif num_week == 1:
            str_weekend = ''

        str += f"{str_week}: {', '.join(birthdays[str_week])}, {str_weekend}\n"
        
    print(str)    
     


# Array for test
users = []
name = ["Bill", "Jill", "Kim", "Jan", "Ann", "Jhon", "Tom", "James", "Robert", "Mary", "Patricia", "Jennifer" ]
for new_name in name:
    user = {
        'name': new_name, 
        'birthday': datetime(year=2000, month=5, day=randint(26,31))
    }
    users.append(user)

 
 
# Call main function 
get_birthdays_per_week(users)

