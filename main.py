from abc import abstractproperty
from os import scandir
import random
from tkinter.constants import END

class Kocka:
    f = ["G", "G", "G", "G", "G", "G", "G", "G", "G"]
    r = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
    b = ["B", "B", "B", "B", "B", "B", "B", "B", "B"]
    l = ["R", "R", "R", "R", "R", "R", "R", "R", "R"]
    u = ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]
    d = ["W", "W", "W", "W", "W", "W", "W", "W", "W"]

#scramble = list(map(str, input().split(" ")))
# class Kocka:
#     f = ["O", "B", "W", "G", "G", "O", "R", "B", "Y"]
#     r = ["G", "R", "G", "W", "O", "B", "O", "Y", "W"]
#     b = ["W", "R", "W", "Y", "B", "W", "B", "R", "R"]
#     l = ["B", "O", "Y", "R", "R", "W", "B", "O", "G"]
#     u = ["O", "G", "O", "G", "Y", "B", "B", "O", "R"]
#     d = ["Y", "W", "G", "Y", "W", "G", "Y", "Y", "R"]

kocka = Kocka
resenje = []

solvedEdges = [[0, 0, -10, -12, -11, -9], [0, 0, -2, -4, -3, -1], [10, 2, 0, 0, 6, -5], [12, 4, 0, 0, -7, 8], [11, 3, -6, 7, 0, 0], [9, 1, 5, -8, 0, 0]]
solvedCorners = [["GOY", "OBY", "BRY", "RGY"], ["GOW", "OBW", "BRW", "RGW"]]

corners = [["", "", "", ""], ["", "", "", ""]]
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
def inputCorners():
    corners[0][0] = kocka.f[2] + kocka.r[0] + kocka.u[8]
    corners[0][1] = kocka.r[2] + kocka.b[0] + kocka.u[2]
    corners[0][2] = kocka.b[2] + kocka.l[0] + kocka.u[0]
    corners[0][3] = kocka.l[2] + kocka.f[0] + kocka.u[6]
    corners[1][0] = kocka.f[8] + kocka.r[6] + kocka.d[2]
    corners[1][1] = kocka.r[8] + kocka.b[6] + kocka.d[8]
    corners[1][2] = kocka.b[8] + kocka.l[6] + kocka.d[6]
    corners[1][3] = kocka.l[8] + kocka.f[6] + kocka.d[0] 

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
def moveMPrim():
    a = kocka.f[1]
    b = kocka.f[7]
    c = kocka.f[4]
    kocka.f[1] = kocka.d[1]
    kocka.f[4] = kocka.d[4]
    kocka.f[7] = kocka.d[7]
    kocka.d[1] = kocka.b[7]
    kocka.d[4] = kocka.b[4]
    kocka.d[7] = kocka.b[1]
    kocka.b[1] = kocka.u[7]
    kocka.b[4] = kocka.u[4]
    kocka.b[7] = kocka.u[1]
    kocka.u[1] = a
    kocka.u[4] = c
    kocka.u[7] = b
def moveM():
    moveMPrim()
    moveMPrim()
    moveMPrim()
def moveS():
    a = kocka.u[3]
    b = kocka.u[5]
    c = kocka.u[4]
    kocka.u[3] = kocka.l[7]
    kocka.u[5] = kocka.l[1]
    kocka.u[4] = kocka.l[4]
    kocka.l[1] = kocka.d[3]
    kocka.l[7] = kocka.d[5]
    kocka.l[4] = kocka.d[4]
    kocka.d[3] = kocka.r[7]
    kocka.d[5] = kocka.r[1]
    kocka.d[4] = kocka.r[4]
    kocka.r[1] = a
    kocka.r[7] = b
    kocka.r[4] = c
def moveSPrim():
    moveS()
    moveS()
    moveS()
def moveE():
    a = kocka.f[3]
    b = kocka.f[5]
    c = kocka.f[4]
    kocka.f[3] = kocka.l[3]
    kocka.f[5] = kocka.l[5]
    kocka.f[4] = kocka.l[4]
    kocka.l[5] = kocka.b[5]
    kocka.l[3] = kocka.b[3]
    kocka.l[4] = kocka.b[4]
    kocka.b[3] = kocka.r[3]
    kocka.b[5] = kocka.r[5]
    kocka.b[4] = kocka.r[4]
    kocka.r[3] = a
    kocka.r[5] = b
    kocka.r[4] = c
def moveEPrim():
    moveE()
    moveE()
    moveE()
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
def M2():
    moveMPrim()
    moveMPrim()
def E2():
    moveE()
    moveE()
