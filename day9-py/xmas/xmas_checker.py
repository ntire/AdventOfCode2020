
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