# Go from 4 -> 14 characters
with open('input.txt') as f:
    lines = f.readlines()
    bucket = []
    for i in range(0,len(lines[0].replace('\n',''))):
        print(i,lines[0][i])
        bucket.append(lines[0][i])
        print(bucket)
        
        if i >= 13:
            # exit(1)
            if lines[0][i] not in bucket[0:13]:
                # Last 3 need to be unique too
                if len(set(bucket[0:13])) == 13:
                    print(f'MATCH AT CHARACTER {i+1}') # Off set b/c they start at 1 count for winning value
                    exit(0)
            if len(bucket) == 14:
                bucket.pop(0)
