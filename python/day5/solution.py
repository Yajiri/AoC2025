from pathlib import Path

def fresh_items(file):
    ranges = []
    numbers = []

    reading_ranges = True
    numberOfFreshItems = 0

    with open(file, "r") as f:
        for line in f:
            line = line.strip()

            if not line: 
                reading_ranges = False
                continue

            if reading_ranges:
                start, end = map(int, line.split("-"))
                ranges.append((start, end))
            else:
                numbers.append(int(line))

        for number in numbers:
            fresh = False
            for start, end in ranges:
                if start <= number <= end:
                    fresh = True
                    numberOfFreshItems = numberOfFreshItems + 1
                    break

        return numberOfFreshItems
    
if __name__ == "__main__":
    file = file = Path(__file__).parent / ".." / "inputs" / "input5.txt"
    print("The total amount of fresh items are:", fresh_items(file))