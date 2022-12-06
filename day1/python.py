

with open('input.txt') as f:
    lines = f.readlines()
    counter = 1 # Which elf
    my_dict = {}
    bucket = list()
    final_bucket = list()
    for line in lines:
        len_line = len(line)
        print(f'{line} : lenght of {len_line}')
        if len_line == 1:
            # print(bucket)
            # print(sum(bucket))
            my_dict[counter] = sum(bucket)
            print(my_dict)
            bucket = []
            # print(bucket)
            counter = counter + 1
            # print(counter)
            # exit(0)
        else:
            bucket.append(int(line.replace('\n','')))
            print(bucket)
    print(my_dict)
    # print max value elf
    max_elf = max(my_dict, key=my_dict.get)
    print(f"elf number {max_elf} with calories {max(my_dict.values())}")

    # part 2: we need to sort so we get not just max but top 3
    print('\n')
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    print(sorted_dict)
    for x in list(sorted_dict)[-3:]:
        final_bucket.append(sorted_dict[x])
    print(f'top 3 elf calories: {sum(final_bucket)}')