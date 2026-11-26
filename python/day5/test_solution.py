import unittest
from pathlib import Path
from solution import fresh_items

file = file = Path(__file__).parent / ".." / "inputs" / "input5.txt"

class testDay5(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(fresh_items(file), 607, "The answer is wrong")
        print(fresh_items(file))

if __name__ == "__main__":
    unittest.main()