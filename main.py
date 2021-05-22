class Kocka:
    f = ["G", "G", "G", "G", "G", "G", "G", "G", "G"]
    r = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
    b = ["B", "B", "B", "B", "B", "B", "B", "B", "B"]
    l = ["R", "R", "R", "R", "R", "R", "R", "R", "R"]
    u = ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]
    d = ["W", "W", "W", "W", "W", "W", "W", "W", "W"]

algoritmi = {"okreniPrednjiEdge" : ["R'", "F", "R", "F'", "U"]}
scramble = ["R", "U", "F", "D'"]

# class Kocka:
#     f = ["O", "B", "W", "G", "G", "O", "R", "B", "Y"]
#     r = ["G", "R", "G", "W", "O", "B", "O", "Y", "W"]
#     b = ["W", "R", "W", "Y", "B", "W", "B", "R", "R"]
#     l = ["B", "O", "Y", "R", "R", "W", "B", "O", "G"]
#     u = ["O", "G", "O", "G", "Y", "B", "B", "O", "R"]
#     d = ["Y", "W", "G", "Y", "W", "G", "Y", "Y", "R"]

kocka = Kocka
resenje = []
edges = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
def ispisiKocku():
    print("----------------------------------------------------")
    print("Prednja:")
    for i in range(0, 9, 3):
        print(kocka.f[i] + " " + kocka.f[i + 1] + " " + kocka.f[i + 2])
    print("----------------------------------------------------")
    print("Desna:")
    for i in range(0, 9, 3):
        print(kocka.r[i] + " " + kocka.r[i + 1] + " " + kocka.r[i + 2])
    print("----------------------------------------------------")
    print("Zadnja:")
    for i in range(0, 9, 3):
        print(kocka.b[i] + " " + kocka.b[i + 1] + " " + kocka.b[i + 2])
    print("----------------------------------------------------")
    print("Leva:")
    for i in range(0, 9, 3):
        print(kocka.l[i] + " " + kocka.l[i + 1] + " " + kocka.l[i + 2])
    print("----------------------------------------------------")
    print("Gornja:")
    for i in range(0, 9, 3):
        print(kocka.u[i] + " " + kocka.u[i + 1] + " " + kocka.u[i + 2])
    print("----------------------------------------------------")
    print("Donja:")
    for i in range(0, 9, 3):
        print(kocka.d[i] + " " + kocka.d[i + 1] + " " + kocka.d[i + 2])
def mapiranje(s):
    if s == "W":
        return 0
    elif s == "Y":
        return 1
    elif s == "O":
        return 2
    elif s == "R":
        return 3
    elif s == "B":
        return 4
    elif s == "G":
        return 5
def mainInput():
    print("Prednja strana:")
    kocka.f[0], kocka.f[1], kocka.f[2] = input().split(" ")
    kocka.f[3], kocka.f[4], kocka.f[5] = input().split(" ")
    kocka.f[6], kocka.f[7], kocka.f[8] = input().split(" ")
    print("Desna strana:")
    kocka.r[0], kocka.r[1], kocka.r[2] = input().split(" ")
    kocka.r[3], kocka.r[4], kocka.r[5] = input().split(" ")
    kocka.r[6], kocka.r[7], kocka.r[8] = input().split(" ")
    print("Zadnja strana:")
    kocka.b[0], kocka.b[1], kocka.b[2] = input().split(" ")
    kocka.b[3], kocka.b[4], kocka.b[5] = input().split(" ")
    kocka.b[6], kocka.b[7], kocka.b[8] = input().split(" ")
    print("Leva strana:")
    kocka.l[0], kocka.l[1], kocka.l[2] = input().split(" ")
    kocka.l[3], kocka.l[4], kocka.l[5] = input().split(" ")
    kocka.l[6], kocka.l[7], kocka.l[8] = input().split(" ")
    print("Gornja strana:")
    kocka.u[0], kocka.u[1], kocka.u[2] = input().split(" ")
    kocka.u[3], kocka.u[4], kocka.u[5] = input().split(" ")
    kocka.u[6], kocka.u[7], kocka.u[8] = input().split(" ")
    print("Donja strana:")
    kocka.d[0], kocka.d[1], kocka.d[2] = input().split(" ")
    kocka.d[3], kocka.d[4], kocka.d[5] = input().split(" ")
    kocka.d[6], kocka.d[7], kocka.d[8] = input().split(" ")
