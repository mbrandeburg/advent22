import pandas as pd

df = pd.DataFrame(columns=['TopParent','TotalValue'])

with open('input.txt') as f:
    lines = f.readlines()
    totals = {}
    bucket = {}
    workingTree = []
    currentParent = None
    currentDirectory = None
    currentValues = []


    # Version 2: Simplify this whole things. We keep top level only.
    # Add the values to the top level -- lets do a dataframe
    for i,line in enumerate(lines):
        line = line.replace('\n','')
        if line == '$ ls':
            pass
        else:
            if i < 5000000: #16 if using input_test.txt
                print(f'line: {line}')
                splitValues = line.split(' ')


                if splitValues[0] == '$': # we pass ls but keeping for other items
                    if splitValues[1] == 'cd':
                        if splitValues[2] == '..':
                            # move up parent -- IF ITS FIRST PARENT, CLEAR PARENT TREE AND RESTART
                            # OTHERWISE, DO NOTHING AS WE KEEP ADDING VALUES TO DATAFRAME

                            # take the currentParent in the tree, 
                            #   then jump to first parent before that as new parent
                            parentBuckets = []
                            latestLocation = None
                            newParentLocation = None

                            for i, item in enumerate(workingTree):
                                if item == '<-parent':
                                    parentBuckets.append(i-1)
                                if item == currentDirectory:
                                    latestLocation = i
                            # print(currentDirectory)
                            # print(f'parentBuckets: {parentBuckets}')
                            # print(f'latestLocation: {latestLocation}')
                            for i, item in enumerate(parentBuckets):
                                if parentBuckets[i] == latestLocation:
                                    newParentLocation = parentBuckets[i-1]
                            currentDirectory = workingTree[newParentLocation]
                            print(currentDirectory)

                            # NOTE: if we got back to currentDirectory == '/'
                            #   then erase everything else from list
                            if currentDirectory == '/':
                                workingTree = ['/', '<-parent']

                        else:
                            # do something - we add a new parent
                            currentDirectory = splitValues[2]
                            if currentDirectory in workingTree:
                                # insert within working tree
                                for i, item in enumerate(workingTree):
                                    if item == currentDirectory:
                                        # workingTree.insert(i+1,'<-parent') # We dont need to update parents anymore since only collecting parents...
                                        currentParent = currentDirectory
                                print(f'updated working tree: {workingTree}')
                            else:
                                currentParent = currentDirectory
                                workingTree.append(currentDirectory)
                                workingTree.append('<-parent') # for splititng later?
                                print(f'updated working tree: {workingTree}')
                elif splitValues[0] == 'dir':
                    # We used to append to tree but we really dont need to in all likelyhood
                    # B/C NOW WE ONLY CARE ABOUT TOP LEVEL PARENT CHANGES
                    pass
                else: # appending values from file sizes
                    # get top level parent and see if already a row, if not add it (update value unless new, then set as value)
                    parentBuckets = []
                    for i, item in enumerate(workingTree):
                        if item == '<-parent':
                            parentBuckets.append(i-1)
                    if len(parentBuckets) == 1:
                        trueParent = workingTree[parentBuckets[0]] # Capture / but then ignore it rest of time
                    else:
                        trueParent = workingTree[parentBuckets[1]] # We only care about level just below slash
                    # Check if already exists
                    if trueParent in df['TopParent'].values:
                        for i in range(0,len(df)):
                            if df['TopParent'][i] == trueParent:
                                df['TotalValue'][i] = df['TotalValue'][i] + int(splitValues[0])
                    else:
                        df = df.append({'TopParent':trueParent, 'TotalValue':int(splitValues[0])},ignore_index=True)

print('\n',df)
# print(df.columns)
# print(df['TopParent'].values)