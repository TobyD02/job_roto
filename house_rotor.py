from datetime import datetime
import json
import smtplib, ssl

users = ['Toby', 'Leon', 'Ollie', 'Elena', 'James', 'Tom', 'Annie', 'Chloe']
mail_list = ['thetjdixon1234@gmail.com']

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

    mail(jobs)
    
    with open("jobs.json", "w") as f:
        x = json.dumps(jobs, indent=4)
        f.write(x)


def mail(message_object):
    port = 465
    with open("authentication.txt", "r") as f:
        password = f.read()

    sender = 'develop.tobyd@gmail.com'
    
    message ="""
    JOBS FOR {date}

    Dishwasher: {dishwasher}
    Bins: {bins}
    Sides: {sides}
    """.format(date=message_object['Dishwasher']['date'],
               dishwasher=message_object['Dishwasher']['person'],
               bins=message_object['Bins']['person'],
               sides=message_object['Sides']['person'])
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        for email in mail_list:        
            server.sendmail(sender, email, message)

#seed()
next_day()
