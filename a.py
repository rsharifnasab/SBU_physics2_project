from matplotlib import pyplot as plt

db = []
step = 1
TedadElement = 25
toolZel = 100
kolQ = 100
K = 1/(4 * 3.1415926 * 8.85*10**(-12) )
max_dist = toolZel * 5

for fasele in range(1,max_dist,step):
    E = 0
    E2 = 0
    for i in range(TedadElement):
        for j in range(TedadElement):
            #UP
            dist = fasele**2
            dist += ((TedadElement/2 - i)*toolZel )**2
            dist += ((TedadElement/2 - i)*toolZel )**2
            ssin = fasele  / (dist**0.5)
            E += K * kolQ * ssin / (TedadElement**2) /dist
            #DOWN
            dist = (fasele+toolZel)**2
            dist += ((TedadElement/2 - i)*toolZel )**2
            dist += ((TedadElement/2 - i)*toolZel )**2
            ssin = fasele / (dist **0.5)
            E += K * kolQ * ssin / (TedadElement**2) /dist
            #ZEL
            dist = fasele**2
            dist += ((TedadElement/2 - i)*toolZel )**2
            dist += ((TedadElement/2 - i)*toolZel )**2
            ssin = fasele  / (dist**0.5)
            E2 += K * kolQ * ssin / (TedadElement**2) /dist
            E2 *=4
            #TODO
    print(fasele," : ",E)
    db.append(E)
print(max(db));
plt.bar(range(len(db)),db)
plt.show()
