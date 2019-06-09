from matplotlib import pyplot as plt

db = {}
z_step = 1
integ_step = 1
l = 100
K = 1/(4 * 3.1415926 * 8.85*10**(-12) )
k = 1
max_dist = l//2 * 5


for z in range(1,max_dist,z_step): #UP
    E_up = 0
    for x in range(- l//2 , l//2 + 1, integ_step):
        for y in range(- l//2 , l//2+1, integ_step):
            if(l//2 == z): continue
            r = (x**2 + y**2 + (l//2 - z)**2 ) ** 0.5
            #print(" r is : ",r)
            dE = (K * z) / (r**3)
            ccos = z / r
            dE_z = dE * (z / r)
            E_up += dE_z
    db[z] = E_up

plt.bar(db.keys(),db.values())
plt.show()