def inputEdges():
    #----------------------------
    front = mapiranje(kocka.f[1])
    up = mapiranje(kocka.u[7])
    edges[front][up] = 1
    edges[up][front] = -1
    #----------------------------
    front = mapiranje(kocka.r[1])
    up = mapiranje(kocka.u[5])
    edges[front][up] = 2
    edges[up][front] = -2
    #----------------------------
    front = mapiranje(kocka.b[1])
    up = mapiranje(kocka.u[1])
    edges[front][up] = 3
    edges[up][front] = -3
    #----------------------------
    front = mapiranje(kocka.l[1])
    up = mapiranje(kocka.u[3])
    edges[front][up] = 4
    edges[up][front] = -4
    #----------------------------
    front = mapiranje(kocka.f[5])
    up = mapiranje(kocka.r[3])
    edges[front][up] = 5
    edges[up][front] = -5
    #----------------------------
    front = mapiranje(kocka.r[5])
    up = mapiranje(kocka.b[3])
    edges[front][up] = 6
    edges[up][front] = -6
    #----------------------------
    front = mapiranje(kocka.b[5])
    up = mapiranje(kocka.l[3])
    edges[front][up] = 7
    edges[up][front] = -7
    #----------------------------
    front = mapiranje(kocka.l[5])
    up = mapiranje(kocka.f[3])
    edges[front][up] = 8
    edges[up][front] = -8
    #----------------------------
    front = mapiranje(kocka.f[7])
    up = mapiranje(kocka.d[1])
    edges[front][up] = 9
    edges[up][front] = -9
    #----------------------------
    front = mapiranje(kocka.r[7])
    up = mapiranje(kocka.d[5])
    edges[front][up] = 10
    edges[up][front] = -10
    #----------------------------
    front = mapiranje(kocka.b[7])
    up = mapiranje(kocka.d[7])
    edges[front][up] = 11
    edges[up][front] = -11
    #----------------------------
    front = mapiranje(kocka.l[7])
    up = mapiranje(kocka.d[3])
    edges[front][up] = 12
    edges[up][front] = -12
    #----------------------------
    for i in range(6):
        print(edges[i])

def uradiAlgoritam(niz):
    for i in niz:
        if i == "R":
            moveRight()
        elif i == "R'":
            moveRightPrim()
        elif i == "L":
            moveLeft()
        elif i == "L'":
            moveLeftPrim()
        elif i == "D":
            moveDown()
        elif i == "D'":
            moveDownPrim()
        elif i == "U":
            moveUp()
        elif i == "U'":
            moveUpPrim()
        elif i == "F":
            moveFront()
        elif i == "F'":
            moveFrontPrim()
        elif i == "B":
            moveBack()
        elif i == "B'":
            moveBackPrim()
        elif i == "R2":
            R2()
        elif i == "L2":
            L2()
        elif i == "F2":
            F2()
        elif i == "B2":
            B2()
        elif i == "U2":
            U2()
        elif i == "D2":
            D2()
def moveRight():
    a = kocka.f[2]
    b = kocka.f[5]
    c = kocka.f[8]
    kocka.f[2] = kocka.d[2]
    kocka.f[5] = kocka.d[5]
    kocka.f[8] = kocka.d[8]
    kocka.d[2] = kocka.b[6]
    kocka.d[5] = kocka.b[3]
    kocka.d[8] = kocka.b[0]
    kocka.b[6] = kocka.u[2]
    kocka.b[3] = kocka.u[5]
    kocka.b[0] = kocka.u[8]
    kocka.u[2] = a
    kocka.u[5] = b
    kocka.u[8] = c
    a = kocka.r[3]
    b = kocka.r[6]
    kocka.r[3] = kocka.r[7]
    kocka.r[6] = kocka.r[8]
    kocka.r[7] = kocka.r[5]
    kocka.r[8] = kocka.r[2]
    kocka.r[5] = kocka.r[1]
    kocka.r[2] = kocka.r[0]
    kocka.r[1] = a
    kocka.r[0] = b
def moveRightPrim():
    moveRight()
    moveRight()
    moveRight()
