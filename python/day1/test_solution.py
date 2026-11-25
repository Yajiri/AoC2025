import unittest
from pathlib import Path
from solution import count_stops

file = Path(__file__).parent / ".." / "inputs" / "input1.txt"

class TestDay1(unittest.TestCase):

    def test_answer(self):
        #the comment is only printed if it fails.
        self.assertEqual(count_stops(file), 1102, "Day 1 solution returned the wrong answer")


if __name__ == "__main__":
    unittest.main()