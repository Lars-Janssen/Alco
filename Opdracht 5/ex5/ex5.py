import fileinput
invoer = []
for line in fileinput.input():
    invoer.append(line.split())

length = invoer[0][0]
ns = []
es = []
cs = []
ps = []
qs = []
lcms = []
ds = []
ms = []

for i in range(1, len(invoer)):
    ns.append(int(invoer[i][0]))
    es.append(int(invoer[i][1]))
    cs.append(int(invoer[i][2]))

for j in range(len(ns)):
    for i in range(2,(int(ns[j]/2+1))):
        if((ns[j] + 0.0)/i == int((ns[j] + 0.0)/i)):
            ps.append(i-1)
            qs.append(int(ns[j]/i)-1)
            break

for i in range(len(ps)):
    gcd = 1
    a = ps[i]
    b = qs[i]
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    lcms.append(int((ps[i] * qs[i])/a))

    for d in range(lcms[i]):
        if((d*es[i]) % lcms[i] == 1):
            ds.append(d)
            break

    message = 1
    for j in range(ds[i]):
        message = (message* cs[i]) % ns[i]
    ms.append(message)

for i in range(len(ms)):
    print(ms[i])

