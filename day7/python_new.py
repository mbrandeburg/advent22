import pandas as pd

df1 = pd.DataFrame()

with open('input.txt') as f:
    lines = f.readlines()
    totals = {}
    bucket = {}
    workingTree = []
    currentParent = None
    currentDirectory = None
    currentValues = []


    # TODO: Simplify this whole things. We keep top level only.
    # Add the values to the top level -- lets do a dataframe
    for i,line in enumerate(lines):
        line = line.replace('\n','')
        if line == '$ ls':
            pass
        else:
            if i < 12: #30 later
                print(f'line: {line}')
                splitValues = line.split(' ')


                if splitValues[0] == '$': # we pass ls but keeping for other items
                    if splitValues[1] == 'cd':
                        if splitValues[2] == '..':
                            # move up parent -- IF ITS FIRST PARENT, CLEAR PARENT TREE AND RESTART
                            # OTHERWISE, DO NOTHING AS WE KEEP ADDING VALUES TO DATAFRAME
                            pass
                        else:
                            # do something - we add a new parent
                            pass
                elif splitValues[0] == 'dir':
                    # do something - append to tree but we really dont need to in all likelyhood
                    # NOW WE ONLY CARE ABOUT TOP LEVEL PARENT CHANGES
                    pass
                else:
                    # add values to parent
                    pass