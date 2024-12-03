def readInList(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Initialize empty lists for each column
        left_column = []
        right_column = []
        
        # Read each line in the file
        for line in file:
            # Split the line by whitespace
            left, right = line.strip().split()
            # Append the values to the respective lists
            left_column.append(int(left))
            right_column.append(int(right))
    return left_column, right_column

# Call the function with the filename
left_column, right_column = readInList('files/day1-location_lists.txt')
total = 0
left_column = sorted(left_column)
right_column = sorted(right_column)
for i in range(len(left_column)):
    total += abs(left_column[i] - right_column[i])
print(total)