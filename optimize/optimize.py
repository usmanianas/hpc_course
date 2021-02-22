from datetime import datetime
import numpy as np


N = 10**5

a =  np.random.random(N)
b =  np.random.random(N)
c = np.empty(N)
c1 = np.empty(N)
c2 = np.empty(N)

# with loop
t1 = datetime.now()
for i in range(N):
    c[i] = a[i] + b[i]
t2 = datetime.now()

print ("for loop, time = ", t2-t1)
looptime = t2-t1


t1 = datetime.now()
c1 = a + b
t2 = datetime.now()
print ("for vectorised ops, time = ", t2-t1)

#print(c2/c1)

vecttime = t2-t1

print(looptime/vecttime)

'''

## 2D loop
N = 10**3
a2 = np.random.random((N,N))
b2 = np.random.random((N,N))
c2 = np.random.random((N,N))

t1 = datetime.now()
#c2[0:N, 0:N] = a2[0:N, 0:N] * b2[0:N, 0:N]
c2 = a2 * b2
t2 = datetime.now()

vecttime = t2-t1

print ("for vectorised ops, time = ", t2-t1)
#or vectorised ops, time =  0:00:00.799441

t1 = datetime.now()
for i in range(N):
	for j in range(N):
		c2[i,j] = a2[i,j]*b2[i,j]

t2 = datetime.now()

looptime = t2-t1

print ("for loop, time = ", t2-t1)

print(looptime/vecttime)


## 2D loop
N = 10**2
a2 = np.random.random((N,N,N))
b2 = np.random.random((N,N,N))
c2 = np.random.random((N,N,N))

t1 = datetime.now()
c2[0:N, 0:N, 0:N] = a2[0:N, 0:N, 0:N] * b2[0:N, 0:N, 0:N]
#c2 = a2 * b2
t2 = datetime.now()

vecttime = t2-t1

print ("for vectorised ops, time = ", t2-t1)
#or vectorised ops, time =  0:00:00.799441

t1 = datetime.now()
for i in range(N):
	for j in range(N):
		for k in range(N):
			c2[i,j,k] = a2[i,j,k]*b2[i,j,k]

t2 = datetime.now()

looptime = t2-t1

print ("for loop, time = ", t2-t1)

print(looptime/vecttime)

#for loop_i_j, time =  0:00:55.346258




t1 = datetime.now()
for j in range(N):
	for i in range(N):
		c2[i,j] = a2[i,j]*b2[i,j]

t2 = datetime.now()
print ("for loop_j_i, time = ", t2-t1)
#for loop_j_i, time =  0:01:06.284808



t1 = datetime.now()
for i in range(N):
	for j in range(N):
		if (a2[i,j] > 0.5):
			c2[i,j] = a2[i,j]*b2[i,j]
		else:
			c2[i,j] = -a2[i,j]*b2[i,j]

t2 = datetime.now()
print ("for loop_i_j_with_if, time = ", t2-t1)		
# for loop_i_j, time =  0:01:23.087140


a =  np.random.random((10**4,10**4))
b =  np.random.random((10**4,10**4))

t1 = datetime.now()

c = a*b

t2 = datetime.now()
print ("for loop_j_i, time = ", t2-t1)
#for loop_j_i, time =  0:01:06.284808
'''
