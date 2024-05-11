with open("stu.csv") as file:
    for line in file:
        print("Hello", line.rstrip())