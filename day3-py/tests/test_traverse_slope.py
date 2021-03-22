from traverse.traverse import traverse_slope

# Based on knowledge from day 3, part 1
def test_traverse_slope31_with_test_input():
    f = 'input_test'
    assert traverse_slope(f, 3, 1) == 7

# Following tests based on knowledge from day 3, part 2

def test_traverse_slope11_with_test_input():
    f = 'input_test'
    assert traverse_slope(f, 1, 1) == 2

def test_traverse_slope51_with_test_input():
    f = 'input_test'
    assert traverse_slope(f, 5, 1) == 3

def test_traverse_slope71_with_test_input():
    f = 'input_test'
    assert traverse_slope(f, 7, 1) == 4

def test_traverse_slope12_with_test_input():
    f = 'input_test'
    assert traverse_slope(f, 1, 2) == 2

