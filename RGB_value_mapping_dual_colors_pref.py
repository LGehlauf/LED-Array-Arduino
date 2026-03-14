import itertools

import pygame
import sys

bigVal = 100000 # equivalent to 1 on paper
steps = 300 # steps to come 0 to bigVal, 6 times total

R = []
G = []
B = []

######################### 1 #########################
AdderA = 0
for x in range(0, steps):
    R.append(0)
    G.append(AdderA)
    B.append(bigVal)

    sum = R[-1] + G[-1] + B[-1]

    R[-1] = R[-1] * 6 / bigVal
    G[-1] = G[-1] * 6 / bigVal
    B[-1] = B[-1] * 6 / bigVal

    AdderA += bigVal / steps

# R.append(10000)
# G.append(10000)
# B.append(10000)

######################### 2 #########################
AdderA = bigVal
for x in range(0, steps):
    R.append(0)
    G.append(bigVal)
    B.append(AdderA)

    sum = R[-1] + G[-1] + B[-1]

    R[-1] = R[-1] * 6 / bigVal
    G[-1] = G[-1] * 6 / bigVal
    B[-1] = B[-1] * 6 / bigVal

    AdderA -= bigVal / steps

# R.append(20000)
# G.append(20000)
# B.append(20000)

######################### 3 #########################
AdderA = 0
for x in range(0, steps):
    R.append(AdderA)
    G.append(bigVal)
    B.append(0)

    sum = R[-1] + G[-1] + B[-1]

    R[-1] = R[-1] * 6 / bigVal
    G[-1] = G[-1] * 6 / bigVal
    B[-1] = B[-1] * 6 / bigVal

    AdderA += bigVal / steps

# R.append(30000)
# G.append(30000)
# B.append(30000)

######################### 4 #########################
AdderA = bigVal
for x in range(0, steps):
    R.append(bigVal)
    G.append(AdderA)
    B.append(0)

    sum = R[-1] + G[-1] + B[-1]

    R[-1] = R[-1] * 6 / bigVal
    G[-1] = G[-1] * 6 / bigVal
    B[-1] = B[-1] * 6 / bigVal

    AdderA -= bigVal / steps

# R.append(40000)
# G.append(40000)
# B.append(40000)

######################### 5 #########################
AdderA = 0
for x in range(0, steps):
    R.append(bigVal)
    G.append(0)
    B.append(AdderA)

    sum = R[-1] + G[-1] + B[-1]

    R[-1] = R[-1] * 6 / bigVal
    G[-1] = G[-1] * 6 / bigVal
    B[-1] = B[-1] * 6 / bigVal

    AdderA += bigVal / steps

# R.append(50000)
# G.append(50000)
# B.append(50000)


######################### 6 #########################
AdderA = bigVal
for x in range(0, steps):
    R.append(AdderA)
    G.append(0)
    B.append(bigVal)

    sum = R[-1] + G[-1] + B[-1]

    R[-1] = R[-1] * 6 / bigVal
    G[-1] = G[-1] * 6 / bigVal
    B[-1] = B[-1] * 6 / bigVal

    AdderA -= bigVal / steps

# R.append(60000)
# G.append(60000)
# B.append(60000)



# for i, elem in enumerate(R):
#     if R[i] + G[i] + B[i] < 5.99999 or R[i] + G[i] + B[i] > 6.000001:
#         print("ERROR != 6 in sum")



RoundR = [ round(elem, 3) for elem in R ]
RoundG = [ round(elem, 3) for elem in G ]
RoundB = [ round(elem, 3) for elem in B ]



# print(RoundR)
# print(RoundG)
# print(RoundB)


# shortR1 = [element for element in itertools.islice(RoundR, 0, 22)]
# shortG1 = [element for element in itertools.islice(RoundG, 0, 22)]
# shortB1 = [element for element in itertools.islice(RoundB, 0, 22)]

# shortR2 = [element for element in itertools.islice(RoundR, 22, 44)]
# shortG2 = [element for element in itertools.islice(RoundG, 22, 44)]
# shortB2 = [element for element in itertools.islice(RoundB, 22, 44)]

# shortR3 = [element for element in itertools.islice(RoundR, 44, 66)]
# shortG3 = [element for element in itertools.islice(RoundG, 44, 66)]
# shortB3 = [element for element in itertools.islice(RoundB, 44, 66)]

