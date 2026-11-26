import unittest
from pathlib import Path
from solution import main

file = Path(__file__).parent.parent / "inputs" / "input10.txt"

class TestDay10(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main(file), 417, "This answer is wrong")
        print(main(file))

if __name__ == "__main__":
    unittest.main()