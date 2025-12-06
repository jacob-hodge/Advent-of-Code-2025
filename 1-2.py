curr_val = 50
count = 0
with open("1.txt") as f:
    for x in f:
        turn = int(x[1:])
        turnmod = turn % 100
        count += turn // 100

        if x[0] == "L":
            if curr_val <= turnmod and curr_val != 0:
                count += 1
            curr_val -= turnmod
        else:
            if curr_val + turnmod >= 100 and curr_val != 0:
                count += 1
            curr_val += turnmod
        curr_val = curr_val % 100

    print(count)