def S2():
    moveS()
    moveS()

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
        elif i == "M":
            moveM()
        elif i == "M'":
            moveMPrim()
        elif i == "S":
            moveS()
        elif i == "S'":
            moveSPrim()
        elif i == "E":
            moveE()
        elif i == "E'":
            moveEPrim()
        elif i == "E2":
            E2()
        elif i == "M2":
            M2()
        elif i == "S2":
            S2()
        elif i == "X":
            moveMPrim()
            moveRight()
            moveLeftPrim()
        elif i == "X2":
            M2()
            L2()
            R2()
        elif i == "X'":
            moveM()
            moveRightPrim()
            moveLeft()
        elif i == "Y":
            moveEPrim()
            moveDownPrim()
            moveUp()
        elif i == "Y2":
            E2()
            D2()
            U2()
        elif i == "Y'":
            moveE()
            moveDown()
            moveUpPrim()
        elif i == "Z":
            moveS()
            moveFront()
            moveBackPrim()
        elif i == "Z2":
            S2()
            F2()
            B2()
        elif i == "Z'":
            moveSPrim()
            moveBack()
            moveFrontPrim()

def zelenoBeliEdge():
    a = edges[5][0]
    if a == 1:
        uradiAlgoritam(["F2"])
        resenje.append(["F2"])
        return
    if a == -1:
        uradiAlgoritam(["U'", "R'", "F"])
        resenje.append(["U'", "R'", "F"])
        return
    if a == 2:
        uradiAlgoritam(["U", "F2"])
        resenje.append(["U", "F2"])
        return
    if a == -2:
        uradiAlgoritam(["R'", "F"])
        resenje.append(["R'", "F"])
        return
    if a == 3:
        uradiAlgoritam(["U2", "F2"])
        resenje.append(["U2", "F2"])
        return
    if a == -3:
        uradiAlgoritam(["U", "R'", "F"])
        resenje.append(["U", "R'", "F"])
        return
    if a == 4:
        uradiAlgoritam(["U'", "F2"])
        resenje.append(["U'", "F2"])
        return
    if a == -4:
        uradiAlgoritam(["L", "F'"])
        resenje.append(["L", "F'"])
    if a == 5:
        uradiAlgoritam(["F"])
        resenje.append(["F"])
        return
    if a == -5:
        uradiAlgoritam(["R", "U", "F2"])
        resenje.append(["R", "U", "F2"])
        return
    if a == 6:
        uradiAlgoritam(["R", "D'"])
        resenje.append(["R", "D'"])
        return
    if a == -6:
        uradiAlgoritam(["B'", "D2"])
        resenje.append(["B'", "D2"])
        return
    if a == 7:
        uradiAlgoritam(["B", "D2"])
        resenje.append(["B", "D2"])
        return
    if a == -7:
        uradiAlgoritam(["L'", "D"])
        resenje.append(["L'", "D"])
        return
    if a == 8:
        uradiAlgoritam(["L", "D"])
        resenje.append(["L", "D"])
        return
    if a == -8:
        uradiAlgoritam(["F'"])
        resenje.append(["F'"])
        return
    if a == -9:
        uradiAlgoritam(["F'", "R'", "D'"])
        resenje.append(["F'", "R'", "D'"])
        return
    if a == 10:
        uradiAlgoritam(["D'"])
        resenje.append(["D'"])
        return
    if a == -10:
        uradiAlgoritam(["R", "F"])
        resenje.append(["R", "F"])
        return
    if a == 11:
        uradiAlgoritam(["D2"])
        resenje.append(["D2"])
        return
    if a == -11:
        uradiAlgoritam(["D'", "R", "F"])
        resenje.append(["D'", "R", "F"])
        return
    if a == 12:
        uradiAlgoritam(["D"])
        resenje.append(["D"])
        return
    if a == -12:
        uradiAlgoritam(["L'", "F'"])
        resenje.append(["L'", "F'"])
        return
