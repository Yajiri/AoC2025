import unittest 
from pathlib import Path
from solution import largest_numbers

file = Path(__file__).parent / ".." / "inputs" / "input3.txt"

class testDay3(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(largest_numbers(file), 16927, "The answer is wrong")
        print(largest_numbers(file))

if __name__ == "__main__":
    unittest.main()