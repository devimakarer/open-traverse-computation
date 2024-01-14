# devim akarer / term project / part-1
# open traverse computation

import math

print("This program calculates the coordinates in open traverse serie")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

# lists (we will use later)

IDlist = []
traverse_list = []
dis_list = []
azimuth_list = []
delta_x_list = []
delta_y_list = []
coord_x_list = []
coord_y_list = []

# input

first_kpID = input("Enter the point ID of first known point           : ")
first_kpyID = float(input("Enter the Y coordinates of first known point   (m): "))
first_kpxID = float(input("Enter the X coordinates of first known point   (m): "))
IDlist.append(first_kpID)
IDlist[0] = first_kpID
second_kpID = input("Enter the point ID of second known point          : ")
second_kpyID = float(input("Enter the Y coordinates of second known point  (m): "))
second_kpxID = float(input("Enter the X coordinates of second known point  (m): "))
IDlist.append(second_kpID)
IDlist[1] = second_kpID
number_of_tp = int(input("Enter the number of unknown traverse points       : "))

for dev in range(number_of_tp):
    print("Enter the point ID of unknown point", (dev + 1), "            : ", end="")
    p = input()
    IDlist.append(p)

a = 0
while a < (len(IDlist) - 2):
    a += 1
    print("Enter the traverse angle of ", IDlist[a], "(grad)             : ", end="")
    t = float(input())
    traverse_list.append(t)

b = 1
while b < (len(IDlist) - 1):
    print("Enter the horizontal distance between", IDlist[b], " and", IDlist[b + 1], "(m): ", end="")
    d = float(input())
    dis_list.append(d)
    b += 1

# calculations

imy = second_kpyID - first_kpyID
imx = second_kpxID - first_kpxID

if imy > 0 and imx > 0:
    az = math.atan(abs(imy / imx)) * 200 / math.pi
    son = az
    azimuth_list.append(son)
    azimuth_list[0] = son

elif imy < 0 and imx < 0:
    az = math.atan(abs(imy / imx)) * 200 / math.pi
    son = 200 + az
    azimuth_list.append(son)
    azimuth_list[0] = son

elif imy > 0 and imx < 0:
    az = math.atan(abs(imy / imx)) * 200 / math.pi
    son = 200 - az
    azimuth_list.append(son)
    azimuth_list[0] = son

elif imy == 0:
    if imx > 0:
        azimuth_list.append(300)
        azimuth_list[0] = 300
    else:
        azimuth_list.append(100)
        azimuth_list[0] = 100

elif imx == 0:
    if imy > 0:
        azimuth_list.append(0)
        azimuth_list[0] = 0
    else:
        azimuth_list.append(200)
        azimuth_list[0] = 200

elif imx == 0 and imy == 0:
    print("Same point!")

else:
    az = math.atan(abs(imy / imx)) * 200 / math.pi
    son = 400 - az
    azimuth_list.append(son)
    azimuth_list[0] = son
# conditions of next azimuth angle:
akr = 0
while akr < (len(traverse_list)):
    er = azimuth_list[akr] + traverse_list[akr]
    if er < 200:
        er += 200
        azimuth_list.append(er)
        akr = akr + 1
    elif 200 < er < 600:
        er = er - 200
        azimuth_list.append(er)
        akr = akr + 1
    elif er > 600:
        er = er - 600
        azimuth_list.append(float(er))
        akr = akr + 1
    er += 1

# calculations of delta x, delta y:

bil = 0
while bil < (len(azimuth_list) - 1):
    delta_x = math.cos(azimuth_list[bil + 1] * math.pi / 200) * dis_list[bil]
    delta_y = math.sin(azimuth_list[bil + 1] * math.pi / 200) * dis_list[bil]
    if azimuth_list[0] == 0:
        delta_x = 0
        delta_y = imy
    elif azimuth_list[0] == 100:
        delta_y = 0
        delta_x = -imx
    elif azimuth_list[0] == 200:
        delta_x = 0
        delta_y = -imy
    elif azimuth_list[0] == 300:
        delta_y = 0
        delta_x = imx
    else:
        delta_x = math.cos(azimuth_list[bil + 1] * math.pi / 200) * dis_list[bil]
        delta_y = math.sin(azimuth_list[bil + 1] * math.pi / 200) * dis_list[bil]

    delta_x_list.append(delta_x)
    delta_y_list.append(delta_y)

    bil += 1

# coordinates x, y

co = 0
while co < (len(azimuth_list) - 1):
    x = delta_x_list[co] + second_kpxID
    second_kpxID = x
    coord_x_list.append(second_kpxID)

    y = delta_y_list[co] + second_kpyID
    second_kpyID = y
    coord_y_list.append(second_kpyID)
    co += 1

# output

print(format("Point ID", "<10s"), format("Point ID", "<10s"), format("Azimuth", "<10s"), format("Delta Y", "<10s"),
      format("Delta X", "<10s"), end="\n")
print("---------------------------------------------------")

print(format(IDlist[0], "<10s"), format(str(IDlist[1]), "<10s"),
      format(str(format(azimuth_list[0], ".4f")), "<10s"), end="\n")

for fin in range(len(delta_x_list)):
    xxx1_729 = format(str(IDlist[fin + 1]), "<10s")
    xxx2_729 = format(str(IDlist[fin + 2]), "<10s")
    xxx3_729 = format(str(format(azimuth_list[fin + 1], ".4f")), "<10s")
    xxx4_729 = format(str(format(delta_y_list[fin], ".2f")), "<10s")
    xxx5_729 = format(str(format(delta_x_list[fin], ".2f")), "<10s")
    fin += 1
    print(xxx1_729, xxx2_729, xxx3_729, xxx4_729, xxx5_729, end="\n")
print("---------------------------------------------------")
print(format("Point ID", "<10s"), format("Coordinate(Y)", "<10s"), format("Coordinate(X)", "<10s"), end="\n")
print("--------------------------------------")

for ito in range(len(coord_x_list)):
    xxx6_729 = format(str(IDlist[ito + 2]), "<10s")
    xxx7_729 = format(str(format(coord_y_list[ito], ".2f")), "<10s")
    xxx8_729 = format(str(format(coord_x_list[ito], ".2f")), "<10s")
    print(xxx6_729, xxx7_729, xxx8_729, sep="")
print("--------------------------------------")
