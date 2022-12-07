with open('input.txt') as f:
    lines = f.readlines()
    totals = {}
    bucket = {}
    workingTree = []
    currentParent = None
    currentDirectory = None
    currentValues = []
    for i,line in enumerate(lines):
        line = line.replace('\n','')
        if line == '$ ls':
            pass
        else:
            if i < 30:
                print(f'line: {line}')
                # things we know:
                # every time we hit cd, we either:
                    # add to pre-existing entry
                    # add contents as new under top level
                        # and need to handle for `cd ..`
                # let's make nested json!

                splitValues = line.split(' ')
                if splitValues[0] == '$':
                    if splitValues[1] == 'cd':
                        if splitValues[2] != '..':
                            print(f'here is our folder value: {splitValues[2]}')
                            print(f'current bucket: {bucket}')
                            if splitValues[2] in bucket:
                                print('\n\n***** we need to be able to move in our tree')
                                exit(1) # TODO: cd back up a level
                            else:
                                if currentDirectory != None:
                                    print(f'PREVIOUS DIRECOTRY: {currentDirectory} SIZE: {sum(currentValues)}')
                                    totals[currentDirectory] = sum(currentValues)
                                currentDirectory = splitValues[2]
                                print(f'current directory: {currentDirectory}')
                                # Check if already in tree/bucket:
                                if currentDirectory in workingTree:
                                    # insert into bucket
                                    bucket[currentParent]['sub-folders'] = {currentDirectory:{'sub-folders':{}}}
                                    print(f'updated bucket: {bucket}','\n')
                                    
                                    # insert within working tree
                                    for i, item in enumerate(workingTree):
                                        if item == currentDirectory:
                                            workingTree.insert(i+1,'<-parent')
                                            currentParent = currentDirectory
                                    print(f'updated working tree: {workingTree}')
                                    currentValues = [] # empty it out
                                else:
                                    currentParent = currentDirectory
                                    workingTree.append(currentDirectory)
                                    workingTree.append('<-parent') # for splititng later?
                                    print(f'updated working tree: {workingTree}')
                                    bucket[splitValues[2]] = {'sub-folders':{}}
                                    print(f'updated bucket: {bucket}','\n')
                                    currentValues = [] # empty it out
                        else: # if cd ..
                            # move up the tree
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
                            # print(currentDirectory)
                            # exit(1)
                else:
                    if splitValues[0] != 'dir': 
                        # Until we hit a new directory in above line, its our key
                        # and we figure out how to traverse json though...
                        currentValues.append(int(splitValues[0]))
                    else:
                        # we need to add to our tree ..
                        # not just straight append, but insert after parent
                        for i, item in enumerate(workingTree):
                            if item == currentParent:
                                workingTree.insert(i+2, splitValues[1])  
                        print(f'working tree: {workingTree}')

                # print('\n')
                # print(totals)
                # print(bucket)
                # print('\n')