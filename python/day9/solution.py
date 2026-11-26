from pathlib import Path

def red_tile_area(file):
    red_tiles = []

    with open(file, "r") as f:
        for line in f:
            line = line.strip()

            red_tile_row, red_tile_col = map(int, line.split(","))
            red_tiles.append((red_tile_row, red_tile_col))
            
    largest = 0

    for i in range(len(red_tiles)):
        for j in range((i + 1), len(red_tiles)):
            dx = abs(red_tiles[i][0] - red_tiles[j][0]) + 1
            dy = abs(red_tiles[i][1] - red_tiles[j][1]) + 1
            area = dx * dy

            largest = max(largest, area)

    return largest

if __name__ == "__main__":
    file = Path(__file__).parent.parent / "inputs" / "input9.txt"
    print("The largest grid has an area of:", red_tile_area(file))