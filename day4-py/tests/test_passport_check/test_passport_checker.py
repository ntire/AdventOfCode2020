from passport_check.passport_checker import extract_passports, count_passports_with_valid_field_count, count_passports_with_valid_fields, count_passports_with_valid_fields_and_valid_count

def test_has_4_passports():
    f = "input_test"
    passports = extract_passports(f)
    assert 4 == len(passports)

def test_has_2_valid_passports():
    f = "input_test"
    no_of_valid_passports = count_passports_with_valid_field_count(f)
    assert 2 == no_of_valid_passports

def test_has_4_invalid_passports():
    f = "input_invalid"
    assert 4 == len(extract_passports(f))
    assert 0 == count_passports_with_valid_fields(f)

def test_has_4_valid_passports():
    f = "input_valid"
    assert 4 == len(extract_passports(f))
    assert 4 == count_passports_with_valid_fields(f)

def test_has_3_valid_passports_with_valid_count():
    f = "input_valid_count"
    assert 3 == count_passports_with_valid_fields_and_valid_count(f)
