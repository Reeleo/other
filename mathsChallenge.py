
sum = 0
for i in range(1,9):
    for j in range(10,21):
        for k in range(1,10):
            num = (str(i)+str(j)+str(k))
            sum += int(num)
print(sum)
#3686760


tum = 0
for i in range(1,9):
    for j in range(10,21):
        for k in range(1,10):
            num = (i*1000*j*10*k)
            tum += int(num)
print(tum)
#2673000000

print(sum/tum)
#0.0013792592592592593