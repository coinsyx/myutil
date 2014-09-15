from numpy import *


def normalize_by_row(arr):
    n = sum(arr,1)
    for i in range(shape(arr)[0]):
        arr[i,:] /= n[i]

def sample_multi(p):
    samp = random.multinomial(1, p)
    for i in range(len(samp)):
        if samp[i] == 1:
            return i
        
p = array([2.0, 3.0, 5.0])
p /= sum(p)

q = random.random((3,3))
normalize_by_row( q )

# metropolis-hasting 

# actual Markov transition matrix
qq = zeros((3,3))
for i in range(3):
    for j in range(3):
        alpha = min(1, (p[j]*q[j,i]) / (p[i]*q[i,j]))    
        qq[i,i] += q[i,j] * (1-alpha) # reject j, get i 
        qq[i,j] += q[i,j] * alpha  # accept j from i



n = [0.0] * 3   # sample count
x = 0           # init status
m = 4000        # burn-in iteration
for i in range(10000+m):
    y = sample_multi(q[x,:]) 
    alpha = min(1, (p[y]*q[y,x]) / (p[x]*q[x,y]))    
    u = random.random()
    if u <= alpha:
        x = y
    else:
        x = x
    if i >= m:
        n[x] += 1

print(n)








