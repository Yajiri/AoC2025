import unittest
from pathlib import Path
from solution import invalid_ids

file = Path(__file__).parent / ".." / "inputs" / "input2.txt"

class testDay2(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(invalid_ids(file), 56660955519, "The answer is wrong")
        print("The total sum is:", invalid_ids(file)) #just here to see what the acctual answer is


if __name__ == "__main__":
    unittest.main()