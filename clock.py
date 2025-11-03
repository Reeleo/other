




def checkArithmetic(h,m,s):
    hmDiff = m-h
    msDiff = s-m
    if hmDiff == msDiff:
        return hmDiff
    else:
        return 0
    
def makeAccute(angle):
    if angle > 180:
        return 360-angle
    return angle

totals = []
for h in range(0,25):
    for m in range(1,61):
        for s in range(1,61):
            d = checkArithmetic(h,m,s)
            over12 = False
            if d != 0:
                if h > 12:
                    h -= 12
                    over12 = True
                hangle = h*30+m*0.5+s*(1/120)
                mangle = m*6+s*0.1
                sangle = s*6
                alpha = makeAccute(abs(hangle-mangle))
                beta = makeAccute(abs(mangle-sangle))
                gamma = makeAccute(abs(hangle-sangle))
                total = alpha+beta+gamma
                if over12:
                    d += 12
                if total < 50:
                    totals.append([round(total,2),": h",h,round(hangle,3),"m",m,round(mangle,3),"s",s,round(sangle,3)])

for i in range(len(totals)):
    print(totals[i])
                




















