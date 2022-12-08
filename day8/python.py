import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None

# Step 1: create a dataframe
with open('input.txt') as f:
    lines = f.readlines()
    score = list()
    totalRows = len(lines)
    totalCols = None
    for z, line in enumerate(lines):
        line=line.replace('\n','')
        if z == 0: # B/c initialization lets us do a lot of stuff we skip for all other rows
            print(line)
            totalCols = len(line)
            colNames = []
            for i in range(0,len(line)):
                colNames.append(f'col{i}')

            a = np.arange(0, totalCols*totalRows).reshape(totalRows,totalCols)
            df = pd.DataFrame(a,columns=colNames)

            # print('z','i','item')
            for i, item in enumerate(line):
                # if i < 2:
                #     print(z, i,item)
                df[f'col{i}'].loc[z] = item
        else:
            for i, item in enumerate(line):
                # if i < 2:
                #     print(z, i,item)
                df[f'col{i}'].loc[z] = item




## NOW ANALYZE THE DF
# Step 2: count len() first and last row, and doulbe number of rows total to get borders that are inherently visible
initialCount = len(df.col1) * 2 + len(df.loc[0]) * 2 - 3 # b/c can't count the 4 corners each time

# Step 3: figure out how to traverse dataframe, figuring if visible from outside
# Step 3b: keep in mind that inner rows have to keep checking all the way till outer row is hit...
newCounts = 0
for i in range(1,len(df)-1): # we skip first and last row
    for z in range(1,len(df.loc[i])-1): # we skip first and last column
        # Get a x,y coordinate
        currentLocation = [i,z]
        currentValue = df.loc[i][z]  # i is row, z is column
        print('**CHECKING***')
        print(f'currentLocation: {currentLocation}')
        print(f'currentValue: {currentValue}')

        # for each cell, do 4 checks until element == 0 or 98
        # if pass, newCounts = newCounts + 1
        # check north
        northList = list(range(0,currentLocation[1]))
        northList = northList[::-1] # Reverse that order!
        for coord in northList:
            adjacentValue = df.loc[coord][currentLocation[1]]
            if adjacentValue < currentValue:
                if coord == 0:
                    print(f'North hit for {currentLocation}')
                    newCounts = newCounts + 1
                    # exit(1)
            else:
                break
        
        # check south
        southList = list(range(currentLocation[0]+1,99))
        # print(southList)
        for coord in southList:
            adjacentValue = df.loc[coord][currentLocation[1]]
            print(adjacentValue, currentValue)
            # exit(1)
            if adjacentValue < currentValue:
                if coord == 98:
                    print(f'South hit for {currentLocation}')
                    newCounts = newCounts + 1
                    # exit(1)
            else:
                break

        # check east
        eastList = list(range(currentLocation[1]+1,99))
        # print(eastList)
        for coord in eastList:
            # print(f'New coord: {coord}')
            # exit(1)
            adjacentValue = df.loc[currentLocation[0]][coord]
            # print(f'Adjacent to east: {adjacentValue}')
            # exit(1)
            if adjacentValue < currentValue:
                if coord == 98:
                    print(f'East hit for {currentLocation}')
                    newCounts = newCounts + 1
                    # exit(1)
            else:
                break

        # check west
        westList = list(range(0,currentLocation[0]))
        westList = westList[::-1]
        # print(westList)
        # exit(1)
        for coord in westList:
            adjacentValue = df.loc[currentLocation[0]][coord]
            if adjacentValue < currentValue:
                if coord == 0:
                    print(f'West hit for {currentLocation}')
                    newCounts = newCounts + 1
                    # exit(1)
            else:
                break

        # print(newCounts)
        # exit(1)

###### PRINT
# print(df)
# print(df.col1)
# print(df.loc[0]) # print row 0
# print(df.loc[98])
print(initialCount+newCounts)