with open("tables from 2 to 20.txt", "w") as f:
    for tab in range(2, 21):
        f.write(f"---Table of {tab}---\n")
        print("\n")
        for i in range(1,11):
            line = (f"{tab} * {i} = {tab*i}\n")
            print(line, end="")
            f.write(line)
        f.write("\n")