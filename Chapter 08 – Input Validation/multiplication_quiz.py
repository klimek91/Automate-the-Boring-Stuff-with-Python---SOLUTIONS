import pyinputplus as pyip
import random, time

numOfQuestions = 10
correctAnswers = 0

for questionNum in range(numOfQuestions):
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    prompt = "#{}: {} x {} =".format(questionNum+1, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes=["^{}$".format(num1*num2)], blockRegexes=[('.*', 'WRONG !!!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Out of time")
    except pyip.RetryLimitException:
        print("Out of tries")
    else:
        print("Correct")
        correctAnswers+=1
    time.sleep(1)
print("Score is {}/{}".format(correctAnswers,numOfQuestions))