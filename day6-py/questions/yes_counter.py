
def count_unique_answers_of_anyone(all_answers):
    unique_answers = set()
    for answer in all_answers:
        for item in answer:
            unique_answers.add(item)
    return len(unique_answers)