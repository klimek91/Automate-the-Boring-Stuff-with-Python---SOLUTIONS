import random, os
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
    'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
    'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

os.makedirs(os.getcwd() + '\quiz', exist_ok=True)
path = os.getcwd() + '\quiz'

states = []
for keys in capitals:
    states.append((keys))


for i in range(35):
    file = open(path + '\quiz{}.txt'.format(i+1), 'w')
    file.write("Quiz number {}".format(i+1))
    file.write("\nName:\nSurname:\nClass:\nDate:\n")

    random.shuffle(states)
    for x in range(50):
        file.write("\n{}. What is capital of {}?\n".format(x+1,states[x]))
        good_answer = capitals[states[x]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(good_answer)]
        other_answers = random.sample(wrongAnswers,3)
        answers = other_answers + [good_answer]
        random.shuffle(answers)
        for y in range(4):
            file.write("{}. {}\n".format('ABCD'[y], answers[y]))
            if answers[y] == good_answer:
                answer = open(path + '\quiz{}_answer.txt'.format(i+1), 'a')
                answer.write("{}. {} {}\n".format(x+1,'ABCD'[y],good_answer))