# print("R1-2:", shortR1)
# print("R3-4:", shortR2)
# print("R5-6:", shortR3)
# print("G1-2:", shortG1)
# print("G3-4:", shortG2)
# print("G5-6:", shortG3)
# print("B1-2:", shortB1)
# print("B3-4:", shortB2)
# print("B5-6:", shortB3)

# print("const PROGMEM float RainbowR[",len(R),"] = {", [el for el in R], "};", sep="", )
# print("const PROGMEM float RainbowG[",len(R),"] = {", [el for el in G], "};", sep="")
# print("const PROGMEM float RainbowB[",len(R),"] = {", [el for el in B], "};", sep="")
# print(len(R))

Mult = 20

RGame = [round(Mult * elem) for elem in R]
GGame = [round(Mult * elem) for elem in G]
BGame = [round(Mult * elem) for elem in B]

OldRoundR = 0
Rcounter = 0

OldRoundG = 0
Gcounter = 0

OldRoundB = 0
Bcounter = 0

RRangeList = []
GRangeList = []
BRangeList = []

for i in range(0, 500, 1):
#     NewRoundR = round(Mult * RoundR[i])
#     if NewRoundR != OldRoundR:
#         RRangeList.append(Rcounter)
#         # print("R", OldRoundR, "->", NewRoundR, Rcounter)
#         OldRoundR = NewRoundR
#         Rcounter = 0
#     Rcounter = Rcounter + 1

#     NewRoundG = round(Mult * RoundG[i])
#     if NewRoundG != OldRoundG:
#         GRangeList.append(Gcounter)
#         # print("G", Gcounter)
#         OldRoundG = NewRoundG
#         Gcounter = 0
#     Gcounter = Gcounter + 1

#     NewRoundB = round(Mult * RoundB[i])
#     if NewRoundB != OldRoundB:
#         BRangeList.append(Bcounter)
#         # print("B", OldRoundB, "->", NewRoundB,  Bcounter)
#         OldRoundB = NewRoundB
#         Bcounter = 0
#     Bcounter = Bcounter + 1

    # if i % 10 == 0:
    #     print("R", "RoundR", "G", "RoundG", "B", "RoundG", sep="\t")
    print(Mult * RoundR[i], round(Mult * RoundR[i]), Mult * RoundG[i], round(Mult * RoundG[i]), Mult * RoundB[i], round(Mult * RoundB[i]), sep="\t")

# print("RRangeList:", RRangeList, "GRangeList:", GRangeList, "BRangeList:", BRangeList, sep="\n")


# bei Mult = 2:     farbwechsel aller 570 ms -> 1.75 Hz
# bei Mult = 4:     farbwechsel aller 320
# bei Mult = 42:    farbwechsel aller 20 ms ->  50 Hz


# print([el for el in itertools.islice(RoundR, 0, 22)])

# RString = f"const PROGMEM float RainbowR[{len(R)}] = \u007b"
# RString += ",".join(str(element) for element in RoundR)
# RString += f"\u007d;"
# GString = f"const PROGMEM float RainbowG[{len(G)}] = \u007b"
# GString += ",".join(str(element) for element in RoundG)
# GString += f"\u007d;"
# BString = f"const PROGMEM float RainbowB[{len(B)}] = \u007b"
# BString += ",".join(str(element) for element in RoundB)
# BString += f"\u007d;"


# with open('RGBVal.txt', 'w', encoding="utf-8") as f:
#     f.write(RString + '\n')
#     f.write(GString + '\n')
#     f.write(BString)


# Funktion zum Umwandeln von RGB-Farben in ein pygame-Farbfeld
def convert_to_pygame_color(color):
    return tuple(color)

# Hauptfunktion
def main():
    # Initialisierung von pygame
    pygame.init()

    # Bildschirmgröße festlegen
    width, height = 1400, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RGB Farbwechsel")

    
    current_index = 0

    # Uhr für Zeitsteuerung
    clock = pygame.time.Clock()

    # Haupt-Loop
    while True:
        # Überprüfen auf Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Aktuelle Farbe zeichnen
        color = [RGame[current_index], GGame[current_index], BGame[current_index]]
        screen.fill(convert_to_pygame_color(color))
        # screen.fill(tuple([200,100,200]))
        # Farbwerte alle 10 ms wechseln
        pygame.display.flip()
        current_index = (current_index + 1) % len(R)

        # Wartezeit einhalten
        clock.tick(50)  # 100 fps = 10 ms pro Frame

if __name__ == "__main__":
    main()

