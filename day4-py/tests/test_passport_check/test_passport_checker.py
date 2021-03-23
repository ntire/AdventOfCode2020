from passport_check.passport_checker import extract_passports, count_valid_passports

def test_has_4_passports():
    f = "input_test"
    passports = extract_passports(f)
    assert 4 == len(passports)

def test_has_2_valid_passports():
    f = "input_test"
    no_of_valid_passports = count_valid_passports(f)
    assert 2 == no_of_valid_passports