def moveLeftPrim():
    a = kocka.f[0]
    b = kocka.f[3]
    c = kocka.f[6]
    kocka.f[0] = kocka.d[0]
    kocka.f[3] = kocka.d[3]
    kocka.f[6] = kocka.d[6]
    kocka.d[0] = kocka.b[8]
    kocka.d[3] = kocka.b[5]
    kocka.d[6] = kocka.b[2]
    kocka.b[8] = kocka.u[0]
    kocka.b[5] = kocka.u[3]
    kocka.b[2] = kocka.u[6]
    kocka.u[0] = a
    kocka.u[3] = b
    kocka.u[6] = c
    a = kocka.l[3]
    b = kocka.l[6]
    kocka.l[3] = kocka.l[1]
    kocka.l[6] = kocka.l[0]
    kocka.l[1] = kocka.l[5]
    kocka.l[0] = kocka.l[2]
    kocka.l[5] = kocka.l[7]
    kocka.l[2] = kocka.l[8]
    kocka.l[7] = a
    kocka.l[8] = b
def moveLeft():
    moveLeftPrim()
    moveLeftPrim()
    moveLeftPrim()
def moveUp():
    a = kocka.f[0]
    b = kocka.f[1]
    c = kocka.f[2]
    kocka.f[0] = kocka.r[0]
    kocka.f[1] = kocka.r[1]
    kocka.f[2] = kocka.r[2]
    kocka.r[0] = kocka.b[0]
    kocka.r[1] = kocka.b[1]
    kocka.r[2] = kocka.b[2]
    kocka.b[0] = kocka.l[0]
    kocka.b[1] = kocka.l[1]
    kocka.b[2] = kocka.l[2]
    kocka.l[0] = a
    kocka.l[1] = b
    kocka.l[2] = c
    a = kocka.u[7]
    b = kocka.u[8]
    kocka.u[7] = kocka.u[5]
    kocka.u[8] = kocka.u[2]
    kocka.u[5] = kocka.u[1]
    kocka.u[2] = kocka.u[0]
    kocka.u[1] = kocka.u[3]
    kocka.u[0] = kocka.u[6]
    kocka.u[3] = a
    kocka.u[6] = b
def moveUpPrim():
    moveUp()
    moveUp()
    moveUp()
def moveFront():
    a = kocka.l[2]
    b = kocka.l[5]
    c = kocka.l[8]
    kocka.l[2] = kocka.d[0]
    kocka.l[5] = kocka.d[1]
    kocka.l[8] = kocka.d[2]
    kocka.d[0] = kocka.r[6]
    kocka.d[1] = kocka.r[3]
    kocka.d[2] = kocka.r[0]
    kocka.r[6] = kocka.u[8]
    kocka.r[3] = kocka.u[7]
    kocka.r[0] = kocka.u[6]
    kocka.u[6] = c
    kocka.u[7] = b
    kocka.u[8] = a
    a = kocka.f[0]
    b = kocka.f[1]
    kocka.f[0] = kocka.f[6]
    kocka.f[1] = kocka.f[3]
    kocka.f[6] = kocka.f[8]
    kocka.f[3] = kocka.f[7]
    kocka.f[8] = kocka.f[2]
    kocka.f[7] = kocka.f[5]
    kocka.f[2] = a
    kocka.f[5] = b
def moveFrontPrim():
    moveFront()
    moveFront()
    moveFront()
def moveDown():
    a = kocka.f[6]
    b = kocka.f[7]
    c = kocka.f[8]
    kocka.f[6] = kocka.l[6]
    kocka.f[7] = kocka.l[7]
    kocka.f[8] = kocka.l[8]
    kocka.l[6] = kocka.b[6]
    kocka.l[7] = kocka.b[7]
    kocka.l[8] = kocka.b[8]
    kocka.b[6] = kocka.r[6]
    kocka.b[7] = kocka.r[7]
    kocka.b[8] = kocka.r[8]
    kocka.r[6] = a
    kocka.r[7] = b
    kocka.r[8] = c
    a = kocka.d[7]
    b = kocka.d[8]
    kocka.d[7] = kocka.d[5]
    kocka.d[8] = kocka.d[2]
    kocka.d[5] = kocka.d[1]
    kocka.d[2] = kocka.d[0]
    kocka.d[1] = kocka.d[3]
    kocka.d[0] = kocka.d[6]
    kocka.d[3] = a
    kocka.d[6] = b
def moveDownPrim():
    moveDown()
    moveDown()
    moveDown()
