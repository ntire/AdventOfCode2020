from joltage.joltage_adapter import determine_joltages_possibilities, retrieve_joltage_array

# def test_4_possibilities():
#     joltages = [1, 4, 5, 6, 7]
#     p = determine_joltages_possibilities(joltages)
#     assert 4 == p

# def test_simple_example():
#     joltages = retrieve_joltage_array('input_example')
#     assert 8 == determine_joltages_possibilities(joltages)

def test_larger_example():
    joltages = retrieve_joltage_array('input_larger_example')
    assert 19208 == determine_joltages_possibilities(joltages)

# def test_in_a_row_4_possibilities():
#     joltages = [1, 2, 3, 4]
#     p = determine_joltages_possibilities(joltages)
#     assert 7 == p

# def test_two_possibilities():
#     joltages = [1, 2]
#     assert 2 == determine_joltages_possibilities(joltages)

# def test_one_possibility():
#     joltages = [1]
#     assert 1 == determine_joltages_possibilities(joltages)