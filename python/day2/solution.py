from pathlib import Path

def invalid_ids(file):
    with open(file, "r") as f:
        line = f.read().strip()

    ranges = [
        tuple(map(int, token.split("-")))
        for token in line.split(",")
    ]

    invalidNumberValue = 0

    for start, end in ranges:
        for n in range(start, end +1):
            s = str(n)
            if len(s) %2 == 0:
                half = len(s) // 2 
                if s[:half] == s[half:]:
                    #print(n)
                    invalidNumberValue += n
    return invalidNumberValue

if __name__ == "__main__":
    file = Path(__file__).parent / ".." / "inputs" / "input2.txt"
    print("The total sum of all are:", invalid_ids(file))