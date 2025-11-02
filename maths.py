

divis = 0
for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    string = str(a+1)+str(b+1)+str(c+1)+str(d+1)+str(e+1)
                    print(string)
                    if int(string) % 25 == 0:
                        divis += 1
print(divis)
total = 6*6*6*6*6
prob = divis / total
print(divis, "/", total, "=", round(prob,3))