from matplotlib import pyplot as plt

db = {}
z_step = 1
integ_step = 1
l = 100
K = 1/(4 * 3.1415926 * 8.85*10**(-12) )
K = 1
max_dist = l//2 * 8
print("calculating")

for z in range(0,max_dist,z_step): #UP

    E_up = 0
    for x in range(- l//2 , l//2, integ_step):
        for y in range(- l//2 , l//2, integ_step):
            z2 = l//2 - z
            if z2 == 0: continue

            r = (x**2 + y**2 + z2**2 ) ** 0.5
            dE = (K * z2) / (r**3)
            #dE = (k)/(r*r) #TODO
            E_up += dE
    db[z] = E_up * -1
print("...")
for z in range(0,max_dist,z_step): #DOWN
    E_down = 0
    for x in range(- l//2 , l//2, integ_step):
        for y in range(- l//2 , l//2, integ_step):
            z2 = l//2 + z
            if z2 == 0: continue
            r = (x**2 + y**2 + z2**2 ) ** 0.5
            dE = (K * z2) / (r**3)
            #dE = (K)/(r*r) #TODO
            E_down += dE
    db[z] += E_down * 1
print("...")
for z in range(0,max_dist,z_step): #SIDE
    E_SIDE = 0
    y = l//2
    for x in range(- l//2 , l//2, integ_step):
        for zl in range(- l//2 , l//2, integ_step):
            z2 = z-zl
            r = (x**2 + y**2 + z2**2 ) ** 0.5
            dE = (K * z2) / (r**3)
            #dE = (K)/(r*r) #TODO
            E_SIDE += dE
    db[z] += E_SIDE * 4

print("done, opening output")
plt.bar(db.keys(),db.values())
plt.show()
