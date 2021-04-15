from xmas.xmas_checker import find_contiguous_range, find_encryption_weakness

def test_simple_range():
    with open ("input_test") as f:
        data = [int(i) for i in f.readlines()]

    result_range = find_contiguous_range(127, data)

    assert [15, 25, 47, 40] == result_range


def test_test_input_range():
    with open ("input_test") as f:
        data = [int(i) for i in f.readlines()]

    weakness = find_encryption_weakness(data, 5)
    assert 62 == weakness