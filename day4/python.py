
with open('input.txt') as f:
    lines = f.readlines()
    scoreBucket = []
    for i, line in enumerate(lines):
        # if i < 5:
        line = line.replace('\n','')
        assignments = line.split(',')
        print('\n',assignments)
        rangehold1 = assignments[0].split('-')
        # print(assignments[0])
        range1 = [*range(int(rangehold1[0]),int(rangehold1[1])+1)]
        # print(range1)
        rangehold2 = assignments[1].split('-')
        range2 = [*range(int(rangehold2[0]),int(rangehold2[1])+1)]

        if len(range1) <= len(range2):
            print('range 1 smaller, so check for all of range 1 in range 2')
            # print(range1, range2)
            if set(range1).issubset(range2): # NOTE: tested with 12-15,13-28 and it works
                print('yes')
                scoreBucket.append(int(1))
        else:
            print('range 2 smaller, so check for all of range 2 in range 1')
            if set(range2).issubset(range1): # NOTE: tested with 12-15,13-28 and it works
                print('yes')
                scoreBucket.append(int(1))
    print(sum(scoreBucket))

    # Part 2: we need ANY overlap, so simplier
    print('\n***********')
    newBucket = []
    for i, line in enumerate(lines):
        # if i < 5:
        line = line.replace('\n','')
        assignments = line.split(',')
        print('\n',assignments)
        rangehold1 = assignments[0].split('-')
        # print(assignments[0])
        range1 = [*range(int(rangehold1[0]),int(rangehold1[1])+1)]
        # print(range1)
        rangehold2 = assignments[1].split('-')
        range2 = [*range(int(rangehold2[0]),int(rangehold2[1])+1)]

        tempBucket = []
        if len(range1) <= len(range2):
            print('range 1 smaller, so check for all of range 1 in range 2')
            # print(range1, range2)
            for x in range1:
                if x in range2:
                    print('yes')
                    tempBucket.append(int(1))
        else:
            print('range 2 smaller, so check for all of range 2 in range 1')
            for x in range2:
                if x in range1:
                    print('yes')
                    tempBucket.append(int(1))
        # B/c if doing every number in range, will have more than 1 hit per range sometimes...
        if sum(tempBucket) > 0:
            newBucket.append(int(1))
    print(sum(newBucket))

