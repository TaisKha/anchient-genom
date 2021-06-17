from random import randrange


def generateRF(length):
    with open("rf.txt", "w") as f:
        for _ in range(length):
            f.write("GACT"[randrange(0, 4)])


l = 100
generateRF(l)
