import pandas as pd
df = pd.DataFrame()

with open('input.txt') as f:
    lines = f.readlines()
    score = list()
    for z, line in enumerate(lines):
        line=line.replace('\n','')
        if z == 0:
            print(line)
            # Step 1: create a dataframe
            # Step 2: count len() first and last row, and doulbe number of rows total to get borders that are inherently visible
            # Step 3: figure out how to traverse dataframe, figuring if visible from outside
            # Step 3b: keep in mind that inner rows have to keep checking all the way till outer row is hit...