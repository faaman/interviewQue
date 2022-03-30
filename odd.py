from datetime import datetime
from os import getcwd

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute ->", right_this_minute, "seems a little odd.")
else:
    print("Not an odd minute.")

# gets us the current working directory
where_am_I = getcwd()
print(where_am_I)

person1 = {'Name': 'Jane Austen',
           'Gender': 'Female',
           'Occupation': 'Author',
           'When': 'The 1800s'}
print(person1)
person1['Book1'] = 'P&P'
print(person1)
print(person1['Book1'])

