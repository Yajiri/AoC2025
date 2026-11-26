from pathlib import Path

def trash_compactor(file):
    numbers = []
    operators = []
    lines = []
    finalResult = 0

    with open(file, "r") as f:
        for line in f:
            lines.append(line.strip())

    operators = list(lines[-1].split())

    for line in lines[:-1]:
        numbers.append([int(num) for num in line.split()])


    for col in range(len(operators)):
        if operators[col] == '*':
            result = 1

            for row in numbers:
                result *= row[col]

        if operators[col] == '+':
            result = 0
            for row in numbers:
                result += row[col]

        if operators[col] == '-':
            result = numbers[0][col]
            for row in numbers[1:]:
                result -= row[col]

        if operators[col] == '/':
            result = numbers[0][col]
            for row in numbers[1:]:
                result /= row[col]
            
        finalResult += result
    
    return finalResult

if __name__ == "__main__":
    file = file = Path(__file__).parent / ".." / "inputs" / "input6.txt"
    print("The total sum of all math problems is:", trash_compactor(file))