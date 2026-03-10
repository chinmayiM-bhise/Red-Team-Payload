import os


def simulate_persistence():

    path = os.path.expanduser("~")

    file = os.path.join(path, "startup_simulation.txt")

    with open(file, "w") as f:
        f.write("This simulates persistence in startup folder.")

    print("Persistence simulation created.")


if __name__ == "__main__":
    simulate_persistence()