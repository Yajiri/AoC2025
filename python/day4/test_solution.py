import unittest 
from pathlib import Path
from solution import remove_paper

file = Path(__file__).parent / ".." / "inputs" / "input4.txt"

class testDay4(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(remove_paper(file), 1587, "This answer is wrong")
        print(remove_paper(file))

if __name__ == "__main__":
    unittest.main()