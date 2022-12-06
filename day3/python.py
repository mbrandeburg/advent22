import string

# Set the dictionary for my upper and lower case values
priorityDictLower = dict((key, i+1) for i, key in enumerate(string.ascii_lowercase)) 
priorityDictHigher = dict((key, i+27) for i, key in enumerate(string.ascii_uppercase))

def Merge(dict1, dict2):
    return(dict1.update(dict2))
Merge(priorityDictLower,priorityDictHigher)

priorityDict = priorityDictLower
# print(priorityDict)


# Now read in the input file and match against dictionary
with open('input.txt') as f:
    lines = f.readlines()
    scoreBucket = []
    for i, line in enumerate(lines):
        # if i < 2:
        line = line.replace('\n','')
        len_line = len(line)

        split_len_line = int(len_line/2)
        # print(split_len_line)
        # print(len_line)
        # print(line)

        firstHalf = line[split_len_line:]
        secondHalf = line[:split_len_line]
        # print(firstHalf)
        # print(secondHalf)

        matchBucket = []
        for x in firstHalf:
            if x in secondHalf:
                matchBucket.append(x)
        # print(matchBucket)
        scoreBucket.append(priorityDict[matchBucket[0]])
    print(sum(scoreBucket))

# Part 2
with open('input.txt') as f:
    lines = f.readlines()
    NEWscoreBucket = []
    for i, line in enumerate(lines):
        if i > 0:
            # if i < 7: # TEST WITH 2 GROUPS
            if i % 3 == 0: # our groups of 3
                commonLetter = []
                sacks = lines[i-3:i]
                print('\n',sacks)
                for x in sacks[0]:
                    if x != '\n':
                        if x in sacks[1]:
                            if x in sacks[2]:
                                if x not in commonLetter:
                                    commonLetter.append(x)
                                    print(commonLetter)
                                    print(priorityDict[commonLetter[0]])
                                    NEWscoreBucket.append(priorityDict[commonLetter[0]])
    # For some reason, missing last 3, so:
    lastSack = lines[-3:]
    print(lastSack)
    commonLetter = [] # Reset it
    for x in lastSack[0]:
        if x != '\n':
            if x in lastSack[1]:
                if x in lastSack[2]:
                    if x not in commonLetter:
                        commonLetter.append(x)
                        print(commonLetter)
                        print(priorityDict[commonLetter[0]])
                        NEWscoreBucket.append(priorityDict[commonLetter[0]])
    # Finally, sum:
    print(sum(NEWscoreBucket))
   
