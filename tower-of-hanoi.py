peg1 = [8, 7, 6, 5, 4, 3, 2, 1]
peg2 = []
peg3 = []

def move(num_disks, source, dest, aux):
    # Moves num_disks disks from the source peg onto the dest peg using the aux peg

    if (num_disks > 0):
        move(num_disks - 1, source, aux, dest) # Move all the disks except the bottom disk onto the aux peg
        dest.append(source.pop())
        print("Peg 1: " + str(peg1))
        print("Peg 2: " + str(peg2))
        print("Peg 3: " + str(peg3))
        print("####################")
        move(num_disks - 1, aux, dest, source)

move(len(peg1), peg1, peg3, peg2)