
import unittest

def main(finput):
    expenses = []
    
    # 1. Read input file line by line
    with open(finput) as f:
        for line in f.readlines():
            expenses.append(int(line))

    for i in range(len(expenses) - 2):
        for j in range (i + 1, len(expenses) - 1):
            for k in range (j + 1, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k]== 2020:
                    print("Found {} + {} + {} = 2020".format(expenses[i], expenses[j], expenses[k]))
                    return expenses[i] * expenses[j] * expenses[k]
    return 0

class Test(unittest.TestCase):
    
    def test_expenses(self):
        result = main("day1/test_input.txt")
        self.assertEqual(result, 241861950, "Should be 241861950")

if __name__ == "__main__":
    is_test = False # Change 

    if is_test:
        unittest.main()
    else:
        # main program
        result = main("day1/input.txt")
        print(result) # Answer: 212428694