def plavoBeliEdge():
    if(edges[4][0] == 1):
        uradiAlgoritam(["U2", "B2"])
        resenje.append(["U2", "B2"])
        return
    elif(edges[4][0] == -1):
        uradiAlgoritam(["U", "L'", "B"])
        resenje.append(["U", "L'", "B"])
        return
    elif(edges[4][0] == 2):
        uradiAlgoritam(["U'", "B2"])
        resenje.append(["U'", "B2"])
    elif(edges[4][0] == -2):
        uradiAlgoritam(["R", "B'"])
        resenje.append(["R", "B'"])
    elif(edges[4][0] == 3):
        uradiAlgoritam(["B2"])
        resenje.append(["B2"])
    elif(edges[4][0] == -3):
        uradiAlgoritam(["U'", "L'", "B"])
        resenje.append(["U'", "L'", "B"])
    elif(edges[4][0] == 4):
        uradiAlgoritam(["U", "B2"])
        resenje.append(["U", "B2"])
    elif(edges[4][0] == -4):
        uradiAlgoritam(["L'", "B"])
        resenje.append(["L'", "B"])
    elif(edges[4][0] == 5):
        uradiAlgoritam(["R2", "B'"])
        resenje.append(["R2", "B'"])
    elif(edges[4][0] == -5):
        uradiAlgoritam(["R", "U'", "B2"])
        resenje.append(["R", "U'", "B2"])
    elif(edges[4][0] == 6):
        uradiAlgoritam(["R'", "U'", "B2"])
        resenje.append(["R'", "U'", "B2"])
    elif(edges[4][0] == -6):
        uradiAlgoritam(["B'"])
        resenje.append(["B'"])
    elif(edges[4][0] == 7):
        uradiAlgoritam(["B"])
        resenje.append(["B"])
    elif(edges[4][0] == -7):
        uradiAlgoritam(["L", "U", "B2"])
        resenje.append(["L", "U", "B2"])
    elif(edges[4][0] == 8):
        uradiAlgoritam(["D", "L", "D'"])
        resenje.append(["D", "L", "D'"])
    elif(edges[4][0] == -8):
        uradiAlgoritam(["L2", "B"])
        resenje.append(["L2", "B"])
    elif(edges[4][0] == 10):
        uradiAlgoritam(["R2", "U'", "B2"])
        resenje.append(["R2", "U'", "B2"])
    elif(edges[4][0] == -10):
        uradiAlgoritam(["R'", "B'"])
        resenje.append(["R'", "B'"])
    elif(edges[4][0] == -11):
        uradiAlgoritam(["B", "D'", "R", "D"])
        resenje.append(["B", "D'", "R", "D"])
    elif(edges[4][0] == 12):
        uradiAlgoritam(["L", "D", "L'", "D'"])
        resenje.append(["L", "D", "L'", "D'"])
    elif(edges[4][0] == -12):
        uradiAlgoritam(["L", "B"])
        resenje.append(["L", "B"])
def narandzastoBeliEdge():
    if(edges[2][0] == 1):
        uradiAlgoritam(["U'", "R2"])
        resenje.append(["U'", "R2"])
        return
    if(edges[2][0] == -1):
        uradiAlgoritam(["F", "R'", "F'"])
        resenje.append(["F", "R'", "F'"])
        return
    if(edges[2][0] == 2):
        uradiAlgoritam(["R2"])
        resenje.append(["R2"])
        return
    if(edges[2][0] == -2):
        uradiAlgoritam(["U", "F", "R'", "F'"])
        resenje.append(["U", "F", "R'", "F'"])
        return
    if(edges[2][0] == 3):
        uradiAlgoritam(["U", "R2"])
        resenje.append(["U", "R2"])
        return
    if(edges[2][0] == -3):
        uradiAlgoritam(["B'", "R", "B"])
        resenje.append(["B'", "R", "B"])
        return
    if(edges[2][0] == 4):
        uradiAlgoritam(["U2", "R2"])
        resenje.append(["U2", "R2"])
        return
    if(edges[2][0] == -4):
        uradiAlgoritam(["U'", "F", "R'", "F'"])
        resenje.append(["U'", "F", "R'", "F'"])
        return
    if(edges[2][0] == 5):
        uradiAlgoritam(["D'", "F", "D"])
        resenje.append(["D'", "F", "D"])
        return
    if(edges[2][0] == -5):
        uradiAlgoritam(["R'"])
        resenje.append(["R'"])
        return
    if(edges[2][0] == 6):
        uradiAlgoritam(["R"])
        resenje.append(["R"])
        return
    if(edges[2][0] == -6):
        uradiAlgoritam(["D", "B'", "D'"])
        resenje.append(["D", "B'", "D'"])
        return
    if(edges[2][0] == 7):
        uradiAlgoritam(["D", "B", "D'"])
        resenje.append(["D", "B", "D'"])
        return
    if(edges[2][0] == -7):
        uradiAlgoritam(["B2", "R", "B2"])
        resenje.append(["B2", "R", "B2"])
        return
    if(edges[2][0] == 8):
        uradiAlgoritam(["L'", "U2", "R2"])
        resenje.append(["L'", "U2", "R2"])
        return
    if(edges[2][0] == -8):
        uradiAlgoritam(["F", "U'", "F'", "R2"])
        resenje.append(["F", "U'", "F'", "R2"])
        return
    if(edges[2][0] == -10):
        uradiAlgoritam(["R", "F'", "U'", "F", "R2"])
        resenje.append(["R", "F'", "U'", "F", "R2"])
        return
    if(edges[2][0] == 12):
        uradiAlgoritam(["L2", "U2", "R2"])
        resenje.append(["L2", "U2", "R2"])
        return
    if(edges[2][0] == -12):
        uradiAlgoritam(["L2", "U'", "F", "R'", "F'"])
        resenje.append(["L2", "U'", "F", "R'", "F'"])
        return
