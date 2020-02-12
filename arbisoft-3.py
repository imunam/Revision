Tribes = {}


def FillTribes(names: list):
    tribeSet = list(names[1:])
    tribeSet = [name.strip() for name in tribeSet]

    if names[0] in Tribes.keys():
        if names[1].rstrip() not in Tribes[names[0]]:
            Tribes[names[0]].extend(tribeSet)
    else:
        Tribes[names[0]] = tribeSet


def PrintNamesInTribes(case: int):
    with open('output3.txt', 'w+') as out:
        out.write(f"Case: {i+1}\n")
        for key, value in Tribes.items():
            print(f"{key} {len(value)} : {value}\n")
            out.write(f"{key} {len(value)}\n")


with open('input3.txt', 'r') as file:
    totalTestCases = file.readline()
    for i in range(0, int(totalTestCases)):
        totalRows = file.readline()
        for j in range(0, int(totalRows)):
            inp = file.readline()
            names = inp.split(' ', 1)
            FillTribes(names)
        print(f"Case: {i+1}\n")
        PrintNamesInTribes(i)
