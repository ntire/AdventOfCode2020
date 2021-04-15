
def find_xmas_mismatch(data, preamble):
    for i in range(preamble, len(data)):
        if not is_sum_of_two(data[i], data[i-preamble:i]):
            return data[i]        
    return None

def is_sum_of_two(target_sum, data):
    # print("Data: {} could sum up to {}?".format(data, target_sum))
    for i in range(len(data) - 1):
        for j in range( i + 1, len(data)):
            if data[i] + data[j] == target_sum:
                return True
    return False 

def find_contiguous_range(target_sum, data):

    for i in range(len(data)):
        result_range = list()
        exceeds_target_sum = False
        j = i
        while not exceeds_target_sum:
            #print("Range: {} for sum {}".format(result_range, target_sum))
            if sum(result_range) > target_sum:
                exceeds_target_sum = True
            elif sum(result_range) == target_sum:
                exceeds_target_sum = True
                return result_range
            else:
                result_range.append(data[j])
                j += 1
    return None

def find_encryption_weakness(data, preamble):
    first_mismatch = find_xmas_mismatch(data, preamble)

    c_range = find_contiguous_range(first_mismatch, data)

    return min(c_range) + max(c_range)
