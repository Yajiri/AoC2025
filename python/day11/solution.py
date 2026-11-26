from pathlib import Path

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

def exists_in_parents(current, target):
    while current is not None:
        if current.name == target:
            return True
        current = current.parent
    return False

def search(current, graph):
    moves = graph.get(current.name)
    if moves is None:
        return
    for move in moves:
        if exists_in_parents(current, move):
            continue
        #Java: Node child = new Node(move, current)
        child = Node(move, current)
        current.children.append(child)
        search(child, graph)

def print_tree(node, depth):
    print(" " * depth + node.name)
    for child in node.children:
        print_tree(child, depth + 1)

def count_paths(node):
    if node.name == "out":
        return 1
    paths = 0
    for child in node.children:
        paths += count_paths(child)
    return paths

def main(file):
    grid = []

    with open(file, "r") as f:
        for line in f:
            grid.append(line.strip())

    start_point = "you"
    root = Node(start_point)

    graph = {}

    for line in grid:
        parts = line.split(":")
        if len(parts) != 2:
                    print("Invlaid line: ", line)
                    continue
        from_node = parts[0]

        moves = []
        for move in parts[1].split():
            moves.append(move)
        graph[from_node] = moves
    search(root, graph)
    print_tree(root, 0)
    return count_paths(root)

if __name__ == "__main__":
    file = Path(__file__).parent.parent / "inputs" / "input11.txt"
    print(main(file))