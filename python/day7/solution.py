from pathlib import Path

def beam_splitter(file):
    grid = []

    with open(file, "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    for i in range(cols):
        if grid[0][i] == 'S':
            #print("S can be found at (0,", i, ")", sep="")

            grid[1][i] = '|'

            #print("".join(grid[1]))

    for r in range(rows - 1):
        for c in range(cols):
            if grid[r][c] == '|':
                if grid[r+1][c] =='^':
                    if c > 0:
                        grid[r+1][c-1] = '|'
                    if c + 1 < cols:
                        grid[r+1][c+1] = '|'
                    count += 1
                    continue
                elif grid[r+1][c] == '.':
                    grid[r+1][c] = '|'
    return count

if __name__ == "__main__":
    file = file = Path(__file__).parent / ".." / "inputs" / "input7.txt"
    print("The beam splits", beam_splitter(file), "amount of times")
