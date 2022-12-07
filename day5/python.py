# First, convert diagram to lists
list1 = ['N','W','F','R','Z','S','M','D']
list2 = ['S','G','Q','P','W']
list3 = ['C','J','N','F','Q','V','R','W']
list4 = ['L','D','G','C','P','Z','F']
list5 = ['S','P','T']
list6 = ['L','R','W','F','D','H']
list7 = ['C','D','N','Z']
list8 = ['Q','J','S','V','F','R','N','W']
list9 = ['V','W','Z','G','S','M','R']
list1 = list1[::-1]
list2 = list2[::-1]
list3 = list3[::-1]
list4 = list4[::-1]
list5 = list5[::-1]
list6 = list6[::-1]
list7 = list7[::-1]
list8 = list8[::-1]
list9 = list9[::-1]

# Second, do actions specified in input.txt
with open('input.txt') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        # if i < 3: # Veriied response matches diagram after 3 turns
        line = line.replace('\n','')
        print(line)
        commandParts = line.split(' ')

        for i, item in enumerate(commandParts):
            if i == 1:
                numberToMove = int(item)
            elif i == 3:
                startList = int(item)
            elif i == 5:
                destinationList = int(item)

        # try moving 1 from start -> destination
        for x in range(0,numberToMove):
            if startList == 1:
                if destinationList == 1:
                    list1.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 2:
                    list2.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 3:
                    list3.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 4:
                    list4.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 5:
                    list5.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 6:
                    list6.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 7:
                    list7.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 8:
                    list8.append(list1[-1:][0])
                    list1.pop(-1)
                elif destinationList == 9:
                    list9.append(list1[-1:][0])
                    list1.pop(-1)
            elif startList == 2:
                if destinationList == 1:
                    list1.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 2:
                    list2.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 3:
                    list3.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 4:
                    list4.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 5:
                    list5.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 6:
                    list6.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 7:
                    list7.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 8:
                    list8.append(list2[-1:][0])
                    list2.pop(-1)
                elif destinationList == 9:
                    list9.append(list2[-1:][0])
                    list2.pop(-1)
            elif startList == 3:
                if destinationList == 1:
                    list1.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 2:
                    list2.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 3:
                    list3.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 4:
                    list4.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 5:
                    list5.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 6:
                    list6.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 7:
                    list7.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 8:
                    list8.append(list3[-1:][0])
                    list3.pop(-1)
                elif destinationList == 9:
                    list9.append(list3[-1:][0])
                    list3.pop(-1)
            elif startList == 4:
                if destinationList == 1:
                    list1.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 2:
                    list2.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 3:
                    list3.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 4:
                    list4.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 5:
                    list5.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 6:
                    list6.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 7:
                    list7.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 8:
                    list8.append(list4[-1:][0])
                    list4.pop(-1)
                elif destinationList == 9:
                    list9.append(list4[-1:][0])
                    list4.pop(-1)
            elif startList == 5:
                if destinationList == 1:
                    list1.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 2:
                    list2.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 3:
                    list3.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 4:
                    list4.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 5:
                    list5.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 6:
                    list6.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 7:
                    list7.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 8:
                    list8.append(list5[-1:][0])
                    list5.pop(-1)
                elif destinationList == 9:
                    list9.append(list5[-1:][0])
                    list5.pop(-1)
            elif startList == 6:
                if destinationList == 1:
                    list1.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 2:
                    list2.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 3:
                    list3.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 4:
                    list4.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 5:
                    list5.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 6:
                    list6.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 7:
                    list7.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 8:
                    list8.append(list6[-1:][0])
                    list6.pop(-1)
                elif destinationList == 9:
                    list9.append(list6[-1:][0])
                    list6.pop(-1)
            elif startList == 7:
                if destinationList == 1:
                    list1.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 2:
                    list2.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 3:
                    list3.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 4:
                    list4.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 5:
                    list5.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 6:
                    list6.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 7:
                    list7.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 8:
                    list8.append(list7[-1:][0])
                    list7.pop(-1)
                elif destinationList == 9:
                    list9.append(list7[-1:][0])
                    list7.pop(-1)
            elif startList == 8:
                if destinationList == 1:
                    list1.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 2:
                    list2.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 3:
                    list3.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 4:
                    list4.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 5:
                    list5.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 6:
                    list6.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 7:
                    list7.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 8:
                    list8.append(list8[-1:][0])
                    list8.pop(-1)
                elif destinationList == 9:
                    list9.append(list8[-1:][0])
                    list8.pop(-1)
            elif startList == 9:
                if destinationList == 1:
                    list1.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 2:
                    list2.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 3:
                    list3.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 4:
                    list4.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 5:
                    list5.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 6:
                    list6.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 7:
                    list7.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 8:
                    list8.append(list9[-1:][0])
                    list9.pop(-1)
                elif destinationList == 9:
                    list9.append(list9[-1:][0])
                    list9.pop(-1)

    print(f'my last container 1: {list1[-1]}')
    print(f'my last container 2: {list2[-1]}')
    print(f'my last container 3: {list3[-1]}')
    print(f'my last container 4: {list4[-1]}')
    print(f'my last container 5: {list5[-1]}')
    print(f'my last container 6: {list6[-1]}')
    print(f'my last container 7: {list7[-1]}')
    print(f'my last container 8: {list8[-1]}')
    print(f'my last container 9: {list9[-1]}')