def crvenoBeliEdge():
    if(edges[3][0] == 12):
        return
    if(edges[3][0] == 1):
        uradiAlgoritam(["U", "L2"])
        resenje.append(["U", "L2"])
        return
    if(edges[3][0] == -1):
        uradiAlgoritam(["F'", "L", "F"])
        resenje.append(["F'", "L", "F"])
        return
    if(edges[3][0] == 2):
        uradiAlgoritam(["U2", "L2"])
        resenje.append(["U2", "L2"])
        return
    if(edges[3][0] == -2):
        uradiAlgoritam(["U", "F'", "L", "F"])
        resenje.append(["U", "F'", "L", "F"])
        return
    if(edges[3][0] == 3):
        uradiAlgoritam(["U'", "L2"])
        resenje.append(["U'", "L2"])
        return
    if(edges[3][0] == -3):
        uradiAlgoritam(["B", "L'", "B'"])
        resenje.append(["B", "L'", "B'"])
        return
    if(edges[3][0] == 4):
        uradiAlgoritam(["L2"])
        resenje.append(["L2"])
        return
    if(edges[3][0] == -4):
        uradiAlgoritam(["U'", "F'", "L", "F"])
        resenje.append(["U'", "F'", "L", "F"])
        return
    if(edges[3][0] == 5):
        uradiAlgoritam(["R", "U", "R'", "F'", "L", "F"])
        resenje.append(["R", "U", "R'", "F'", "L", "F"])
        return
    if(edges[3][0] == -5):
        uradiAlgoritam(["R", "U2", "R'", "L2"])
        resenje.append(["R", "U2", "R'", "L2"])
        return
    if(edges[3][0] == 6):
        uradiAlgoritam(["B2", "L'", "B2"])
        resenje.append(["B2", "L'", "B2"])
        return
    if(edges[3][0] == -6):
        uradiAlgoritam(["R'", "U", "R", "F'", "L", "F"])
        resenje.append(["R'", "U", "R", "F'", "L", "F"])
        return
    if(edges[3][0] == 7):
        uradiAlgoritam(["B'", "U'", "B", "L2"])
        resenje.append(["B'", "U'", "B", "L2"])
        return
    if(edges[3][0] == -7):
        uradiAlgoritam(["L'"])
        resenje.append(["L'"])
        return
    if(edges[3][0] == 8):
        uradiAlgoritam(["L"])
        resenje.append(["L"])
        return
    if(edges[3][0] == -8):
        uradiAlgoritam(["F", "U", "F'", "L2"])
        resenje.append(["F", "U", "F'", "L2"])
        return
    if(edges[3][0] == -12):
        uradiAlgoritam(["L2", "U'", "F'", "L", "F"])
        resenje.append(["L2", "U'", "F'", "L", "F"])
        return

def daLiJeRotirana():
    if kocka.f[4] == "G" and kocka.u[4] == "Y":
        return True
    return False
def rotiraj():
    if daLiJeRotirana():
        return
    if kocka.u[4] == "G":
        uradiAlgoritam(["X'"])
        resenje.append(["X'"])
    elif kocka.b[4] == "G":
        uradiAlgoritam(["X2"])
        resenje.append(["X2"])
    elif kocka.d[4] == "G":
        uradiAlgoritam(["X"])
        resenje.append(["X"])
    elif kocka.r[4] == "G":
        uradiAlgoritam(["Y"])
        resenje.append(["Y"])
    elif kocka.l[4] == "G":
        uradiAlgoritam(["Y'"])
        resenje.append(["Y'"])
    
    if daLiJeRotirana():
        return
    if kocka.r[4] == "Y":
        uradiAlgoritam(["Z'"])
        resenje.append(["Z'"])
    elif kocka.d[4] == "Y":
        uradiAlgoritam(["Z2"])
        resenje.append(["Z2"])
    elif kocka.l[4] == "Y":
        uradiAlgoritam(["Z"])
        resenje.append(["Z"])

def daLiJeBeliKrst():
    if edges[0][2] == -10 and edges[0][3] == -12 and edges[0][4] == -11 and edges[0][5] == -9:
        return True
    return False
def beliKrst():
    inputEdges()
    zelenoBeliEdge()
    inputEdges()
    plavoBeliEdge()
    inputEdges()
    narandzastoBeliEdge()
    inputEdges()
    crvenoBeliEdge()

