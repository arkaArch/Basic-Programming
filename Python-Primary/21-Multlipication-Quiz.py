import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answer = 0

for question in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = "Q:%s: %s x %s = " % (question + 1, num1, num2)

    try:
        # Right answer is handeled by allow_regex
        # Wrong answer is handeled by block_regex
        pyip.inputStr(prompt, allowRegexes = ['%s' % (num1 * num2)],
                                blockRegexes = [('.*', 'Incorrect!')],
                                timeout = 8, limit = 3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')

    else:   # Run if no exceptions were raised in try blocks
        print('Correct !')
        correct_answer += 1
    
    # Brief pause to let user see the result.
    time.sleep(1)

print('Score: %s out of %s' % (correct_answer, number_of_questions))
