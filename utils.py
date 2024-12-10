def readInList(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Initialize empty lists for each column
        data = []

        # Read each line in the file
        for line in file:
            # Split the line by whitespace
            rowSData = line.strip().split()
            # Append the values to the respective lists
            rowData =[]
            for i in rowSData:
                rowData.append(int(i))
            data.append(rowData)
    return data