import sys

kata = (19,42,21)

def kata_do():
    s = str(kata[0])
    for i in range(1, len(kata)):
        s = s  + ', ' + str(kata[i])
    print(f"There are {len(kata)} numbers : {s}")
    return

if __name__ == "__main__":
    if len(sys.argv) == 1:
        kata_do()
    elif sys.argv[1] == "new_tuple":
        kata = tuple(int(x) for x in input("Enter the numbers separated by commas: ").split(","))
        kata_do()
    else:
        print("Error: Too many arguments")