import math


def distance_metric(a: tuple, b: tuple):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def average_point(points: list):
    avgx = 0
    avgy = 0

    for i in range(len(points)):
        avgx += points[i][0]
        avgy += points[i][1]

    avgx = avgx/len(points)
    avgy = avgy/len(points)

    print(f"{avgx} ,  {avgy}")
    return (avgx, avgy)


def findMeetingPoint(points: list, avg_point: tuple):
    avgDist = distance_metric(points[0], avg_point)
    meetingPoint = points[0]
    totalDistance = avgDist
    for i in range(1, len(points)):
        tempDist = distance_metric(points[i], avg_point)
        totalDistance += tempDist
        if avgDist > tempDist:
            avgDist = tempDist
            meetingPoint = points[i]
    print(meetingPoint, str(totalDistance))


with open("input2.txt", "r") as f:
    input_line = f.readline()
    distances = []
    points = []
    while input_line[0] != '0':
        temp = []
        temp = input_line[2:].split(' ')
        temp = [int(t.strip('\n')) for t in temp]
        print(temp)
        for i in range(0, int(input_line[0])):
            points.append((temp[2*i], temp[(2*i)+1]))

        input_line = f.readline()
        while (input_line == '\n'):
            input_line = f.readline()
        if input_line[0] == '0':
            break
    print(points)
    findMeetingPoint(points, average_point(points))
