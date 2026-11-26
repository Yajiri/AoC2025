from pathlib import Path


def largest_numbers(file):
    total = 0
    with open(file, "r") as f:
            for line in f:
                stringOfCode = line.strip()

                if not stringOfCode:
                    continue
        
                largest = 0
                y = 0
                start_index = 0

                i = 0

                while i < len(stringOfCode) - 1:

                    #This is here to ensure that we break on the first 9
                    if stringOfCode[i] == '9':
                        largest = 9
                        start_index = i + 1
                        break

                    #If there is no 9 we'd still need to find the largest number    
                    if int(stringOfCode[i]) > largest:
                        largest = int(stringOfCode[i])
                        start_index = i + 1
                    i += 1

                #second loop, starting from the position just after the largest number we found.
                i = start_index

                while i < len(stringOfCode):
                    if int(stringOfCode[i]) > y:
                        y = int(stringOfCode[i])
                    i += 1
                value = largest * 10 + y
                total += value
 
    return total

if __name__ == "__main__":
    file = file = Path(__file__).parent / ".." / "inputs" / "input3.txt"
    print("The total sum is:", largest_numbers(file))