from datetime import datetime
import json

users = ['Toby', 'Leon', 'Ollie', 'Elena', 'James', 'Tom', 'Annie', 'Chloe']


def seed():
    
    now = datetime.now()
    today = '{}/{}/{}'.format(now.strftime('%d'), now.strftime('%m'), now.strftime('%Y'))
    #today = '08/02/2022'
    
    jobs = {'Dishwasher': {'date': today, 'person': users[0]},
            'Sides': {'date': today, 'person': users[1]},
            'Bins': {'date': today, 'person': users[2]}}

    with open("jobs.json", "w") as f:
        x = json.dumps(jobs, indent=4)
        f.write(x)


def next_day():
    now = datetime.now()
    today = '{}/{}/{}'.format(now.strftime('%d'), now.strftime('%m'), now.strftime('%Y'))

    with open("jobs.json", "r") as f:
        jobs = json.loads(f.read())

    #1. Find how many days since last assignment
    #2. Based on that, increment person assigned to that job

    for i in jobs:
        date_object = datetime.strptime(jobs[i]['date'], '%d/%m/%Y')
        days_since = (now - date_object).days

        index = users.index(jobs[i]['person'])

        new_index = index + days_since
        if new_index >= len(users):
            new_index = new_index - len(users)

        new_person = users[new_index]

        jobs[i]['person'] = new_person
        jobs[i]['date'] = today

    with open("jobs.json", "w") as f:
        x = json.dumps(jobs, indent=4)
        f.write(x)


seed()
next_day()
