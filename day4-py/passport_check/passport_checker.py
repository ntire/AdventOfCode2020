import re

def extract_passports(filename):
    passports = []
    current_passport = []
    with open(filename) as f:
        for line in f.readlines():
            if line != "\n":
                current_passport.append(line.rstrip("\n"))
            else:
                if len(current_passport) > 0:
                    passports.append(current_passport)
                current_passport=[]
        if len(current_passport) > 0:
            passports.append(current_passport) # Append last passports,since no \n is expected
    return passports


def count_passports_with_valid_field_count(filename):
    passports = extract_passports(filename)
    valid_passport_counter = 0
    
    for passport in passports:
        fields = {"byr": False, "iyr": False,"eyr": False, "hgt": False,
            "hcl": False, "ecl": False, "pid": False, "cid": False}
        
        # Verify which elements are contained in passport
        for line in passport:
            for key in fields.keys():
                fields[key] = fields[key] or key in line
        
        # Count all identified fields (ignore cid, since it's optional)
        identified_field_counter = 0
        for k in fields:
            if k != "cid" and fields.get(k) == True:
                # print("Found {}\n".format(k))
                identified_field_counter += 1

        if identified_field_counter >= 7:
            valid_passport_counter += 1    

    return valid_passport_counter

def count_passports_with_valid_fields(filename):
    passports = extract_passports(filename)
    valid_passport_counter = 0

    for passport in passports:
        is_valid_passport = True
        # print("\n")
        for line in passport:
            for token in line.split(" "):
                _id = token.split(":")[0]
                _val = token.split(":")[1]
                # print("Token ID: {}, token value: {}".format(token_id, token_value))
                if _id == "byr":
                    is_valid_passport = is_valid_passport and   (int(_val) >= 1920) and (int(_val) <= 2002)
                elif _id == "iyr":
                    is_valid_passport = is_valid_passport and   (int(_val) >= 2010) and (int(_val) <= 2020)
                elif _id == "eyr":
                    is_valid_passport = is_valid_passport and   (int(_val) >= 2020) and (int(_val) <= 2030)
                elif _id == "hgt":
                    unit = _val[-2:]
                    _val = _val[:-2]
                    if unit == "cm":
                        is_valid_passport = is_valid_passport and   (int(_val) >= 150) and (int(_val) <= 193)
                    elif unit == "in":
                        is_valid_passport = is_valid_passport and   (int(_val) >= 59) and (int(_val) <= 76)
                    else:
                        is_valid_passport = is_valid_passport and   False
                elif _id == "hcl":
                    is_valid_passport = is_valid_passport and   re.match("#[a-h0-9]{6}", _val) is not None
                elif _id == "ecl":
                    is_valid_passport = is_valid_passport and   _val in ["amb", "blu", "brn", "gry", "grn","hzl","oth"]
                elif _id == "pid":
                    is_valid_passport = is_valid_passport and   re.match("[0-9]{9}", _val) is not None
                # print("ID {} = {}, status = {}".format(_id, token.split(":")[1], is_valid_passport))
        
        if is_valid_passport:
            valid_passport_counter += 1    

    return valid_passport_counter

def count_passports_with_valid_fields_and_valid_count(filename):
    passports = extract_passports(filename)
    valid_passport_counter = 0

    for passport in passports:
        has_cid = False
        field_counter = 0
        is_valid_passport = True
        # print("\n")
        found_fields = set()
        for line in passport:
            for token in line.split(" "):
                _id = token.split(":")[0]
                _val = token.split(":")[1]
                if not _id in found_fields:
                    if _id == "cid":
                        field_counter += 1
                        has_cid = True
                    # print("Token ID: {}, token value: {}".format(token_id, token_value))
                    if _id == "byr":
                        is_valid_passport = is_valid_passport and   (int(_val) >= 1920) and (int(_val) <= 2002)
                        field_counter += 1

                    elif _id == "iyr":
                        is_valid_passport = is_valid_passport and   (int(_val) >= 2010) and (int(_val) <= 2020)
                        field_counter += 1

                    elif _id == "eyr":
                        is_valid_passport = is_valid_passport and   (int(_val) >= 2020) and (int(_val) <= 2030)
                        field_counter += 1

                    elif _id == "hgt":
                        unit = _val[-2:]
                        _val = _val[:-2]
                        if unit == "cm":
                            is_valid_passport = is_valid_passport and   (int(_val) >= 150) and (int(_val) <= 193)
                            field_counter += 1
                        elif unit == "in":
                            is_valid_passport = is_valid_passport and   (int(_val) >= 59) and (int(_val) <= 76)
                            field_counter += 1
                        else:
                            is_valid_passport = False
                    elif _id == "hcl":
                        is_valid_passport = is_valid_passport and   re.match("^#[a-f0-9]{6}$", _val) is not None
                        field_counter += 1

                    elif _id == "ecl":
                        is_valid_passport = is_valid_passport and   (_val in ["amb", "blu", "brn", "gry", "grn","hzl","oth"]) and (len(_val) == 3)
                        field_counter += 1

                    elif _id == "pid":
                        is_valid_passport = is_valid_passport and   re.match("^[0-9]{9}$", _val) is not None
                        field_counter += 1

                    # print("ID {} = {}, status = {}".format(_id, token.split(":")[1], is_valid_passport))
                    found_fields.add(_id)        
        if is_valid_passport and\
            ((field_counter == 8 and has_cid) or\
            (field_counter == 7 and not has_cid)):
            valid_passport_counter += 1    

    return valid_passport_counter