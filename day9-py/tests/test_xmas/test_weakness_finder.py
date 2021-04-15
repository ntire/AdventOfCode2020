from xmas.xmas_checker import find_xmas_mismatch

def test_very_simple_example():
    data = [1, 2, 3, 4]
    first_mismatch = find_xmas_mismatch(data, 2)
    assert 4 == first_mismatch

def test_simple_example():
    f = "input_test"
    with open(f) as f:
        data = [int(i) for i in f.readlines()]

    first_mismatch = find_xmas_mismatch(data, 5)
    assert 127 == first_mismatch

