import unittest
from pathlib import Path
from solution import junction_boxes

file = Path(__file__).parent / ".." / "inputs" / "input8.txt"

class TestDay8(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(junction_boxes(file), 57564, "The answer is wrong")

if __name__ == "__main__":
    unittest.main()