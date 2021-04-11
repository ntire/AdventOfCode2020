
def count_unique_answers_of_anyone(all_answers):
    unique_answers = set()
    for answer in all_answers:
        for item in answer:
            unique_answers.add(item)
    return len(unique_answers)

def count_unique_answers_of_everyone(answer_group):
    # initialize
    counter = dict()
    for letter in range(26):
        counter[chr(ord('a') + letter)] = 0
    
    for single_person_answers in answer_group:
        for answer in single_person_answers:
            counter[answer] = counter.get(answer) + 1
    
    total_persons = len(answer_group)
    everyone_counter = 0
    for answer in counter.keys():
        if counter.get(answer) == total_persons:
            everyone_counter += 1

    return everyone_counter