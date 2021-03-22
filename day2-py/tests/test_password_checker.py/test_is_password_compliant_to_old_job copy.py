from passwordchecker.check_old_job_policies import is_password_compliant

def test_non_compliant_password():
    assert is_password_compliant("1-3 b: cdefg") == False

def test_compliant_password():
    assert is_password_compliant("1-3 a: abcde") == True

def test_another_compliant_password():
    assert is_password_compliant("2-9 c: ccccccccc") == True