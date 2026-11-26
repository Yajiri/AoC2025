import unittest
from pathlib import Path
from solution import beam_splitter

file = file = Path(__file__).parent / ".." / "inputs" / "input7.txt"

class testDay7(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(beam_splitter(file), 1566, "The answer is wrong")
        print("the beam splits", beam_splitter(file), "amount of times")

if __name__ == "__main__":
    unittest.main()