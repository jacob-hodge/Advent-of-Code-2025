curr_val = 50
count = 0
with open("1.txt") as f:
    for x in f:
        if x[0] == "L":
            curr_val -= int(x[1:])
        else:
            curr_val += int(x[1:])
        curr_val = curr_val % 100
        if curr_val == 0:
            count += 1

print(curr_val)
print(count)