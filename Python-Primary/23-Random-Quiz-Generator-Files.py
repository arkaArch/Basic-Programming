# Creates quizzes with questions and answers in random order, along with the answer key.

import random

capitals_of_states_and_ut = {'Andhra Pradesh': 'Amaravati',
                             'Arunachal Pradesh': 'Itanagar',
                             'Assam': 'Dispur',
                             'Bihar': 'Patna',
                             'Chhattisgarh': 'Raipur',
                             'Goa': 'Panaji',
                             'Gujarat': 'Gandhinagar',
                             'Haryana': 'Chandigarh',
                             'Himachal Pradesh': 'Shimla',
                             'Jharkhand': 'Ranchi',
                             'Karnataka': 'Bengaluru',
                             'Kerala': 'Thiruvananthapuram',
                             'Madhya Pradesh': 'Bhopal',
                             'Maharashtra': 'Mumbai',
                             'Manipur': 'Imphal',
                             'Meghalaya': 'Shillong',
                             'Mizoram': 'Aizawl',
                             'Nagaland': 'Kohima',
                             'Odisha': 'Bhubaneswar',
                             'Punjab': 'Chandigarh',
                             'Rajasthan': 'Jaipur',
                             'Sikkim': 'Gangtok',
                             'Tamil Nadu': 'Chennai',
                             'Telangana': 'Hyderabad',
                             'Tripura': 'Agartala',
                             'Uttar Pradesh': 'Lucknow',
                             'Uttarakhand': 'Dehradun',
                             'West Bengal': 'Kolkata',
                             'Andaman and Nicobar Islands': 'Port Blair',
                             'Chandigarh': 'Chandigarh',
                             'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
                             'Lakshadweep': 'Kavaratti',
                             'Delhi': 'New Delhi',
                             'Puducherry': 'Puducherry',
                             'Ladakh': 'Leh',
                             'Jammu and Kashmir(summer)': 'Srinagar',
                             'Jammu and Kashmir(winter)': 'Jammu'}      # 37 key-value pair

# Generate 35 quiz files:
for quiz_num in range(35):
    # Create the quiz and answer key files
    quiz_file = open(f'capitals_quiz_{quiz_num + 1}.txt', 'w')  # open the file in write mode
    answer_key_file = open(f'capitals_quiz_{quiz_num + 1}_ans.txt', 'w')
    # Write out the header for the quiz
    quiz_file.write('Name:\n\nDate\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')
    # Shuffle the order of the states and uts
    states_and_uts = list(capitals_of_states_and_ut.keys())
    random.shuffle(states_and_uts)

    # Loop through all 37 states and uts, making a question for each.
    for question_num in range(37):
        correct_answer = capitals_of_states_and_ut[states_and_uts[question_num]]
        # To get three wrong answers first we have to copy all capitals into a list
        possible_answers = list(capitals_of_states_and_ut.values())
        # Second delete the right answer from the list
        del possible_answers[possible_answers.index(correct_answer)]
        # Now randomly get three wrong answers from the possible_answers and store it a list
        wrong_answers = random.sample(possible_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
    
        # Write the question and the answer options to the quiz file
        quiz_file.write(f'{question_num + 1}. What is the capital of {states_and_uts[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')
    
        # Write the answer key to the answer_key_file
        answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
    
    quiz_file.close()
    answer_key_file.close()




