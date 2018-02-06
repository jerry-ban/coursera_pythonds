for person in people:
	print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
	
times_tables = [j*i for i in range(10) for j in range(10)]

lst = []
for i in range(3):
	for j in range (4):
		lst.append(i*j)

import numpy as np
# creating arrays
mylist = [1,2,3]
x = np.array(mylist)

y= np.array([4,5,6])
z = np.array([[7,8,9], [10,11,12]])
z.shape()

n=np.arange(0,30,2)
n.reshape(3,5)

np.ones((3,2))
np.zeros((2,3))
np.eye(4)
np.diag([4,5,6])

np.array([1,2,3] *3)
np.repeat([1,2,3],3)

p=np.ones([2,3],int)
np.vstack([p, 2*p])
np.hstack([p, 2*p])


#Operations

x+y
x**2
z.T
z.T.shape
z.dtype

z.astype("f")
x.sum()
x.min()
x.max()
x.argmax()
x.argmin()


#Indexing and slicing
s=np.arange(13)**2
s[0], s[4], s[0:3]
s[1:5]
s[-4:]
s[-4::-2]


r=np.arange(36)
r.resize([6,6])
r[2,2]
r[2,3:5]
r[2, 3:]

r[:2, :-1]
r[-1, ::2]

r[r>30]

r[r>30] = -30

#copy
r2= r[:3, :3]
r2[:] = 0
# now r is also updated
r_copy = r.copy()
r_copy[:] = -1
r_copy


# Iterating over arrays
test = np.random.randint(0,10,(4,3))

for row in test:
	print(row)

for i in range(len(test)):
	print(test[i])

for i,row in enumerate((test)):
	print("row ", i, " is: ", row)

test2 = test**2
for i, j in zip(test,test2):
	print("(i,j): {},{}".format(i,j))
	print("i+j=> {}+{}={}".format(i,j,i+j))

r3 = np.arange(36)
r3=r3.reshape([6,6])
r3.reshape(36)[::7]