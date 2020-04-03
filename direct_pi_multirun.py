import random
def directpi(N):
    n_hits=0
    for i in range(N):
        x,y = random.uniform(-1.0,1.0), random.uniform(-1.0,1.0)
        if x**2 + y**2 < 1.0:
            n_hits+=1
    return n_hits
n_runs = 1000
n_trials = 4000
file = open("myfile.txt","w") 
for run in range(n_runs):
    a = 4.0 * directpi(n_trials)/ float(n_trials)
    print(a)
file.write('a')
file.close()
