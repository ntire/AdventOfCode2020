from joltage.joltage_adapter import retrieve_joltage_array, determine_voltage_distribution

def test_examples_input():
    joltages = retrieve_joltage_array('input_example')
    assert 11 == len(joltages)

    jdis = determine_voltage_distribution(joltages)

    assert 7 == jdis[0] # 1-jolts
    assert 0 == jdis[1] # 2-jolts
    assert 5 == jdis[2] # 3-jolts

def test_larger_example():
    joltages = retrieve_joltage_array('input_larger_example')
    assert 31 == len(joltages)

    jdis = determine_voltage_distribution(joltages)

    assert 22 == jdis[0] # 1-jolts
    assert 0 == jdis[1] # 2-jolts
    assert 10 == jdis[2] # 3-jolts
