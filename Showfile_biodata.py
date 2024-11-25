with open ("biodata.txt", "r") as Satomo:
    lines = Satomo.readlines()
    print(lines[0].strip())
    print(lines[1].strip())
    print(lines[5].strip())