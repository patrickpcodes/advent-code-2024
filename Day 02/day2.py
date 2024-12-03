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

# Call the function with the filename
data = readInList('../files/day2-reports.txt')

    


def checkValidReport(report, numToRemove):
    if numToRemove == 1:
        for j in range(len(report)):
            updated_list = [item for i, item in enumerate(report) if i != j]
            result = checkValidReport(updated_list, 0)
            if result:
                return True
        return False
    else:
        row = report
        increasing = False
        if row[0] == row[1]:
            return False
        elif row[0] < row[1]:
            increasing = True
        is_valid = True
        for j in range(len(row)-1):
            if increasing:
                if row[j+1] <= row[j] or abs(row[j+1] -row[j]) > 3:
                    is_valid = False
                    break
            else:
                if row[j+1] >= row[j] or abs(row[j+1] -row[j]) > 3:
                    is_valid = False
                    break
        if is_valid:
            return True
        else:
            return False

count =0
for i in range(len(data)):
    result = checkValidReport(data[i], 0)
    if result:
        count += 1
print(count)
count = 0
for i in range(len(data)):
    result = checkValidReport(data[i], 0)
    if result == False:
        result = checkValidReport(data[i], 1)
    if result:    
        count += 1
    print(result, data[i])
    

print(count)