import unittest
from pathlib import Path
from solution import red_tile_area

file = Path(__file__).parent.parent / "inputs" / "input9.txt"

class TestDay9(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(red_tile_area(file), 4759420470, "This answer is wrong")
        print(red_tile_area(file))

if __name__ == "__main__":
    unittest.main()