def testCrossNTimes():
    potezi = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2", "M", "M2", "M'", "S", "S2", "S'", "E", "E'", "E2", "X", "Y", "Z"]

    tacnih = 0
    rotacija = 0
    crveni = 0
    plavi = 0
    zeleni = 0
    narandzasti = 0

    fRotacija = open("ErrRotacija.txt", "w")
    fPlavi = open("ErrPlavi.txt", "w")
    fZeleni = open("ErrZeleni.txt", "w")
    fNarandzasti = open("ErrNarandzasti.txt", "w")
    fCrveni = open("ErrCrveni.txt", "w")
    fPlavi.truncate(0)
    fZeleni.truncate(0)
    fCrveni.truncate(0)
    fNarandzasti.truncate(0)
    fRotacija.truncate(0)

    n = int(input("Testova za rad: "))

    for i in range(n):
        duzina = random.randrange(5, 25)
        scramble = []
        strScramble = ""
        resenje = []

        for j in range(duzina): 
            scramble.append(random.choice(potezi))
            if j != 0:
                strScramble += ", "
            strScramble += '"' + scramble[j] + '"'
        strScramble += "\n"
        print("Scramble: ", end="")
        print(scramble)
        uradiAlgoritam(scramble)

        rotiraj()
        if daLiJeRotirana():  
            print("pass rotacija")
            rotacija += 1

        beliKrst()

        print("Resenje: ", end="")
        print(resenje)
        print("Output: ", end="")

        inputEdges()
        if daLiJeBeliKrst():
            print("pass\n")
            tacnih += 1
            continue
        else:
            print("fail\n")
            inputEdges()
            if edges[0][5] != -9:
                zeleni += 1
                fZeleni.write(strScramble)
            if edges[0][2] != -10:
                narandzasti += 1
                fNarandzasti.write(strScramble)
                fNarandzasti.write(str(edges[0][2]))
                fNarandzasti.write("\n\n")
            if edges[0][4] != -11:
                plavi += 1
                fPlavi.write(strScramble)
            if edges[0][3] != -12:
                crveni += 1
                fCrveni.write(strScramble)
            print()

    print("\nDobrih rotacija: ", end="")
    print(rotacija)

    print("Pass: ", end="")
    print(tacnih, end=" / ")
    print(n, end="\n\n")
    print("FAILURES:")
    print("Zeleni     : ", end="")
    print(zeleni)
    print("Narandzasti: ", end="")
    print(narandzasti)
    print("Plavi      : ", end="")
    print(plavi)
    print("Crveni     : ", end="")
    print(crveni)

    fCrveni.close()
    fPlavi.close()
    fNarandzasti.close()
    fZeleni.close()
def testCrossInput(scramble):
    uradiAlgoritam(scramble)
    rotiraj()
    beliKrst()
    ispisiKocku()
    print(resenje)

def zelenoNarandzastoBeli():
    if corners[0][0] == "GOW" or corners[0][0] == "GWO" or corners[0][0] == "WGO" or corners[0][0] == "WOG" or corners[0][0] == "OGW" or corners[0][0] == "OWG":
        uradiAlgoritam(["R'", "F", "R", "F'"])
        resenje.append(["R'", "F", "R", "F'"])
        return
    if corners[0][1] == "GOW" or corners[0][1] == "GWO" or corners[0][1] == "WGO" or corners[0][1] == "WOG" or corners[0][1] == "OGW" or corners[0][1] == "OWG":
        uradiAlgoritam(["U", "R'", "F", "R", "F'"])
        resenje.append(["U", "R'", "F", "R", "F'"])
        return
    if corners[0][2] == "GOW" or corners[0][2] == "GWO" or corners[0][2] == "WGO" or corners[0][2] == "WOG" or corners[0][2] == "OGW" or corners[0][2] == "OWG":
        uradiAlgoritam(["U2", "R'", "F", "R", "F'"])
        resenje.append(["U2", "R'", "F", "R", "F'"])
        return
    if corners[0][3] == "GOW" or corners[0][3] == "GWO" or corners[0][3] == "WGO" or corners[0][3] == "WOG" or corners[0][3] == "OGW" or corners[0][3] == "OWG":
        uradiAlgoritam(["U'", "R'", "F", "R", "F'"])
        resenje.append(["U'", "R'", "F", "R", "F'"])
        return
    if corners[1][0] == "GOW" or corners[1][0] == "GWO" or corners[1][0] == "WGO" or corners[1][0] == "WOG" or corners[1][0] == "OGW" or corners[1][0] == "OWG":
        return
    if corners[1][1] == "GOW" or corners[1][1] == "GWO" or corners[1][1] == "WGO" or corners[1][1] == "WOG" or corners[1][1] == "OGW" or corners[1][1] == "OWG":
        uradiAlgoritam(["R'", "U2", "R", "U'", "R'", "F", "R", "F'"])
        resenje.append(["R'", "U2", "R", "U'", "R'", "F", "R", "F'"])
        return
    if corners[1][2] == "GOW" or corners[1][2] == "GWO" or corners[1][2] == "WGO" or corners[1][2] == "WOG" or corners[1][2] == "OGW" or corners[1][2] == "OWG":
        uradiAlgoritam(["L", "U2", "L'", "R'", "F", "R", "F'"])
        resenje.append(["L", "U2", "L'", "R'", "F", "R", "F'"])
        return
    if corners[1][3] == "GOW" or corners[1][3] == "GWO" or corners[1][3] == "WGO" or corners[1][3] == "WOG" or corners[1][3] == "OGW" or corners[1][3] == "OWG":
        uradiAlgoritam(["F", "U", "F'", "U2", "R'", "F", "R", "F'"])
        resenje.append(["F", "U", "F'", "U2", "R'", "F", "R", "F'"])
        return
