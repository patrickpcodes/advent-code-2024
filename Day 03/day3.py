import re

def readInList(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Initialize empty lists for each column
        data = []

        # Read each line in the file
        for line in file:
            data.append(line)
            # Split the line by whitespace
            # rowSData = line.strip().split()
            # # Append the values to the respective lists
            # # rowData =[]
            # # for i in rowSData:
            # #     rowData.append(int(i))
            # data.append(rowSData)
    return data


def extract_pattern(line):
    # Compile a regular expression pattern that disallows spaces
    # print(line)
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    # Find all matches in the line
    matches = pattern.findall(line)
    return matches


data = readInList('../files/day3-mul.txt')

total = 0
# print(data)
print(len(data))
for i in range(len(data)):
    matches = extract_pattern(data[i])
    # print(matches)
    for j in range(len(matches)):
        total += int(matches[j][0])* int(matches[j][1])

print(total)