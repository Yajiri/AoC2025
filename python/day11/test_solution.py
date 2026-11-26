import unittest
from pathlib import Path
from solution import main

file = Path(__file__).parent.parent / "inputs" / "input11.txt"

class TestDay11(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(main(file), 566, "The answer is wrong")
        print(main(file))

if __name__ == "__main__":
    unittest.main()