def narandzastoPlavoBeli():
    if corners[0][0] == "OBW" or corners[0][0] == "OWB" or corners[0][0] == "WOB" or corners[0][0] == "WBO" or corners[0][0] == "BOW" or corners[0][0] == "BWO":
        uradiAlgoritam(["U", "R'", "U2", "R"])
        resenje.append(["U", "R'", "U2", "R"])
        return
    if corners[0][1] == "OBW" or corners[0][1] == "OWB" or corners[0][1] == "WOB" or corners[0][1] == "WBO" or corners[0][1] == "BOW" or corners[0][1] == "BWO":
        uradiAlgoritam(["U'", "R'", "U", "R"])
        resenje.append(["U'", "R'", "U", "R"])
        return
    if corners[0][2] == "OBW" or corners[0][2] == "OWB" or corners[0][2] == "WOB" or corners[0][2] == "WBO" or corners[0][2] == "BOW" or corners[0][2] == "BWO":
        uradiAlgoritam(["R'", "U", "R"])
        resenje.append(["R'", "U", "R"])
        return
    if corners[0][3] == "OBW" or corners[0][3] == "OWB" or corners[0][3] == "WOB" or corners[0][3] == "WBO" or corners[0][3] == "BOW" or corners[0][3] == "BWO":
        uradiAlgoritam(["R'", "U2", "R"])
        resenje.append(["R'", "U2", "R"])
        return
    if corners[1][2] == "OBW" or corners[1][2] == "OWB" or corners[1][2] == "WOB" or corners[1][2] == "WBO" or corners[1][2] == "BOW" or corners[1][2] == "BWO":
        uradiAlgoritam(["R'", "L", "U", "L'", "R"])
        resenje.append(["R'", "L", "U", "L'", "R"])
        return
    if corners[1][3] == "OBW" or corners[1][3] == "OWB" or corners[1][3] == "WOB" or corners[1][3] == "WBO" or corners[1][3] == "BOW" or corners[1][3] == "BWO":
        uradiAlgoritam(["L'", "R'", "U2", "R", "L"])
        resenje.append(["L'", "R'", "U2", "R", "L"])
        return
def plavoCrvenoBeli():
    if corners[0][0] == "BRW" or corners[0][0] == "BWR" or corners[0][0] == "WBR" or corners[0][0] == "WRB" or corners[0][0] == "RBW" or corners[0][0] == "RWB":
        uradiAlgoritam(["L", "U2", "L'"])
        resenje.append(["L", "U2", "L'"])
        return
    if corners[0][1] == "BRW" or corners[0][1] == "BWR" or corners[0][1] == "WBR" or corners[0][1] == "WRB" or corners[0][1] == "RBW" or corners[0][1] == "RWB":
        uradiAlgoritam(["L", "U'", "L'"])
        resenje.append(["L", "U'", "L'"])
        return
    if corners[0][2] == "BRW" or corners[0][2] == "BWR" or corners[0][2] == "WBR" or corners[0][2] == "WRB" or corners[0][2] == "RBW" or corners[0][2] == "RWB":
        uradiAlgoritam(["U", "L", "U'", "L'"])
        resenje.append(["U", "L", "U'", "L'"])
        return
    if corners[0][3] == "BRW" or corners[0][3] == "BWR" or corners[0][3] == "WBR" or corners[0][3] == "WRB" or corners[0][3] == "RBW" or corners[0][3] == "RWB":
        uradiAlgoritam(["U'", "L", "U2", "L'"])
        resenje.append(["U'", "L", "U2", "L'"])
        return
    if corners[1][3] == "BRW" or corners[1][3] == "BWR" or corners[1][3] == "WBR" or corners[1][3] == "WRB" or corners[1][3] == "RBW" or corners[1][3] == "RWB":
        uradiAlgoritam(["L'", "U2", "L2", "U'", "L'"])
        resenje.append(["L'", "U2", "L2", "U'", "L'"])
        return