def moveBack():
    a = kocka.u[0]
    b = kocka.u[1]
    c = kocka.u[2]
    kocka.u[0] = kocka.r[2]
    kocka.u[1] = kocka.r[5]
    kocka.u[2] = kocka.r[8]
    kocka.r[2] = kocka.d[8]
    kocka.r[5] = kocka.d[7]
    kocka.r[8] = kocka.d[6]
    kocka.d[8] = kocka.l[6]
    kocka.d[7] = kocka.l[3]
    kocka.d[6] = kocka.l[0]
    kocka.l[0] = c
    kocka.l[3] = b
    kocka.l[6] = a
    a = kocka.b[1]
    b = kocka.b[0]
    kocka.b[0] = kocka.b[6]
    kocka.b[1] = kocka.b[3]
    kocka.b[3] = kocka.b[7]
    kocka.b[6] = kocka.b[8]
    kocka.b[7] = kocka.b[5]
    kocka.b[8] = kocka.b[2]
    kocka.b[2] = b
    kocka.b[5] = a
def moveBackPrim():
    moveBack()
    moveBack()
    moveBack()
def R2():
    moveRight()
    moveRight()
def F2():
    moveFront()
    moveFront()
def L2():
    moveLeft()
    moveLeft()
def D2():
    moveDown()
    moveDown()
def U2():
    moveUp()
    moveUp()
def B2():
    moveBack()
    moveBack()
def zelenoBeliEdge():
    inputEdges()
    a = edges[0][5]
    if a == -1:
        resenje.append("F2")
        F2()
    elif a == 1:
        uradiAlgoritam(["U'", "R'", "F", "R"])
        resenje.append(["U'", "R'", "F", "R"])
    elif a == -2:
        moveUp()
        F2()
        resenje.append("U", "F2")
    elif a == 2:
        uradiAlgoritam(["R'", "F", "R"])
        resenje.append(["R'", "F", "R"])
    elif a == -3:
        U2()
        F2()
        resenje.append(["U2", "F2"])
    elif a == 3:
        uradiAlgoritam(["U", "R'", "F", "R"])
        resenje.append(["U", "R'", "F", "R"])
    elif a == -4:
        moveUpPrim()
        F2()
        resenje.append("U'", "F2")
    elif a == 4:
        uradiAlgoritam(["L", "F'", "L'"])
        resenje.append(["L", "F'", "L'"])
    elif a == -5:
        moveFrontPrim()
        resenje.append("F'")
    elif a == 5:
        uradiAlgoritam(["R", "U", "R'", "F2"])
        resenje.append(["R", "U", "R'", "F2"])
    elif a == 6:
        uradiAlgoritam(["R2", "F'"])
        resenje.append(["R2", "F'"])
    elif a == -6:
        uradiAlgoritam(["R", "D'"])
        resenje.append(["R", "D'"])
    elif a == 7:
        uradiAlgoritam(["L", "U'", "F2"])
        resenje.append(["L", "U'", "F2"])
    elif a == -7:
        uradiAlgoritam(["L2", "F'"])
        resenje.append(["L2", "F'"])
    elif a == 8:
        uradiAlgoritam(["F'"])
        resenje.append(["F'"])
    elif a == -8:
        uradiAlgoritam(["L", "D"])
        resenje.append(["L", "D"])
    elif a == 9:
        uradiAlgoritam(["F", "L'", "U'", "F2"])
        resenje.append(["F", "L'", "U'", "F2"])
    elif a == -10:
        uradiAlgoritam(["D'"])
        resenje.append("D'")
    elif a == 10:
        uradiAlgoritam(["R", "F"])
        resenje.append(["R", "F"])
    elif a == -11:
        uradiAlgoritam(["D2"])
        resenje.append("D2")
    elif a == 11:
        uradiAlgoritam(["D'", "R", "F"])
        resenje.append(["D'", "R", "F"])
    elif a == -12:
        uradiAlgoritam(["D"])
        resenje.append("D")
    elif a == 12:
        uradiAlgoritam(["L'", "F'"])
        resenje.append(["L'", "F'"])
def daLiJeBeliKrst():
    if edges[0][0] == 0 and edges[0][2] == -10 and edges[0][3] == -12 and edges[0][4] == -11 and edges[0][5] == -9:
        return True
    return False
def beliKrst():
    inputEdges()
    if daLiJeBeliKrst():
        return


uradiAlgoritam(scramble)
zelenoBeliEdge()
print("RESENJE: ")
print(resenje)
ispisiKocku()
