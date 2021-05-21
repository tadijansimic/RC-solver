class Kocka:
    r = ["", "", "", "", "", "", "", "", ""]
    l = ["", "", "", "", "", "", "", "", ""]
    f = ["", "", "", "", "", "", "", "", ""]
    b = ["", "", "", "", "", "", "", "", ""]
    u = ["", "", "", "", "", "", "", "", ""]
    d = ["", "", "", "", "", "", "", "", ""]

kocka = Kocka
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
    print(a + " " + b + " " + c)
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

mainInput()
inputEdges()
moveRight()
ispisiKocku()