def crvenoZelenoBeli():
    if corners[0][0] == "RGW" or corners[0][0] == "GWR" or corners[0][0] == "WRG" or corners[0][0] == "RWG" or corners[0][0] == "GRW" or corners[0][0] == "WGR":
        uradiAlgoritam(["L'", "U", "L"])
        resenje.append(["L'", "U", "L"])
    if corners[0][1] == "RGW" or corners[0][1] == "GWR" or corners[0][1] == "WRG" or corners[0][1] == "RWG" or corners[0][1] == "GRW" or corners[0][1] == "WGR":
        uradiAlgoritam(["L'", "U2", "L"])
        resenje.append(["L'", "U2", "L"])
    if corners[0][2] == "RGW" or corners[0][2] == "GWR" or corners[0][2] == "WRG" or corners[0][2] == "RWG" or corners[0][2] == "GRW" or corners[0][2] == "WGR":
        uradiAlgoritam(["U", "L'", "U2", "L"])
        resenje.append(["U", "L'", "U2", "L"])
    if corners[0][3] == "RGW" or corners[0][3] == "GWR" or corners[0][3] == "WRG" or corners[0][3] == "RWG" or corners[0][3] == "GRW" or corners[0][3] == "WGR":
        uradiAlgoritam(["U'", "L'", "U", "L"])
        resenje.append(["U'", "L'", "U", "L"])
