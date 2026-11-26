import unittest
from pathlib import Path
from solution import trash_compactor

file = Path(__file__).parent / ".." / "inputs" / "input6.txt"

class testDay6(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(trash_compactor(file), 4580995422905, "The answer is wrong")
        print(trash_compactor(file))

if __name__ == "__main__":
    unittest.main()