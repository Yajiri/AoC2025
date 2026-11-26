from pathlib import Path
import re

def matches(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x != y:
            return False
    return True

def solve_and_return_best(target, buttons):
    best = float('inf')
    combinations = 1 << len(buttons)  

    for mask in range(combinations):
        state = [0] * len(target)
        presses = 0

        for button in range(len(buttons)):
            if mask & (1 << button):
                presses += 1
                for light in buttons[button]:
                    state[light] ^= 1

        if matches(state, target):
            best = min(best, presses)

    return best

def main(file):

    targets = []
    all_buttons = []

    with open(file, "r") as f:
        for line in f:
            line = line.strip()

            target_match = re.search(r"\[([.#]+)\]", line)

            if not target_match:
                continue

            target = [
                1 if c == "#" else 0
                for c in target_match.group(1)
            ]

            targets.append(target)

            buttons = []

            for button_text in re.findall(r"\((.*?)\)", line):
                button = [
                    int(x)
                    for x in button_text.split(",")
                ]
                buttons.append(button)
            all_buttons.append(buttons)

        total_value = 0

    for i in range(len(targets)):
        best = solve_and_return_best(targets[i], all_buttons[i])
        #print("Machine", i + 1, "requires", best, "presses")
        total_value += best

    return total_value

if __name__ == "__main__":
    file = Path(__file__).parent.parent / "inputs" / "input10.txt"
    main(file)
    print(f"Total value (sum of all best presses) = {main(file)}")