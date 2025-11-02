
import math

# original 4,3,-2,4,3,-5

# -3.8,3,-2,4,3,-5
# 4,3,-2,4,3,-3
def reset():
    return 4,3,-2,4,3,-5



# RA ax -3.8   area: 10.6
# RA ax 17.4   area: 84.8
# RA bx -4.0   area: 32.5
# RA by 3.75   area: 24.375
# RA cx -3.5   area: 27.75
# RA cy -3.0   area: 18.5

many = True
if many:
    ax,ay,bx,by,cx,cy = reset()
    for i in range(6):
        ax,ay,bx,by,cx,cy = reset()
        for j in range(4000000):
            point = (j-2000000)/100000
            # print(point)
            if i == 0:
                ii = "ax"
                ax = point
            elif i == 1:
                ii = "ay"
                ay = point
            elif i == 2:
                ii = "bx"
                bx = point
            elif i == 3:
                ii = "by"
                by = point
            elif i == 4:
                ii = "cx"
                cx = point
            elif i == 5:
                ii = "cy"
                cy = point


            ab = (ax-bx)**2+(ay-by)**2
            rootab = math.sqrt(ab)

            bc = (bx-cx)**2+(by-cy)**2
            rootbc = math.sqrt(bc)

            ca = (cx-ax)**2+(cy-ay)**2
            rootca = math.sqrt(ca)

            if ab+bc == ca:
                print("RA",ii,point,"  area:",round(rootab*rootbc/2,3))
            elif bc+ca == ab:
                print("RA",ii,point,"  area:",round(rootbc*rootca/2,3))
            elif ab+ca == bc:
                print("RA",ii,point,"  area:",round(rootab*rootca/2,3))
else:
    ax,ay,bx,by,cx,cy = reset()
    ab = (ax-bx)**2+(ay-by)**2
    rootab = math.sqrt(ab)
    #print(ab)

    bc = (bx-cx)**2+(by-cy)**2

    rootbc = math.sqrt(bc)
    #print(bc)

    ca = (cx-ax)**2+(cy-ay)**2
    rootca = math.sqrt(ca)
    #print(ca)

    if ab+bc == ca:
        print("RA")
        print(round(rootab*rootbc/2,3))
    elif bc+ca == ab:
        print("RA")
        print(round(rootbc*rootca/2,3))
    elif ab+ca == bc:
        print("RA")
        print(round(rootab*rootca/2,3))



