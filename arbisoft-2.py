import math


def distance_metric(x1: int, y1: int, x2: int, y2: int):
    print(f"x1: {x1}, y1: {y1}   ;  x2: {x2}, y2: {y2}")
    return math.sqrt(((x1-x2) * (x1-x2)) + ((y1-y2)*(y1-y2)))


with open("input2.txt", "r") as f:
    input_line = f.readline()
    distances = []
    while input_line[0] != '0':
        temp = []
        temp = input_line[2:].split(' ')
        temp = [int(t.strip('\n')) for t in temp]
        print(temp)
        for i in range(0, int(input_line[0]) - 1, 2):
            distances.append(distance_metric(temp[2*i], temp[(2*i)+1],
                                             temp[(2*i)+2], temp[(2*i)+3]))
        input_line = f.readline()
        while (input_line == '\n'):
            input_line = f.readline()
        print(input_line)
        if input_line[0] == '0':
            break

    print(distances)
