import time, random

numQuestions = 10
correctAnswers = 0

for question in range(numQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    for i in range(3):
        start = time.time()
        prompt = input("#{} What is {} x {} =".format(question+1, num1, num2))
        if prompt == str(num1*num2):
            end = time.time()
            if end - start > 8:
                print('To late')
                break
            correctAnswers+=1
            print('Correct!')
            time.sleep(1)
            break
        else:
            end = time.time()
            if end - start > 8:
                print('To late')
                break
            print('Try again')
            continue

print("You had {}/{} correct answers".format(correctAnswers, numQuestions))