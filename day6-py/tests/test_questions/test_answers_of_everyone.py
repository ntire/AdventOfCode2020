from questions.yes_counter import count_unique_answers_of_everyone

def test_single_person():
    answers = ["abc"]
    assert 3 == count_unique_answers_of_everyone(answers)

def test_three_person_w_one_answer_each():
    answers = ["a", "b", "c"]
    assert 0 == count_unique_answers_of_everyone(answers)

def test_two_persons_w_two_answers_each():
    answers = ["ab", "ac"]
    assert 1 == count_unique_answers_of_everyone(answers)

def test_four_persons_w_one_similiar_answer_each():
    answers = ["a", "a", "a", "a"]
    assert 1 == count_unique_answers_of_everyone(answers)