def belaStrana():
    inputCorners()
    zelenoNarandzastoBeli()
    inputCorners()
    narandzastoPlavoBeli()
    inputCorners()
    plavoCrvenoBeli()
    inputCorners()
    crvenoZelenoBeli()
    inputCorners()
    print(corners[1])
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    uradiAlgoritam(["D"])
    resenje.append(["D"])
    inputCorners()
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    uradiAlgoritam(["D"])
    resenje.append(["D"])
    inputCorners()
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    uradiAlgoritam(["D"])
    resenje.append(["D"])
    inputCorners()
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    if kocka.d[2] != "W":
        uradiAlgoritam(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
        resenje.append(["R", "U", "R'", "U'", "R", "U", "R'", "U'"])
    uradiAlgoritam(["D"])
    resenje.append(["D"])

def test2Layers():
    potezi = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2", "M", "M2", "M'", "S", "S2", "S'", "E", "E'", "E2", "X", "Y", "Z"]

    tacnih = 0

    n = int(input("Testova za rad: "))

    for i in range(n):
        duzina = random.randrange(5, 25)
        scramble = []
        strScramble = ""
        resenje = []

        for j in range(duzina): 
            scramble.append(random.choice(potezi))
            if j != 0:
                strScramble += ", "
            strScramble += '"' + scramble[j] + '"'
        strScramble += "\n"
        print("Scramble: ", end="")
        print(scramble)
        uradiAlgoritam(scramble)
        
        rotiraj()
        beliKrst()
        belaStrana()
        drugiLayer()
        gornjiCross()
        print("Resenje: ", end="")
        print(resenje)
        print("Output: ", end="")

        inputEdges()
        if daLiJeBeliKrst():
            inputCorners()
            if corners[1] == solvedCorners[1]:
                if kocka.u[5] == "Y" and kocka.u[1] == "Y" and kocka.u[3] == "Y" and kocka.u[7] == "Y":
                    print("pass")
                    tacnih += 1
                    continue
        print("fail")
        print(corners[1], end="\n\n")
        print()


    print("Pass: ", end="")
    print(tacnih, end=" / ")
    print(n)
def test2LayersS(scramble):
    print(scramble, end="\n\n")
    uradiAlgoritam(scramble)
    rotiraj()
    beliKrst()
    belaStrana()
    drugiLayer()
    ispisiKocku()
    print(resenje)

def narandzastoZeleniEdge():
    inputEdges()
    if edges[2][5] == -1:
        uradiAlgoritam(["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
        resenje.append(["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
        return
    if edges[2][5] == -2:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == -3:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == -4:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 2:
        uradiAlgoritam(["U'", "F'", "U", "F", "U", "R", "U'", "R'"])
        resenje.append(["U'", "F'", "U", "F", "U", "R", "U'", "R'"])
        return
    if edges[2][5] == 1:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 3:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 4:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 5:
        uradiAlgoritam(["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
        resenje.append(["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 6 or edges[2][5] == -6:
        uradiAlgoritam(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
        resenje.append(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 7 or edges[2][5] == -7:
        uradiAlgoritam(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        resenje.append(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        narandzastoZeleniEdge()
        return
    if edges[2][5] == 8 or edges[2][5] == -8:
        uradiAlgoritam(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        resenje.append(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        narandzastoZeleniEdge()
        return
def narandzastoPlaviEdge():
    inputEdges()
    if edges[2][4] == 2:
        uradiAlgoritam(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
        resenje.append(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
        return
    if edges[2][4] == 1:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == 3:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == 4:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == -3:
        uradiAlgoritam(["U'", "R'", "U", "R", "U", "B", "U'", "B'"])
        resenje.append(["U'", "R'", "U", "R", "U", "B", "U'", "B'"])
        return
    if edges[2][4] == -1:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == -2:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == -4:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == -6:
        uradiAlgoritam(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
        resenje.append(["U", "B", "U'", "B'", "U'", "R'", "U", "R"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == -7 or edges[2][4] == 7:
        uradiAlgoritam(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        resenje.append(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        narandzastoPlaviEdge()
        return
    if edges[2][4] == 8 or edges[2][4] == -8:
        uradiAlgoritam(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        resenje.append(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        narandzastoPlaviEdge()
        return
def plavoCrveniEdge():
    inputEdges()
    if edges[4][3] == -4:
        uradiAlgoritam(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        resenje.append(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        return
    if edges[4][3] == -1:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        plavoCrveniEdge()
        return
    if edges[4][3] == -2:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        plavoCrveniEdge()
        return
    if edges[4][3] == -3:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        plavoCrveniEdge()
        return
    if edges[4][3] == 3:
        uradiAlgoritam(["U", "L", "U'", "L'", "U'", "B'", "U", "B"])
        resenje.append(["U", "L", "U'", "L'", "U'", "B'", "U", "B"])
        return
    if edges[4][3] == 1:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        plavoCrveniEdge()
        return
    if edges[4][3] == 2:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        plavoCrveniEdge()
        return
    if edges[4][3] == 4:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        plavoCrveniEdge()
        return
    if edges[4][3] == -6:
        uradiAlgoritam(["U", "L", "U'", "L'", "U'", "B'", "U", "B"])
        resenje.append(["U", "L", "U'", "L'", "U'", "B'", "U", "B"])
        plavoCrveniEdge()
        return
    if edges[4][3] == 7 or edges[4][3] == -7:
        uradiAlgoritam(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        resenje.append(["U'", "B'", "U", "B", "U", "L", "U'", "L'"])
        plavoCrveniEdge()
        return
    if edges[4][3] == 8 or edges[4][3] == -8:
        uradiAlgoritam(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        resenje.append(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        plavoCrveniEdge()
        return
def crvenoZeleniEdge():
    inputEdges()
    if edges[3][5] == -1:
        uradiAlgoritam(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        resenje.append(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        return
    if edges[3][5] == -2:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        crvenoZeleniEdge()
        return
    if edges[3][5] == -3:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        crvenoZeleniEdge()
        return
    if edges[3][5] == -4:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        crvenoZeleniEdge()
        return
    if edges[3][5] == 4:
        uradiAlgoritam(["U", "F", "U'", "F'", "U'", "L'", "U", "L"])
        resenje.append(["U", "F", "U'", "F'", "U'", "L'", "U", "L"])
        return
    if edges[3][5] == 1:
        uradiAlgoritam(["U"])
        resenje.append(["U"])
        crvenoZeleniEdge()
        return
    if edges[3][5] == 3:
        uradiAlgoritam(["U'"])
        resenje.append(["U'"])
        crvenoZeleniEdge()
        return
    if edges[3][5] == 2:
        uradiAlgoritam(["U2"])
        resenje.append(["U2"])
        crvenoZeleniEdge()
        return
    if edges[3][5] == -8:
        uradiAlgoritam(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        resenje.append(["U'", "L'", "U", "L", "U", "F", "U'", "F'"])
        crvenoZeleniEdge()
        return
def drugiLayer():
    narandzastoZeleniEdge()
    narandzastoPlaviEdge()
    plavoCrveniEdge()
    crvenoZeleniEdge()

def gornjiCross():
    if kocka.u[1] != "Y" and kocka.u[3] != "Y" and kocka.u[5] != "Y" and kocka.u[7] != "Y":
        uradiAlgoritam(["F", "R", "U", "R'", "U'", "S", "R", "U", "R'", "U'", "S'", "F'"])
        resenje.append(["F", "R", "U", "R'", "U'", "S", "R", "U", "R'", "U'", "S'", "F'"])
        return
    if kocka.u[5] == "Y" and kocka.u[1] == "Y" and kocka.u[3] == "Y" and kocka.u[7] == "Y":
        return
    if kocka.u[5] == "Y" and kocka.u[7] == "Y":
        uradiAlgoritam(["F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        resenje.append(["F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        return
    if kocka.u[5] == "Y" and kocka.u[1] == "Y":
        uradiAlgoritam(["U", "F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        resenje.append(["U", "F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        return
    if kocka.u[1] == "Y" and kocka.u[3] == "Y":
        uradiAlgoritam(["U2", "F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        resenje.append(["U2", "F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        return
    if kocka.u[3] == "Y" and kocka.u[7] == "Y":
        uradiAlgoritam(["U'", "F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        resenje.append(["U'", "F", "S", "R", "U", "R'", "U'", "S'", "F'"])
        return
    if kocka.u[3] == "Y" and kocka.u[5] == "Y":
        uradiAlgoritam(["F", "R", "U", "R'", "U'", "F'"])
        resenje.append(["F", "R", "U", "R'", "U'", "F'"])
        return
    if kocka.u[1] == "Y" and kocka.u[7] == "Y":
        uradiAlgoritam(["U", "F", "R", "U", "R'", "U'", "F'"])
        resenje.append(["U", "F", "R", "U", "R'", "U'", "F'"])
        return
    print("Edge is twisted!")

test2Layers()
