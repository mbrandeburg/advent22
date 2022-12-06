## Part 1
with open('input.txt') as f:
    lines = f.readlines()
    score = list()
    for z, line in enumerate(lines):
        # if z == 0:
        line_items = line.split()
        # print(line_items)
    
        # 0 if list, 3 for draw, 6 for win
        if line_items[0] == 'A': # they played rock
            if line_items[1] == 'X': # I played rock
                score.append(1+3)
            elif line_items[1] == 'Y': # I played paper
                score.append(2+6)
            elif line_items[1] == 'Z': # I played scissors
                score.append(3+0)
        elif line_items[0] == 'B': # they played paper
            if line_items[1] == 'X': # I played rock
                score.append(1+0)
            elif line_items[1] == 'Y': # I played paper
                score.append(2+3)
            elif line_items[1] == 'Z': # I played scissors
                score.append(3+6)
        elif line_items[0] == 'C': # they played scissors
            if line_items[1] == 'X': # I played rock
                score.append(1+6)
            elif line_items[1] == 'Y': # I played paper
                score.append(2+0)
            elif line_items[1] == 'Z': # I played scissors
                score.append(3+3)
    # print(score)
    print(f'My total score is: {sum(score)}')

## Part 2
# Now X means I need to throw it, Y means draw, Z means win
with open('input.txt') as f:
    lines = f.readlines()
    score = list()
    for z, line in enumerate(lines):
        # if z == 0:
        line_items = line.split()
        # print(line_items)

        # 0 if list, 3 for draw, 6 for win
        # 1 for Rock, 2 for Paper, and 3 for Scissors
        if line_items[0] == 'A': # they played rock
            if line_items[1] == 'X': # I played scissors
                score.append(3+0)
            elif line_items[1] == 'Y': # I played rock
                score.append(1+3)
            elif line_items[1] == 'Z': # I played paper
                score.append(2+6)
        elif line_items[0] == 'B': # they played paper
            if line_items[1] == 'X': # I played rock
                score.append(1+0)
            elif line_items[1] == 'Y': # I played paper
                score.append(2+3)
            elif line_items[1] == 'Z': # I played scissors
                score.append(3+6)
        elif line_items[0] == 'C': # they played scissors
            if line_items[1] == 'X': # I played paper
                score.append(2+0)
            elif line_items[1] == 'Y': # I played scissors
                score.append(3+3)
            elif line_items[1] == 'Z': # I played rock
                score.append(1+6)
    # print(score)
    print(f'My NEW total score is: {sum(score)}')
