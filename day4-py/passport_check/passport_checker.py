
def extract_passports(filename):
    passports = []
    current_passport = []
    with open(filename) as f:
        for line in f.readlines():
            if line != "\n":
                current_passport.append(line)
            else:
                if len(current_passport) > 0:
                    passports.append(current_passport)
                current_passport=[]
        if len(current_passport) > 0:
            passports.append(current_passport) # Append last passports,since no \n is expected
    return passports


def count_valid_passports(filename):
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